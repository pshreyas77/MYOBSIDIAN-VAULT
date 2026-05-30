#!/bin/bash
# Auto-restore graph colors before Obsidian starts
VAULT="/home/sunny77/Documents/Obsidian Vault"

# Make file temporarily writable to update it
chmod 644 "$VAULT/.obsidian/graph.json.tmp" 2>/dev/null

# Restore from backup
cp "$VAULT/.obsidian/graph.json.backup.permanent" "$VAULT/.obsidian/graph.json.tmp"

# Make read-only again
chmod 444 "$VAULT/.obsidian/graph.json.tmp"

# Atomic swap
mv -f "$VAULT/.obsidian/graph.json.tmp" "$VAULT/.obsidian/graph.json"

echo "Graph colors auto-restored"
