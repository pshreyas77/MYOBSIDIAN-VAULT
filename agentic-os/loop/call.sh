#!/usr/bin/env bash
# call.sh — portable LLM seat for the Agentic OS.
# Replaces `claude -p` / `llm -s` from the guide. Talks to OpenRouter
# (tencent/hy3:free by default) via curl + python3. No jq, no claude CLI,
# no llm CLI required.
#
# Usage:
#   ./call.sh <role> "<system prompt>" "<user prompt>" [model] [max_tokens]
#   roles: triage | conductor | worker | verifier
#   Writes the model's text reply to stdout. Exits 0 on success.
#
# Env:
#   OPENROUTER_API_KEY  (required) — set in your shell profile / .env
#   CHEAP / WORKER      (optional) — override the cheap seats
set -euo pipefail

ROLE="${1:-conductor}"
SYS="${2:-}"
USR="${3:-}"
MODEL="${4:-tencent/hy3:free}"
MAX="${5:-32000}"

# Cheap seats default to the same free model (hy3:free) so the loop costs $0.
# Override CHEAP/WORKER with any OpenRouter slug you have quota for.
if [[ "$ROLE" == triage ]];  then MODEL="${CHEAP:-tencent/hy3:free}"; MAX="${MAX:-8000}"; fi
if [[ "$ROLE" == worker ]];  then MODEL="${WORKER:-tencent/hy3:free}"; MAX="${MAX:-16000}"; fi
if [[ "$ROLE" == conductor ]]; then MODEL="${MODEL:-tencent/hy3:free}"; MAX="${MAX:-64000}"; fi
if [[ "$ROLE" == verifier ]];  then MODEL="${MODEL:-tencent/hy3:free}"; MAX="${MAX:-16000}"; fi

if [[ -z "${OPENROUTER_API_KEY:-}" ]]; then
  echo "ERROR: OPENROUTER_API_KEY not set" >&2
  exit 4
fi

# Build the JSON request body with python3 (avoids jq dependency).
PAYLOAD="$(python3 - "$SYS" "$USR" "$MODEL" "$MAX" <<'PY'
import json, sys
sys_p, usr_p, model, max_t = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
body = {
  "model": model,
  "max_tokens": max_t,
  "messages": [
    {"role": "system", "content": sys_p},
    {"role": "user",   "content": usr_p}
  ]
}
print(json.dumps(body))
PY
)"

# Call OpenRouter. Capture HTTP status.
HTTP_BODY="$(curl -sS --max-time 300 \
  -w '\n__HTTP_STATUS__%{http_code}' \
  -H "Authorization: Bearer ${OPENROUTER_API_KEY}" \
  -H "Content-Type: application/json" \
  -H "HTTP-Referer: http://localhost/agentic-os" \
  -H "X-Title: agentic-os" \
  -d "$PAYLOAD" \
  "https://openrouter.ai/api/v1/chat/completions")"

HTTP_STATUS="$(printf '%s\n' "$HTTP_BODY" | sed -n 's/.*__HTTP_STATUS__//p')"
BODY_JSON="$(printf '%s\n' "$HTTP_BODY" | sed '/__HTTP_STATUS__/d')"

if [[ "$HTTP_STATUS" != "200" ]]; then
  echo "ERROR: OpenRouter HTTP $HTTP_STATUS" >&2
  printf '%s\n' "$BODY_JSON" | head -c 500 >&2
  exit 5
fi

# Refusal detection (Fable-style): finish_reason == "content_filter" or
# stop_reason "refusal". On hy3 this is rare, but check anyway.
FINISH="$(printf '%s\n' "$BODY_JSON" | python3 -c 'import json,sys
try:
  d=json.load(sys.stdin)
  c=d.get("choices",[{}])[0]
  print(c.get("finish_reason","") or "")
except Exception:
  print("")' 2>/dev/null || true)"
if [[ "$FINISH" == "content_filter" ]]; then
  echo "REFUSAL" >&2
  exit 6
fi

# Extract assistant text. Falls back to whole body on parse failure.
printf '%s\n' "$BODY_JSON" | python3 -c 'import json,sys
try:
  d=json.load(sys.stdin)
  print(d["choices"][0]["message"]["content"])
except Exception:
  sys.stderr.write("WARN: could not parse response\n")
  sys.exit(7)' || printf '%s\n' "$BODY_JSON"
