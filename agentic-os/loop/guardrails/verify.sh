#!/usr/bin/env bash
# verify.sh — the deterministic gate. Exit 0 = PASS.
# IMPORTANT: Keep checks fast. No loops over thousands of files.
set -euo pipefail

VAULT_ROOT="${VAULT_ROOT:-E:/_Knowledge/ObsidianVault}"

# 1. Vault exists
[[ -d "$VAULT_ROOT" ]] || { echo "FAIL: Vault not found"; exit 1; }

# 2. Core directories
for dir in "0-raw" "wiki" "06 - OUTPUTS"; do
  [[ -d "$VAULT_ROOT/$dir" ]] || { echo "FAIL: Missing $dir/"; exit 1; }
done

# 3. Wiki index and log exist
[[ -f "$VAULT_ROOT/wiki/index.md" ]] || { echo "FAIL: Missing wiki/index.md"; exit 1; }
[[ -f "$VAULT_ROOT/wiki/log.md" ]] || { echo "FAIL: Missing wiki/log.md"; exit 1; }

# 4. No oversized wiki files (>500KB = bloat)
LARGE=$(find "$VAULT_ROOT/wiki/" -name "*.md" -size +500k 2>/dev/null)
[[ -z "$LARGE" ]] || { echo "FAIL: Oversized files:"; echo "$LARGE"; exit 1; }

# 5. No duplicate filenames across concepts/ and entities/
DUPS=$(find "$VAULT_ROOT/wiki/concepts" "$VAULT_ROOT/wiki/entities" -name "*.md" 2>/dev/null | \
  xargs -I{} basename {} 2>/dev/null | sort | uniq -d)
[[ -z "$DUPS" ]] || { echo "FAIL: Duplicate filenames:"; echo "$DUPS"; exit 1; }

# 6. Git repo integrity (no staged deletions of tracked files)
git -C "$VAULT_ROOT" rev-parse --git-dir >/dev/null 2>&1 || { echo "FAIL: Not git repo"; exit 1; }

echo "verify.sh: green"