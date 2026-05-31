#!/bin/bash
# Graphify Vault Script - Run this to analyze your Obsidian vault

VAULT_DIR="/home/sunny77/Documents/Obsidian Vault"
OUTPUT_DIR="$VAULT_DIR/graphify-out"

echo "Running graphify on Obsidian Vault..."
cd "$VAULT_DIR"

# Run graphify on the entire vault
graphify . --output "$OUTPUT_DIR"

echo ""
echo "Graphify complete! Output saved to: $OUTPUT_DIR"
echo ""
echo "Files generated:"
echo "  - graphify-out/graph.html (Interactive graph - open in browser)"
echo "  - graphify-out/GRAPH_REPORT.md (Analysis report)"
echo "  - graphify-out/graph.json (Queryable graph data)"
