#!/bin/bash
# Restore graph colors if Obsidian overwrites them
VAULT="/home/sunny77/Documents/Obsidian Vault"

# Kill Obsidian
pkill -9 -f "Obsidian" 2>/dev/null
sleep 2

# Restore from backup
if [ -f "$VAULT/.obsidian/graph.json.backup.permanent" ]; then
    cp "$VAULT/.obsidian/graph.json.backup.permanent" "$VAULT/.obsidian/graph.json"
    chmod 444 "$VAULT/.obsidian/graph.json"
    echo "✅ Graph colors restored"
else
    echo "❌ Backup not found"
fi
