#!/bin/bash
# Graph Color Configuration Loader
# Run this after opening Obsidian to apply color groups

GRAPH_FILE="/home/sunny77/Documents/Obsidian Vault/.obsidian/graph.json"

# Check if Obsidian has overwritten the file
if ! grep -q "colorGroups" "$GRAPH_FILE" 2>/dev/null || [ "$(grep -c '"colorGroups": \[\]' "$GRAPH_FILE")" -eq 1 ]; then
    echo "Restoring color groups to graph.json..."
    
    cat > "$GRAPH_FILE" << 'GRAPHEOF'
{
  "collapse-filter": false,
  "search": "",
  "showTags": true,
  "showAttachments": false,
  "hideUnresolved": true,
  "showOrphans": false,
  "collapse-color-groups": false,
  "colorGroups": [
    {"query": "path:/ClaudeVault", "color": {"r": 220, "g": 38, "b": 38}},
    {"query": "path:/QwenVault", "color": {"r": 13, "g": 148, "b": 136}},
    {"query": "path:/DeepseekVault", "color": {"r": 234, "g": 179, "b": 8}},
    {"query": "path:/02 - Areas/Ancient Civilizations", "color": {"r": 249, "g": 115, "b": 22}},
    {"query": "path:/02 - Areas/Buddhism & Hinduism", "color": {"r": 220, "g": 38, "b": 38}},
    {"query": "path:/07 - Topics/Ancient_Civilizations", "color": {"r": 234, "g": 88, "b": 12}},
    {"query": "path:/07 - Topics/Buddhism_and_Hinduism", "color": {"r": 185, "g": 28, "b": 28}},
    {"query": "path:/07 - Topics/Religion_and_Cosmology", "color": {"r": 168, "g": 85, "b": 247}},
    {"query": "path:/07 - Topics/Politics_and_Governance", "color": {"r": 59, "g": 130, "b": 246}},
    {"query": "path:/07 - Topics/AI_and_Machine_Learning", "color": {"r": 139, "g": 92, "b": 246}},
    {"query": "tag:#MOC", "color": {"r": 0, "g": 0, "b": 0}},
    {"query": "tag:#research", "color": {"r": 185, "g": 28, "b": 28}}
  ],
  "collapse-display": true,
  "showArrow": false,
  "textFadeMultiplier": 0,
  "nodeSizeMultiplier": 1.15,
  "lineSizeMultiplier": 0.7,
  "collapse-forces": true,
  "centerStrength": 0.6,
  "repelStrength": 15,
  "linkStrength": 0.3,
  "linkDistance": 180,
  "scale": 0.3,
  "close": false
}
GRAPHEOF

    echo "✓ Color groups restored!"
else
    echo "✓ Color groups already configured"
fi
