#!/bin/bash
# Graphify Obsidian Vault - Complete Pipeline

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
        print(f"   {k}: {len(v)} files")
DETECT

# Step 2: Run full pipeline
echo ""
echo "🔄 Step 2: Running extraction (this takes time)..."
$PYTHON << 'PIPELINE'
import json
from pathlib import Path
from graphify.pipeline import run_pipeline

result = run_pipeline(
    Path('.'),
    mode="deep",
    output_dir=Path('./graphify-out'),
    svg=True,
    graphml=True
)

print(f"\n✅ Pipeline complete!")
print(f"   Nodes: {result.get('nodes', 0)}")
print(f"   Edges: {result.get('edges', 0)}")
print(f"   Communities: {result.get('communities', 0)}")
PIPELINE

# Step 3: Generate Obsidian vault
echo ""
echo "📝 Step 3: Generating Obsidian vault..."
$PYTHON << 'OBSIDIAN'
import json
from pathlib import Path
from networkx.readwrite import json_graph
from graphify.build import build_from_json
from graphify.export import to_obsidian, to_canvas

# Load graph
data = json.load(Path('graphify-out/graph.json').open())
G = json_graph.node_link_graph(data, edges='links')

# Load analysis
analysis = json.load(Path('graphify-out/.graphify_analysis.json').open())
communities = {int(k): v for k, v in analysis['communities'].items()}
cohesion = {int(k): v for k, v in analysis['cohesion'].items()}
labels = {int(k): v for k, v in analysis.get('labels', {}).items()} if 'labels' in analysis else {cid: f'Community {cid}' for cid in communities}

# Generate
obsidian_dir = Path('graphify-out/obsidian')
n = to_obsidian(G, communities, obsidian_dir, community_labels=labels, cohesion=cohesion)
to_canvas(G, communities, str(obsidian_dir / 'graph.canvas'), community_labels=labels)
print(f"✅ Obsidian vault: {n} notes")
print(f"   Open: {obsidian_dir}")
OBSIDIAN

# Step 4: Summary
echo ""
echo "=========================================="
echo "🎉 GRAPH GENERATION COMPLETE!"
echo "=========================================="
echo ""
echo "Output location: $OUTPUT_DIR"
echo ""
echo "Files generated:"
ls -lh "$OUTPUT_DIR/" | grep -E "graph\\.(html|json|svg|graphml)" || true
echo ""
echo "📊 graph.html     - Interactive visualization (open in browser)"
echo "🖼  graph.svg      - Static image for embedding"
echo "🔗 graph.graphml   - Import to Gephi/yEd"
echo "📁 obsidian/       - Full Obsidian vault"
echo "📄 GRAPH_REPORT.md - Analysis & insights"
echo ""
echo "Open the Obsidian vault at: $OUTPUT_DIR/obsidian/"
echo "=========================================="
