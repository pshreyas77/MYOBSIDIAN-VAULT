#!/usr/bin/env bash
# cost-check.sh — budget / rate-limit safety (BUILD 6).
# On the free tier we enforce a DAILY TICK CAP (rate-limit safety) plus the
# optional USD budget from the guide. Exit 1 = over budget -> loop.sh exits 3.
set -euo pipefail
F="$(dirname "$0")/../memory/usage.log"; TICKF="$(dirname "$0")/../memory/ticks.today"
touch "$F" "$TICKF"; TODAY="$(date +%F)"
MAX_TICKS="${MAX_TICKS:-50}"

case "${1:-}" in
  --budget)
    spent="$(awk -F'\t' -v d="$TODAY" '$1 ~ d {s+=$3} END{printf "%.2f",s+0}' "$F")"
    awk -v s="$spent" -v b="$2" 'BEGIN{exit (s>=b)?1:0}' \
      || { echo "spent \$$spent of \$$2" >&2; exit 1; };;
  --tick)
    grep -q "$TODAY" "$TICKF" || echo "$TODAY	0" > "$TICKF"
    n="$(cut -f2 "$TICKF" | head -1)"
    awk -v n="$n" -v cap="$MAX_TICKS" 'BEGIN{exit (n>=cap)?1:0}' \
      || { echo "tick cap $MAX_TICKS reached for $TODAY" >&2; exit 1; };;
  --report)
    awk -F'\t' -v since="$(date -d '7 days ago' +%F 2>/dev/null || date -v-7d +%F 2>/dev/null || echo 1970-01-01)" \
      '$1>=since{s[$2]+=$3;t+=$3} END{for(k in s) printf "  %-10s $%.2f\n",k,s[k]; printf "  TOTAL      $%.2f\n",t+0}' "$F";;
esac
