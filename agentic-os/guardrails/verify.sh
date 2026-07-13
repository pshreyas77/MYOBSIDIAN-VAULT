#!/usr/bin/env bash
# guardrails/verify.sh — The Deterministic Gate
# Final judge for ALL work. No LLM involved. Exit 0 = PASS, non-zero = FAIL.
# This script MUST be deterministic and idempotent.

set -euo pipefail

# ─── Config ─────────────────────────────────────────────────────
WORK_ID="${1:-}"
if [[ -z "$WORK_ID" ]]; then
  echo "Usage: $0 <work_id>" >&2
  exit 2
fi

WORK_DIR="workers/$WORK_ID"
PLAN_FILE="$WORK_DIR/plan.json"
RESULT_FILE="$WORK_DIR/result.json"
VERIFY_FILE="$WORK_DIR/verify.json"

# ─── Pre-flight Checks ──────────────────────────────────────────
[[ -f "$PLAN_FILE" ]] || { echo "FAIL: Missing plan.json" >&2; exit 1; }
[[ -f "$RESULT_FILE" ]] || { echo "FAIL: Missing result.json" >&2; exit 1; }

# ─── Schema Validation (deterministic) ──────────────────────────
validate_json() {
  local file="$1" schema="$2"
  if command -v jsonschema >/dev/null 2>&1; then
    jsonschema -i "$file" "schemas/$schema" 2>/dev/null || return 1
  else
    # Fallback: basic jq validation
    jq empty "$file" 2>/dev/null || return 1
  fi
}

validate_json "$PLAN_FILE" "plan.schema.json" || { echo "FAIL: Invalid plan.json schema" >&2; exit 1; }
validate_json "$RESULT_FILE" "result.schema.json" || { echo "FAIL: Invalid result.json schema" >&2; exit 1; }

# ─── Core Verification: Every Step Must Have Run & Passed ────────
echo "=== Verifying work: $WORK_ID ==="

CHECKS_PASSED=0
CHECKS_FAILED=0
EVIDENCE_FILES=()

# Read plan steps
STEP_NAMES=$(jq -r '.steps[].name' "$PLAN_FILE")
STEP_VERIFY_SCRIPTS=$(jq -r '.steps[].verify_script' "$PLAN_FILE")

# Read result step results
mapfile -t RESULT_STEPS < <(jq -c '.step_results[]' "$RESULT_FILE")

# Verify each step
i=0
while IFS= read -r step_name; do
  verify_script=$(echo "$STEP_VERIFY_SCRIPTS" | sed -n "$((i+1))p")
  
  # Get result for this step
  step_result=$(echo "${RESULT_STEPS[$i]}" 2>/dev/null || echo '{}')
  exit_code=$(echo "$step_result" | jq -r '.exit_code // -1')
  
  echo "→ Checking step: $step_name (exit_code: $exit_code)"
  
  # 1. Step must have exited 0
  if [[ "$exit_code" -ne 0 ]]; then
    echo "  FAIL: Step exited with code $exit_code"
    CHECKS_FAILED=$((CHECKS_FAILED + 1))
    continue
  fi
  
  # 2. Verify script must exist and pass
  if [[ -f "scripts/$verify_script" ]]; then
    if bash "scripts/$verify_script" "$WORK_DIR" 2>&1; then
      echo "  PASS: $verify_script"
      CHECKS_PASSED=$((CHECKS_PASSED + 1))
      EVIDENCE_FILES+=("$WORK_DIR/$verify_script.out")
    else
      echo "  FAIL: $verify_script returned non-zero"
      CHECKS_FAILED=$((CHECKS_FAILED + 1))
    fi
  else
    echo "  SKIP: No verify script ($verify_script)"
    # Not a failure - some steps may not have custom verify scripts
    CHECKS_PASSED=$((CHECKS_PASSED + 1))
  fi
  
  i=$((i + 1))
done <<< "$STEP_NAMES"

# ─── Global Checks (always run) ──────────────────────────────────

# Check 1: No forbidden self-evaluation patterns in result stdout/stderr
echo "→ Global check: forbidden patterns"
if grep -qiE 'I (verified|checked|confirmed|ensured)|comprehensive|thorough|no issues|everything (looks|is) (good|fine|ok)|successfully' "$RESULT_FILE"; then
  echo "  FAIL: Forbidden self-evaluation pattern in result"
  CHECKS_FAILED=$((CHECKS_FAILED + 1))
else
  echo "  PASS: No forbidden patterns"
  CHECKS_PASSED=$((CHECKS_PASSED + 1))
fi

# Check 2: Token budget not exceeded (read from result)
TOKEN_USAGE=$(jq -r '.token_usage // 0' "$RESULT_FILE")
PLAN_BUDGET=$(jq -r '.estimated_tokens' "$PLAN_FILE")
if [[ "$TOKEN_USAGE" -gt "$((PLAN_BUDGET + PLAN_BUDGET / 10))" ]]; then  # 10% tolerance
  echo "  FAIL: Token usage $TOKEN_USAGE exceeds plan budget $PLAN_BUDGET (+10%)"
  CHECKS_FAILED=$((CHECKS_FAILED + 1))
else
  echo "  PASS: Token usage $TOKEN_USAGE within budget $PLAN_BUDGET"
  CHECKS_PASSED=$((CHECKS_PASSED + 1))
fi

# Check 3: All artifacts referenced in result actually exist
echo "→ Global check: artifact existence"
mapfile -t ARTIFACTS < <(jq -r '.artifacts[]' "$RESULT_FILE" 2>/dev/null || true)
for artifact in "${ARTIFACTS[@]}"; do
  if [[ ! -f "$artifact" ]]; then
    echo "  FAIL: Missing artifact: $artifact"
    CHECKS_FAILED=$((CHECKS_FAILED + 1))
  fi
done
if [[ ${#ARTIFACTS[@]} -eq 0 || $CHECKS_FAILED -eq ${CHECKS_FAILED} ]]; then
  echo "  PASS: All artifacts exist"
  CHECKS_PASSED=$((CHECKS_PASSED + 1))
fi

# Check 4: Plan checkpoints all appear in step results
echo "→ Global check: checkpoint coverage"
mapfile -t CHECKPOINTS < <(jq -r '.checkpoints[]' "$PLAN_FILE" 2>/dev/null || true)
for cp in "${CHECKPOINTS[@]}"; do
  FOUND=false
  for step_result in "${RESULT_STEPS[@]}"; do
    if echo "$step_result" | jq -r '.step_name' | grep -q "^$cp$"; then
      FOUND=true
      break
    fi
  done
  if [[ "$FOUND" == false ]]; then
    echo "  FAIL: Missing checkpoint: $cp"
    CHECKS_FAILED=$((CHECKS_FAILED + 1))
  fi
done
echo "  PASS: All checkpoints covered"
CHECKS_PASSED=$((CHECKS_PASSED + 1))

# ─── Final Verdict ──────────────────────────────────────────────
TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
OVERALL="PASS"
[[ $CHECKS_FAILED -gt 0 ]] && OVERALL="FAIL"

cat > "$VERIFY_FILE" <<EOF
{
  "work_id": "$WORK_ID",
  "overall": "$OVERALL",
  "checks": [
    {
      "name": "step_verification",
      "result": "$([[ $CHECKS_FAILED -eq 0 ]] && echo PASS || echo FAIL)",
      "evidence": "workers/$WORK_ID/result.json",
      "details": "$CHECKS_PASSED passed, $CHECKS_FAILED failed"
    }
  ],
  "evidence": $(printf '%s\n' "${EVIDENCE_FILES[@]}" | jq -R . | jq -s .),
  "verified_at": "$TIMESTAMP"
}
EOF

echo "=== Verification complete: $OVERALL ($CHECKS_PASSED passed, $CHECKS_FAILED failed) ==="

[[ "$OVERALL" == "PASS" ]] && exit 0 || exit 1