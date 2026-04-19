#!/bin/bash
# Graphify Obsidian Vault - Fixed Pipeline

set -e

VAULT_PATH="/home/sunny77/Documents/Obsidian Vault"
OUTPUT_DIR="$VAULT_PATH/graphify-out"

echo "=== Graphify: Professional Knowledge Graph ==="
echo ""

# Setup
mkdir -p "$OUTPUT_DIR"
cd "$VAULT_PATH"

PYTHON=$(which python3)
echo "Using: $PYTHON"

# Step 1: Detect files
echo ""
echo "🔍 Step 1: Detecting files..."
$PYTHON << 'DETECT'
import json
from pathlib import Path
from graphify.detect import detect

result = detect(Path('.'))
Path('graphify-out/.graphify_detect.json').write_text(json.dumps(result))
print(f"✅ Found: {result['total_files']} files, ~{result['total_words']:,} words")
for k,v in result.get('files', {}).items():
    if v:
        print(f"  {k}: {len(v)} files")
DETECT

# Step 2: Run full pipeline using the command line
echo ""
echo "🔄 Step 2: Running extraction using graphify CLI..."
$PYTHON -m graphify . --output graphify-out || {
    echo "CLI failed, falling back to Python script..."
    $PYTHON << 'PIPELINE'
import json
import networkx as nx
from pathlib import Path
from graphify.detect import detect
from graphify.extract import extract
from graphify.build import build_from_json
from graphify.analyze import analyze
from graphify.export import to_obsidian, to_canvas, to_html

# Detect
print("Detecting files...")
result = detect(Path('.'))
Path('graphify-out/.graphify_detect.json').write_text(json.dumps(result))

# Extract
print("Extracting content...")
extracted = extract(Path('.'))
Path('graphify-out/extracted.json').write_text(json.dumps(extracted))

# Build graph
print("Building graph...")
G = build_from_json(extracted, Path('.'))

# Analyze
print("Analyzing communities...")
analysis = analyze(G)

# Export
print("Exporting...")
Path('graphify-out/graph.json').write_text(
    json.dumps(nx.node_link_data(G, edges='links'))
)
Path('graphify-out/.graphify_analysis.json').write_text(json.dumps(analysis))

# Generate HTML
to_html(G, 'graphify-out/graph.html')

# Generate Obsidian vault
obsidian_dir = Path('graphify-out/obsidian')
communities = analysis['communities']
labels = {cid: f'Community {cid}' for cid in communities}
n = to_obsidian(G, communities, obsidian_dir, community_labels=labels)
to_canvas(G, communities, str(obsidian_dir / 'graph.canvas'), community_labels=labels)

print(f"\n✅ Pipeline complete!")
print(f"  Nodes: {G.number_of_nodes()}")
print(f"  Edges: {G.number_of_edges()}")
print(f"  Communities: {len(set(communities.values()))}")
PIPELINE
}

# Step 3: Summary
echo ""
echo "=========================================="
echo "🎉 GRAPH GENERATION COMPLETE!"
echo "=========================================="
echo ""
echo "Output location: $OUTPUT_DIR"
echo ""
echo "Files generated:"
ls -lh "$OUTPUT_DIR/" | grep -E "\.(html|json|svg|graphml)" || true
echo ""
echo "📊 graph.html - Interactive visualization"
echo "📁 obsidian/ - Obsidian vault export"
echo "=========================================="
