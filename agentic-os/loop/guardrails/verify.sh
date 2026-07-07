#!/usr/bin/env bash
# verify.sh — the deterministic gate. The bash script holds the final vote.
# Edit the commands below to match your repo's test stack.
set -e

# --- EDIT THIS BLOCK FOR YOUR STACK ---
npm run typecheck --if-present
npm test --if-present
npm run lint --if-present
# ---------------------------------------

# If any command above exits non-zero, `set -e` aborts and this script
# returns a failing status. That is the gate vote: NO SHIP.
echo "verify.sh: green"
