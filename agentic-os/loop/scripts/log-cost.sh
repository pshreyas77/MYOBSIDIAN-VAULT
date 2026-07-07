#!/usr/bin/env bash
# log-cost.sh — append a usage event (BUILD 6).
# hy3:free costs $0, so we log ticks instead of dollars. If you wire a
# paid seat, the third arg is the dollar cost and it flows to cost-check.sh.
set -uo pipefail
echo -e "$(date -Is)\t${1:-unknown}\t${2:-0}" >> "$(dirname "$0")/../memory/usage.log"
# tick counter for rate-limit safety
TICKF="$(dirname "$0")/../memory/ticks.today"; TODAY="$(date +%F)"
touch "$TICKF"
if ! grep -q "$TODAY" "$TICKF"; then echo "$TODAY	0" > "$TICKF"; fi
n="$(cut -f2 "$TICKF" | head -1)"; n=$((n+1))
sed -i "s/^$TODAY\t.*/$TODAY\t$n/" "$TICKF"
