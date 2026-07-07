#!/usr/bin/env bash
# quorum.sh — optional loop (BUILD 7). INSTALL WHEN: dispatch shows
# conductor wake-ups that produced action: stop. Three cheap seats vote;
# conductor wakes on 2 of 3. Voters never see each other's answers.
# Adapted: voters use ./call.sh with $CHEAP; no `llm` CLI.
set -uo pipefail
cd "$(dirname "$0")"
: > /tmp/signals.txt
{ git log --oneline -20; gh issue list --limit 20 2>/dev/null || true; gh run list --limit 10 2>/dev/null || true; } > /tmp/signals.txt

V=0
for m in "tencent/hy3:free" "deepseek/deepseek-v3" "moonshotai/kimi-k2"; do
  OUT="$(CHEAP="$m" ./call.sh triage "$(cat triage.md)" "$(cat /tmp/signals.txt)" 2>/dev/null || true)"
  printf '%s' "$OUT" | grep -q "status: actionable" && V=$((V+1))
done
[ "$V" -ge 2 ] && { echo "quorum: wake ($V/3)"; exec ./loop.sh; } || echo "quorum: quiet ($V/3)"
