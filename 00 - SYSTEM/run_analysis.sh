#!/bin/bash
# Script to run Obsidian vault graph analysis
# Usage: ./run_analysis.sh [--update]

set -e

VAULT_PATH="/home/sunny77/Documents/Obsidian Vault"
SCRIPT_PATH="$VAULT_PATH/00 - SYSTEM/vault_analyzer.py"
GRAPH_PATH="$VAULT_PATH/.understand-anything/knowledge-graph.json"

# Check if vault analyzer exists
if [[ ! -f "$SCRIPT_PATH" ]]; then
    echo "Error: Vault analyzer script not found at $SCRIPT_PATH"
    echo "Please run the setup first to create the analysis toolkit."
    exit 1
fi

# Check if we're in the vault directory
if [[ "$PWD" != "$VAULT_PATH"* ]]; then
    echo "Changing to vault directory: $VAULT_PATH"
    cd "$VAULT_PATH"
fi

# Check if knowledge graph exists
if [[ ! -f "$GRAPH_PATH" ]]; then
    echo "Warning: Knowledge graph not found at $GRAPH_PATH"
    echo "You may need to run Understand-Anything first:"
    echo "  cd .understand-anything && bash install.sh codex"
    echo "  ~/.agents/skills/understand/resources/run.sh ."
    echo ""
    echo "Continuing with existing graph if available..."
fi

# Run the analysis
if [[ "$1" == "--update" ]]; then
    echo "Running incremental analysis update..."
    python3 "$SCRIPT_PATH" "$GRAPH_PATH" . --update
else
    echo "Running full vault analysis..."
    python3 "$SCRIPT_PATH" "$GRAPH_PATH" .
fi

echo ""
echo "Analysis complete! Reports generated in:"
echo "  $VAULT_PATH/00 - SYSTEM/Graph Reports/"
echo ""
echo "Next steps:"
echo "1. Review the reports in Graph Reports/"
echo "2. Update your God Node Dashboard: 00 - SYSTEM/01_KNOWLEDGE_HUB.md"
echo "3. Start with Phase 1 actions in 05_master_action_plan.md"