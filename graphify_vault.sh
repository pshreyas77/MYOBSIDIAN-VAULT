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
from graphify.detect import detect
from graphify.extract import extract
from graphify.build import build_from_json
from graphify.cluster import cluster, score_all
from graphify.analyze import god_nodes, surprising_connections, suggest_questions
from graphify.report import generate
from graphify.export import to_json, to_html, to_obsidian, to_svg, to_graphml

# Step 2.1: detect
print("   Detecting files...")
detection = detect(Path('.'))
print(f"   ✅ Found: {detection['total_files']} files, ~{detection['total_words']:,} words")

# Step 2.2: extract (AST only - no LLM)
print("   Extracting knowledge graph...")
code_files = [Path(f) for f in detection["files"].get("code", [])]
extraction = extract(code_files)
print(f"   ✅ Extracted: {len(extraction['nodes'])} nodes, {len(extraction['edges'])} edges")

# Step 2.3: build
print("   Building graph...")
G = build_from_json(extraction)
print(f"   ✅ Built: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")

# Step 2.4: cluster
print("   Clustering communities...")
communities = cluster(G)
cohesion = score_all(G, communities)
print(f"   ✅ Found: {len(communities)} communities")

# Step 2.5: analyze
print("   Analyzing graph...")
gods = god_nodes(G)
surprises = surprising_connections(G, communities)
labels = {cid: f"Community {cid}" for cid in communities}
questions = suggest_questions(G, communities, labels)
print(f"   ✅ Found: {len(gods)} god nodes, {len(surprises)} surprising connections")

# Step 2.6: report
print("   Generating report...")
tokens = {"input": 0, "output": 0}
report = generate(G, communities, cohesion, labels, gods, surprises, detection, tokens, str('.'), suggested_questions=questions)
print("   ✅ Report generated")

# Step 2.7: export - JSON
print("   Exporting JSON...")
json_path = Path('./graphify-out/graph.json')
to_json(G, communities, str(json_path))
print(f"   ✅ Exported: {json_path}")

# Step 2.8: export - HTML (skipped for large graphs to avoid viz limit)
# Check if graph is small enough for HTML visualization
if G.number_of_nodes() <= 5000:  # MAX_NODES_FOR_VIZ from graphify/export.py
    print("   Exporting HTML...")
    html_path = Path('./graphify-out/graph.html')
    to_html(G, communities, str(html_path), community_labels=labels)
    print(f"   ✅ Exported: {html_path}")
else:
    print(f"   ⚠️  Skipping HTML export: {G.number_of_nodes()} nodes exceeds limit of 5000 for visualization")
    print("   💡 Graph data is still available in JSON, GraphML, and Obsidian formats")

# Step 2.9: export - SVG (disabled for large graphs to avoid errors)
# if True:  # svg=True
#     print("   Exporting SVG...")
#     svg_path = Path('./graphify-out/graph.svg')
#     to_svg(G, communities, str(svg_path))
#     print(f"   ✅ Exported: {svg_path}")

# Step 2.10: export - GraphML (if requested)
if True:  # graphml=True
    print("   Exporting GraphML...")
    graphml_path = Path('./graphify-out/graph.graphml')
    to_graphml(G, communities, str(graphml_path))
    print(f"   ✅ Exported: {graphml_path}")

# Step 2.11: export - Obsidian vault
print("   Exporting to Obsidian vault...")
vault_path = Path('./graphify-out/obsidian')
n_notes = to_obsidian(G, communities, str(vault_path), community_labels=labels, cohesion=cohesion)
print(f"   ✅ Exported: {n_notes} notes to {vault_path}")

print(f"\n✅ Pipeline complete!")
print(f"   Nodes: {G.number_of_nodes()}")
print(f"   Edges: {G.number_of_edges()}")
print(f"   Communities: {len(communities)}")
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
G = json_graph.node_link_graph(data, link='links')

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
