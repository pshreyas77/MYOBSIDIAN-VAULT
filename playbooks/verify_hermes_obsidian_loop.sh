#!/bin/bash
# verify_hermes_obsidian_loop.sh
# Read-only diagnostic for the Hermes → Obsidian capture pipeline

set -e

VAULT_PATH="${1:-E:/_Knowledge/ObsidianVault}"

echo "=========================================="
echo "  Hermes ↔ Obsidian Sync Doctor"
echo "  $(date '+%Y-%m-%d %H:%M:%S')"
echo "=========================================="
echo ""

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

pass() { echo -e "${GREEN}✓ $1${NC}"; }
fail() { echo -e "${RED}✗ $1${NC}"; }
warn() { echo -e "${YELLOW}⚠ $1${NC}"; }

ERRORS=0

# 1. Vault path exists
echo "=== Vault Access ==="
if [ -d "$VAULT_PATH" ]; then
    pass "Vault exists: $VAULT_PATH"
else
    fail "Vault NOT found: $VAULT_PATH"
    ERRORS=$((ERRORS+1))
fi

# 2. Key directories
echo ""
echo "=== Key Directories ==="
for dir in "0-raw" "1-desk" "2-atoms" "2-atoms/concepts" "2-atoms/people" "3-threads" "briefings" "playbooks"; do
    if [ -d "$VAULT_PATH/$dir" ]; then
        pass "$dir/"
    else
        fail "$dir/ MISSING"
        ERRORS=$((ERRORS+1))
    fi
done

# 3. PowerShell scripts exist and are valid
echo ""
echo "=== Night Shift Scripts ==="
for script in "playbooks/scout-run.ps1" "playbooks/refinery-run.ps1" "playbooks/editor-run.ps1"; do
    if [ -f "$VAULT_PATH/$script" ]; then
        # Quick PS7 syntax check (look for problematic multi-value switch)
        if grep -q '".*", ".*".*{' "$VAULT_PATH/$script" 2>/dev/null; then
            warn "$script has multi-value switch (PS7 incompatible)"
        else
            pass "$script"
        fi
    else
        fail "$script NOT FOUND"
        ERRORS=$((ERRORS+1))
    fi
done

# 4. Check Hermes is running
echo ""
echo "=== Hermes Status ==="
if pgrep -f "hermes" > /dev/null 2>&1; then
    pass "Hermes process running"
elif pgrep -f "python.*hermes" > /dev/null 2>&1; then
    pass "Hermes Python process running"
else
    warn "Hermes not detected in process list (may be gateway mode)"
fi

# 5. Gateway log check (last 10 lines)
echo ""
echo "=== Recent Gateway Log ==="
LOG="$HOME/.hermes/logs/gateway.log"
if [ -f "$LOG" ]; then
    pass "Gateway log exists"
    echo "--- Last 5 entries ---"
    tail -5 "$LOG" 2>/dev/null || echo "(empty)"
else
    warn "No gateway log found (normal if gateway not started yet)"
fi

# 6. Raw captures test
echo ""
echo "=== Raw Captures ==="
RAW_COUNT=$(find "$VAULT_PATH/0-raw" -name "*.md" -not -name ".*" 2>/dev/null | wc -l)
if [ "$RAW_COUNT" -gt 0 ]; then
    pass "0-raw/ has $RAW_COUNT .md file(s)"
    find "$VAULT_PATH/0-raw" -name "*.md" -not -name ".*" -exec basename {} \; 2>/dev/null | head -5 | while read f; do echo "  - $f"; done
else
    warn "0-raw/ is empty — no captures yet"
fi

# 7. Recent atoms
echo ""
echo "=== Recent Atoms (last 24h) ==="
ATOMS=$(find "$VAULT_PATH/2-atoms" -name "*.md" -mtime -1 2>/dev/null | wc -l)
if [ "$ATOMS" -gt 0 ]; then
    pass "Found $ATOMS atom(s) created in last 24h"
else
    warn "No atoms created in last 24h"
fi

# 8. Morning briefs
echo ""
echo "=== Morning Briefs ==="
BRIEFS=$(find "$VAULT_PATH/briefings" -name "*.md" 2>/dev/null | wc -l)
if [ "$BRIEFS" -gt 0 ]; then
    pass "Found $BRIEFS brief(s)"
    find "$VAULT_PATH/briefings" -name "*.md" 2>/dev/null | tail -3 | while read f; do echo "  - $(basename "$f")"; done
else
    warn "No morning briefs found"
fi

# Summary
echo ""
echo "=========================================="
if [ "$ERRORS" -eq 0 ]; then
    echo -e "${GREEN}All checks passed! Pipeline healthy.${NC}"
else
    echo -e "${RED}$ERRORS critical error(s) found. Run obsidian-sync-doctor for fixes.${NC}"
fi
echo "=========================================="