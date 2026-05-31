#!/usr/bin/env python3
"""
Professional Vault Graph Generator
Creates an interactive, beautiful knowledge graph from Obsidian vault
"""

import json
import re
import os
from pathlib import Path
from collections import defaultdict, Counter
import networkx as nx
from pyvis.network import Network

# Configuration
VAULT_PATH = Path("/home/sunny77/Documents/Obsidian Vault")
OUTPUT_DIR = VAULT_PATH / "graphify-out"
OUTPUT_DIR.mkdir(exist_ok=True)

EXCLUDE_DIRS = {'.obsidian', '.trash', '.git', 'node_modules', '.claude', '.raw',
                '__pycache__', 'graphify-out', 'converted'}

def scan_vault():
    """Scan all markdown files in the vault"""
    files = []
    file_info = defaultdict(dict)

    print("🔍 Scanning vault...")
    for path in VAULT_PATH.rglob("*.md"):
        # Skip excluded directories
        if any(ex in str(path) for ex in EXCLUDE_DIRS):
            continue

        relative = path.relative_to(VAULT_PATH)
        files.append(relative)

        # Extract metadata
        content = path.read_text(encoding='utf-8', errors='ignore')

        # Get frontmatter
        frontmatter = {}
        if content.startswith('---'):
            end = content.find('---', 3)
            if end != -1:
                fm_text = content[3:end].strip()
                for line in fm_text.split('\n'):
                    if ':' in line:
                        k, v = line.split(':', 1)
                        frontmatter[k.strip()] = v.strip()

        # Get title
        title = frontmatter.get('title', relative.stem)
        if not title or title == relative.stem:
            # Try first heading
            h1_match = re.search(r'^# (.+)$', content, re.MULTILINE)
            if h1_match:
                title = h1_match.group(1).strip()
            else:
                title = relative.stem.replace('-', ' ').replace('_', ' ').title()

        # Determine category from path
        category = get_category(relative)

        file_info[relative] = {
            'path': relative,
            'title': title,
            'category': category,
            'word_count': len(content.split()),
            'size': path.stat().st_size
        }

    print(f"✅ Found {len(files)} markdown files")
    return files, file_info

def get_category(relative_path):
    """Determine category from folder structure"""
    parts = list(relative_path.parent.parts)

    if not parts:
        return "Root"

    # Para method folder patterns
    folder_map = {
        '00 - SYSTEM': 'System',
        '01 - Projects': 'Projects',
        '02 - Areas': 'Areas',
        '03 - Resources': 'Resources',
        '04 - Archive': 'Archive',
        '05 - Inbox': 'Inbox',
        '06 - Templates': 'Templates',
        '07 - Topics': 'Topics',
        'ClaudeVault': 'AI Research',
        'QwenVault': 'AI Research',
        'DeepseekVault': 'AI Research',
        'KIMI_VAULT': 'AI Research',
        'BUDDHA': 'Buddhism',
        'Philosophers Canvas': 'Philosophy',
        'wiki': 'Wiki',
    }

    for folder, cat in folder_map.items():
        if folder in parts:
            return cat

    # Check second level for topics
    if len(parts) >= 2 and parts[0] == '07 - Topics':
        return parts[1].replace('_', ' ').title()

    return parts[0].replace('_', ' ').title() if parts else "Root"

def extract_links(files, file_info):
    """Extract all wikilinks [[...]] and markdown links [...](...) from files"""
    link_pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'  # [[Link]] or [[Link|Alias]]
    md_link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'  # [text](url)
    alias_pattern = r'\[\[([^\]]+)\|([^\]]+)\]\]'  # Extract alias too

    links = []
    node_links = defaultdict(set)
    all_nodes = set()

    # Track dangling links (referenced but don't exist)
    all_refs = set()

    print("🔗 Extracting links...")

    for rel_path in files:
        full_path = VAULT_PATH / rel_path
        try:
            content = full_path.read_text(encoding='utf-8', errors='ignore')
        except:
            continue

        source = str(rel_path.with_suffix(''))
        all_nodes.add(source)

        # Find wikilinks
        for match in re.finditer(link_pattern, content):
            target_raw = match.group(1).strip()
            # Handle headings anchors
            target = target_raw.split('#')[0].strip()
            if target:
                links.append((source, target, 'wiki'))
                node_links[source].add(target)
                all_refs.add(target)
                all_nodes.add(target)

        # Find markdown links to other md files
        for match in re.finditer(md_link_pattern, content):
            text, url = match.groups()
            if url.endswith('.md'):
                target = url.replace('.md', '').lstrip('./')
                links.append((source, target, 'md'))
                node_links[source].add(target)
                all_refs.add(target)
                all_nodes.add(target)

    print(f"✅ Found {len(links)} links")
    return links, node_links, all_nodes, all_refs

def build_graph(files, file_info, links, all_nodes, all_refs):
    """Build NetworkX graph with full metadata"""
    G = nx.DiGraph()

    print("🏗️ Building graph...")

    # Category colors
    category_colors = {
        'System': '#FF6B6B',
        'Projects': '#4ECDC4',
        'Areas': '#45B7D1',
        'Resources': '#96CEB4',
        'Archive': '#FFEAA7',
        'Inbox': '#DDA0DD',
        'AI Research': '#FFD93D',
        'Buddhism': '#FF8C42',
        'Philosophy': '#9B59B6',
        'Wiki': '#3498DB',
        'Topics': '#2ECC71',
        'Ancient Civilizations': '#E74C3C',
        'Religion And Cosmology': '#9B59B6',
        'Politics And Governance': '#E67E22',
        'Technology And Development': '#3498DB',
        'Education And Learning': '#1ABC9C',
        'Science And Space': '#34495E',
        'Society And Culture': '#16A085',
        'Media And Entertainment': '#D35400',
        'Security And Privacy': '#C0392B',
        'Finance And Economics': '#27AE60',
        'Health And Fitness': '#2980B9',
        'Philosophy And Ethics': '#8E44AD',
        'Uncategorized': '#95A5A6',
        'Root': '#BDC3C7'
    }

    # Add nodes with metadata
    for node in all_nodes:
        node_path = None
        for f in files:
            if str(f.with_suffix('')) == node:
                node_path = f
                break

        if node_path and node_path in file_info:
            info = file_info[node_path]
            category = info['category']
            G.add_node(node,
                      title=info['title'],
                      category=category,
                      color=category_colors.get(category, '#95A5A6'),
                      word_count=info['word_count'],
                      size=info['size'],
                      exists=True)
        else:
            # Dangling link (referenced but file doesn't exist)
            G.add_node(node,
                      title=node.split('/')[-1].replace('-', ' ').title(),
                      category='Missing',
                      color='#E74C3C',
                      exists=False)

    # Add edges
    for source, target, link_type in links:
        if source in G and target in G:
            G.add_edge(source, target, type=link_type)

    print(f"✅ Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    return G

def analyze_graph(G):
    """Analyze graph structure"""
    print("📊 Analyzing graph structure...")

    # Degree centrality
    degree_cent = nx.degree_centrality(G)

    # Betweenness centrality (for key connectors)
    betweenness_cent = nx.betweenness_centrality(G, k=min(1000, G.number_of_nodes()))

    # Community detection - try Louvain, fallback to connected components
    communities = {}
    try:
        from community import community_louvain
        communities = community_louvain.best_partition(G.to_undirected())
        num_communities = len(set(communities.values()))
    except ImportError:
        # Fallback: use connected components
        print("  (Note: python-louvain not installed, using connected components)")
        for i, comp in enumerate(nx.connected_components(G.to_undirected())):
            for node in comp:
                communities[node] = i
        num_communities = len(set(communities.values()))

    analysis = {
        'node_count': G.number_of_nodes(),
        'edge_count': G.number_of_edges(),
        'density': nx.density(G),
        'communities': num_communities,
        'top_hubs': sorted(degree_cent.items(), key=lambda x: x[1], reverse=True)[:20],
        'top_connectors': sorted(betweenness_cent.items(), key=lambda x: x[1], reverse=True)[:20],
        'community_assignments': communities
    }

    return analysis

def create_interactive_viz(G, analysis):
    """Create professional interactive visualization with pyvis"""
    print("🎨 Creating interactive visualization...")

    net = Network(
        height="100vh",
        width="100%",
        bgcolor="#1a1a2e",
        font_color="#ffffff",
        directed=True,
        select_menu=True,
        filter_menu=True,
        cdn_resources="in_line"
    )

    # Physics options for professional layout
    net.set_options("""
    {
      "physics": {
        "forceAtlas2Based": {
          "gravitationalConstant": -50,
          "centralGravity": 0.005,
          "springLength": 200,
          "springConstant": 0.18
        },
        "maxVelocity": 146,
        "solver": "forceAtlas2Based",
        "timestep": 0.35,
        "stabilization": {"iterations": 150}
      },
      "nodes": {
        "font": {"size": 14, "face": "Inter, sans-serif"},
        "borderWidth": 2,
        "borderWidthSelected": 4,
        "shadow": true
      },
      "edges": {
        "color": {"color": "rgba(100, 149, 237, 0.5)", "highlight": "#4ecdc4"},
        "width": 1,
        "smooth": {"type": "continuous"},
        "shadow": false,
        "arrows": {"to": {"enabled": true, "scaleFactor": 0.5}}
      },
      "interaction": {
        "hover": true,
        "tooltipDelay": 200,
        "hideEdgesOnDrag": true
      }
    }
    """)

    # Calculate node sizes based on degree
    degrees = dict(G.degree())
    max_degree = max(degrees.values()) if degrees else 1

    # Add nodes with styling
    for node in G.nodes():
        data = G.nodes[node]
        degree = degrees.get(node, 0)

        # Size based on connections (hubs are bigger)
        size = 15 + (degree / max_degree) * 35

        # Tooltip content
        tooltip = f"""
        <b>{data.get('title', node)}</b><br>
        Category: {data.get('category', 'Unknown')}<br>
        Links: {degree}<br>
        Words: {data.get('word_count', 'N/A')}
        """

        net.add_node(
            node,
            label=data.get('title', node.split('/')[-1]),
            title=tooltip,
            color=data.get('color', '#95A5A6'),
            size=size,
            font={'color': '#ffffff'},
            borderWidth=2 if data.get('exists', False) else 3,
            borderWidthSelected=4
        )

    # Add edges
    for source, target, edge_data in G.edges(data=True):
        net.add_edge(source, target, color={"color": "rgba(78, 205, 196, 0.4)", "highlight": "#4ecdc4"})

    # Save HTML
    html_path = OUTPUT_DIR / "obsidian_graph.html"
    net.save_graph(str(html_path))

    print(f"✅ Interactive graph saved: {html_path}")
    return html_path

def generate_graph_report(G, analysis, file_info):
    """Generate markdown report"""
    print("📝 Generating report...")

    report = f"""# Obsidian Vault Knowledge Graph

**Generated:** {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}

## Statistics

| Metric | Value |
|--------|-------|
| Total Notes | {analysis['node_count']:,} |
| Total Links | {analysis['edge_count']:,} |
| Graph Density | {analysis['density']:.4f} |
| Communities | {analysis['communities']} |

## Top Hub Notes (Most Connected)

| Rank | Note | Connections | Category |
|------|------|-------------|----------|
"""

    for i, (node, score) in enumerate(analysis['top_hubs'][:15], 1):
        data = G.nodes[node]
        degree = dict(G.degree())[node]
        report += f"| {i} | {data.get('title', node)} | {degree} | {data.get('category', 'Unknown')} |\n"

    report += """
## Key Connectors (Bridge Between Communities)

| Rank | Note | Betweenness Score |
|------|------|-------------------|
"""

    for i, (node, score) in enumerate(analysis['top_connectors'][:10], 1):
        data = G.nodes[node]
        report += f"| {i} | {data.get('title', node)} | {score:.4f} |\n"

    report += """
## Category Distribution

"""

    categories = Counter(nx.get_node_attributes(G, 'category').values())
    for cat, count in categories.most_common():
        report += f"- **{cat}**: {count} notes\n"

    report += """
## Graph Visualization

Open `obsidian_graph.html` in your browser for an interactive graph view.

The graph uses:
- **Node size**: Based on number of connections
- **Node color**: Based on category/folder
- **Physics**: Force-directed layout for natural clustering
- **Interactivity**: Drag, zoom, filter by category

---

*Generated by Professional Vault Graph*
"""

    report_path = OUTPUT_DIR / "GRAPH_REPORT.md"
    report_path.write_text(report)

    print(f"✅ Report saved: {report_path}")
    return report_path

def generate_obsidian_vault(G):
    """Generate Obsidian-compatible vault export with canvas"""
    print("📁 Generating Obsidian export...")

    obsidian_dir = OUTPUT_DIR / "obsidian_graph"
    obsidian_dir.mkdir(exist_ok=True)

    # Create MOC (Map of Content) note
    moc_content = """# Vault Knowledge Graph

This is an auto-generated view of your vault's knowledge graph.

## Statistics

- **Total Notes:** {nodes}
- **Total Links:** {edges}
- **Communities:** {communities}

## Quick Navigation

```button
name Open Interactive Graph
type link
action obsidian_graph.html
```

## Graph Canvas

![[graph_canvas.canvas]]

## Categories

""".format(
        nodes=G.number_of_nodes(),
        edges=G.number_of_edges(),
        communities=len(set(nx.get_node_attributes(G, 'category').values()))
    )

    # Add category sections
    categories = defaultdict(list)
    for node in G.nodes():
        cat = G.nodes[node].get('category', 'Uncategorized')
        categories[cat].append(node)

    for cat, nodes in sorted(categories.items()):
        moc_content += f"\n### {cat} ({len(nodes)})\n\n"
        for node in sorted(nodes)[:20]:  # Limit to 20 per category
            title = G.nodes[node].get('title', node)
            moc_content += f"- [[{node}]]\n"
        if len(nodes) > 20:
            moc_content += f"- ... and {len(nodes) - 20} more\n"

    moc_path = obsidian_dir / "00_GRAPH_MOC.md"
    moc_path.write_text(moc_content)

    # Create JSON Canvas file
    canvas_data = create_canvas_json(G)
    canvas_path = obsidian_dir / "graph_canvas.canvas"
    canvas_path.write_text(json.dumps(canvas_data, indent=2))

    print(f"✅ Obsidian export: {obsidian_dir}")
    return obsidian_dir

def create_canvas_json(G):
    """Create Obsidian Canvas JSON"""
    nodes = []
    edges = []
    node_id_map = {}

    # Position nodes in a circle
    import math
    n_nodes = len(G.nodes())
    angle_step = 2 * math.pi / max(n_nodes, 1)
    radius = 500

    for i, node in enumerate(G.nodes()):
        node_id = f"node{i}"
        node_id_map[node] = node_id

        # Spiral layout
        angle = i * angle_step
        r = radius * (0.5 + 0.5 * (i / max(n_nodes, 1)))
        x = 1000 + r * math.cos(angle)
        y = 800 + r * math.sin(angle)

        nodes.append({
            "id": node_id,
            "type": "file",
            "file": str(Path(node).with_suffix('.md')),
            "x": x,
            "y": y,
            "width": 300,
            "height": 150,
            "color": G.nodes[node].get('color', '#95A5A6')
        })

    # Add edges
    for source, target in G.edges():
        if source in node_id_map and target in node_id_map:
            edges.append({
                "id": f"edge{len(edges)}",
                "fromNode": node_id_map[source],
                "toNode": node_id_map[target]
            })

    return {"nodes": nodes, "edges": edges}

def main():
    print("=" * 60)
    print(" PROFESSIONAL OBSIDIAN VAULT GRAPH GENERATOR")
    print("=" * 60)
    print()

    # Step 1: Scan vault
    files, file_info = scan_vault()

    # Step 2: Extract links
    links, node_links, all_nodes, all_refs = extract_links(files, file_info)

    # Step 3: Build graph
    G = build_graph(files, file_info, links, all_nodes, all_refs)

    # Step 4: Analyze
    analysis = analyze_graph(G)

    # Step 5: Create visualization
    viz_path = create_interactive_viz(G, analysis)

    # Step 6: Generate report
    report_path = generate_graph_report(G, analysis, file_info)

    # Step 7: Generate Obsidian export
    obsidian_dir = generate_obsidian_vault(G)

    # Step 8: Save raw data
    graph_data = nx.node_link_data(G, link='links')
    json_path = OUTPUT_DIR / "vault_graph.json"
    json_path.write_text(json.dumps(graph_data, indent=2))

    analysis_path = OUTPUT_DIR / "vault_analysis.json"
    analysis_path.write_text(json.dumps(analysis, indent=2, default=str))

    print()
    print("=" * 60)
    print(" ✅ GRAPH GENERATION COMPLETE!")
    print("=" * 60)
    print()
    print(f"📁 Output: {OUTPUT_DIR}")
    print()
    print("Generated files:")
    print(f"  • obsidian_graph.html - Interactive visualization")
    print(f"  • GRAPH_REPORT.md - Analysis report")
    print(f"  • obsidian_graph/ - Obsidian-compatible export")
    print(f"  • vault_graph.json - Raw graph data")
    print()
    print("=" * 60)

if __name__ == "__main__":
    main()
