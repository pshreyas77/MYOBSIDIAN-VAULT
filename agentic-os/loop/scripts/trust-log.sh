#!/usr/bin/env bash
# trust-log.sh — the trust ledger (BUILD 4).
# usage: trust-log.sh <skill> <pass|fail> | --render | --tier <skill>
# Autonomy is PER SKILL, not per loop. Tier rules:
#   auto   = 20+ runs AND 95%+ pass  -> ships unattended
#   queue  = verified drafts wait for you
#   watch  = <10 runs OR <90% pass    -> draft-only
set -euo pipefail
F="$(dirname "$0")/../memory/trust.tsv"; touch "$F"

tier_of() { awk -v r="$1" -v p="$2" 'BEGIN{
  rate=(r>0)?p/r:0
  if (r>=20 && rate>=0.95) print "auto"
  else if (r<10 || rate<0.90) print "watch"
  else print "queue"}'; }

case "${1:-}" in
  --render)
    printf "%-20s %5s %5s %6s %s\n" skill runs pass rate tier
    while IFS=$'\t' read -r s r p; do [ -z "$s" ] && continue
      printf "%-20s %5s %5s %5s%% %s\n" "$s" "$r" "$p" \
        "$(awk -v r="$r" -v p="$p" 'BEGIN{printf "%.0f",(r>0)?p/r*100:0}')" \
        "$(tier_of "$r" "$p")"; done < "$F";;
  --tier)
    line="$(grep -P "^${2}\\t" "$F" 2>/dev/null || echo -e "${2}\t0\t0")"
    tier_of "$(cut -f2 <<<"$line")" "$(cut -f3 <<<"$line")";;
  *)
    awk -v s="$1" -v r="$2" -F'\t' 'BEGIN{OFS="\t"; f=0}
      $1==s {f=1; print s,$2+1,$3+(r=="pass"); next} {print}
      END{if(!f) print s,1,(r=="pass")?1:0}' "$F" > "$F.t" && mv "$F.t" "$F"
    if [ "$2" = fail ]; then
      runs="$(grep -P "^${1}\\t" "$F" 2>/dev/null | cut -f2 || echo 0)"
      [ "$(./trust-log.sh --tier "$1")" = watch ] && [ "${runs:-0}" -ge 10 ] \
        && echo "ALERT: $1 demoted to watch after $runs runs" >&2 || true
    fi;;
esac
