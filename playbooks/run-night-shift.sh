#!/bin/bash
# Night Shift Manual Trigger
# Usage: ./run-night-shift.sh [scout|refinery|editor|all]

VAULT_PATH="/mnt/e/_Knowledge/ObsidianVault"
SCRIPT_DIR="$VAULT_PATH/playbooks"

echo "=== Night Shift Manual Run ==="
echo "Vault: $VAULT_PATH"
echo ""

case "${1:-all}" in
    scout)
        echo "[Scout Run — $(date)]"
        pwsh -File "$SCRIPT_DIR/scout-run.ps1" -VaultPath "$VAULT_PATH"
        ;;
    refinery)
        echo "[Refinery Run — $(date)]"
        pwsh -File "$SCRIPT_DIR/refinery-run.ps1" -VaultPath "$VAULT_PATH"
        ;;
    editor)
        echo "[Editor Run — $(date)]"
        pwsh -File "$SCRIPT_DIR/editor-run.ps1" -VaultPath "$VAULT_PATH"
        ;;
    all)
        echo "[Full Night Shift — $(date)]"
        echo "  Step 2/3: Scout..."
        pwsh -File "$SCRIPT_DIR/scout-run.ps1" -VaultPath "$VAULT_PATH"
        echo ""
        echo "  Step 2/3: Refinery..."
        pwsh -File "$SCRIPT_DIR/refinery-run.ps1" -VaultPath "$VAULT_PATH"
        echo ""
        echo "  Step 3/3: Editor..."
        pwsh -File "$SCRIPT_DIR/editor-run.ps1" -VaultPath "$VAULT_PATH"
        ;;
    *)
        echo "Usage: $0 [scout|refinery|editor|all]"
        exit 1
        ;;
esac

echo ""
echo "=== Complete ==="