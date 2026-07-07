#!/usr/bin/env bash
# loop.sh — the heartbeat (BUILD 3).
# Adapted from the Fable 5 guide: every LLM seat goes through ./call.sh
# (OpenRouter, tencent/hy3:free), all JSON parsing is python3 (no jq),
# and `gh` PR creation is optional. The deterministic gate is unchanged.
set -uo pipefail
LOOP_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$LOOP_DIR"

# --- Config (override via env) ---
export MAX_ITERS="${MAX_ITERS:-10}"
export DAILY_BUDGET_USD="${DAILY_BUDGET_USD:-5}"   # hy3:free is $0; this caps ticks
export MAX_TICKS="${MAX_TICKS:-50}"                 # hard daily tick ceiling (rate-limit safety)
export CHEAP="${CHEAP:-tencent/hy3:free}"
export WORKER="${WORKER:-tencent/hy3:free}"
REPO_ROOT="${TARGET_REPO:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
echo "loop: managing repo $REPO_ROOT (ticks left cap=$MAX_TICKS)"

./scripts/cost-check.sh --budget "$DAILY_BUDGET_USD" || exit 3

for ((i=1; i<=MAX_ITERS; i++)); do
  # 0 tick guard
  ./scripts/cost-check.sh --tick || exit 3

  # 1 TRIAGE: quiet-tick gate, ~free
  TRIAGE_IN="$(
    git -C "$REPO_ROOT" log --oneline -20 2>/dev/null
    echo "---ISSUES---"
    gh -C "$REPO_ROOT" issue list --limit 20 2>/dev/null || true
    echo "---RUNS---"
    gh -C "$REPO_ROOT" run list --limit 10 2>/dev/null || true
  )"
  T_OUT="$(./call.sh triage "$(cat triage.md)" "$TRIAGE_IN" 2>>memory/STATE.md)"
  ./scripts/log-cost.sh triage 0.0
  printf '\n%s\n' "$T_OUT" >> memory/STATE.md
  grep -q "status: actionable" memory/STATE.md || { echo quiet; exit 0; }

  # 2 CONDUCT: hy3:free, fresh context, read-only, JSON out
  C_OUT="$(./call.sh conductor "$(cat conductor.md)" \
    "STATE: $(cat memory/STATE.md)
TRUST: $(./scripts/trust-log.sh --render)
CONTRACT: $(cat contract.md)" 2>>memory/STATE.md)"
  ./scripts/log-cost.sh conductor 0.0
  printf '%s\n' "$C_OUT" > work-order.json

  # 2a ROUTE-TOLERANCE: never iterate on output we didn't get (empty/REFUSAL = reroute)
  if [[ -z "$C_OUT" || "$C_OUT" == *"REFUSAL"* ]]; then
    echo "rerouted" >> memory/STATE.md; exit 2
  fi

  # parse via python3 (no jq)
  python3 - work-order.json >/dev/null <<'PY' || { echo "bad work order JSON"; exit 2; }
import json, sys
d = json.load(open(sys.argv[1]))
assert {"action","item","skill","spec","done_when"} <= set(d), "missing fields"
PY
  SKILL="$(python3 -c 'import json;print(json.load(open("work-order.json"))["skill"])')"
  ACTION="$(python3 -c 'import json;print(json.load(open("work-order.json"))["action"])')"
  [[ "$ACTION" == stop  ]] && exit 0
  [[ "$ACTION" == queue ]] && { echo "queued: $SKILL" >> memory/STATE.md; continue; }

  # 3 EXECUTE: cheap worker, isolated worktree
  WT="$REPO_ROOT/../wt-$i"
  git -C "$REPO_ROOT" worktree add "$WT" -b "loop/$SKILL-$i" >/dev/null 2>&1 || {
    echo "worktree add failed" >> memory/STATE.md; continue; }
  ( cd "$WT" && ./call.sh worker "$(cat "$LOOP_DIR/workers/implement.md")" "$(cat "$LOOP_DIR/work-order.json")" \
      > IMPLEMENTATION.md 2>&1 )
  ./scripts/log-cost.sh worker 0.0

  # 4 VERIFY: fresh hy3, no tools, sees only spec + diff
  DIFF="$(cd "$WT" && git --no-pager diff)"
  V="$(./call.sh verifier "$(cat workers/verify.md)" \
    "SPEC: $(python3 -c 'import json;print(json.load(open("work-order.json"))["spec"])')
DIFF:
$DIFF" 2>>memory/STATE.md)"
  ./scripts/log-cost.sh verifier 0.0

  # 5 GATE: deterministic; then ledger; ship only at auto tier
  if [[ "$V" == PASS* ]] && ( cd "$WT" && "$OLDPWD/guardrails/verify.sh" ); then
    ./scripts/trust-log.sh "$SKILL" pass
    if [[ "$(./scripts/trust-log.sh --tier "$SKILL")" == auto ]]; then
      ( cd "$WT" && git add -A && git commit -qm "loop: $SKILL" && (gh pr create --fill || true) )
      echo "- shipped: $SKILL" >> memory/STATE.md
    else
      echo "- review: $SKILL in $WT" >> memory/STATE.md
    fi
  else
    ./scripts/trust-log.sh "$SKILL" fail
    echo "- FAILED: $SKILL in $WT" >> memory/STATE.md
  fi
done
exit 1   # iteration cap without stop: check STATE.md
