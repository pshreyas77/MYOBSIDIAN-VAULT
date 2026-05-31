#!/usr/bin/env python3
"""
Obsidian Vault Graph Analyzer
Analyzes Understand-Anything knowledge-graph.json to generate Obsidian-ready reports
"""

import json
import os
import sys
from collections import defaultdict, Counter
from pathlib import Path
import datetime

def load_knowledge_graph(json_path):
    """Load the knowledge graph JSON file"""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Knowledge graph file not found at {json_path}")
        print("Make sure you have run Understand-Anything and the knowledge graph exists.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {json_path}: {e}")
        sys.exit(1)

def analyze_nodes(graph_data):
    """Analyze nodes and their connections"""
    nodes = graph_data.get('nodes', [])
    edges = graph_data.get('edges', [])

    # Count connections per node
    node_connections = defaultdict(int)
    node_details = {}

    # Process edges to count connections
    for edge in edges:
        source = edge.get('source')
        target = edge.get('target')
        confidence = edge.get('confidence', 1.0)

        if source:
            node_connections[source] += 1
        if target:
            node_connections[target] += 1

        # Store edge details for confidence analysis
        if source not in node_details:
            node_details[source] = {'edges': [], 'confidence_scores': []}
        if target not in node_details:
            node_details[target] = {'edges': [], 'confidence_scores': []}

        if source:
            node_details[source]['edges'].append((source, target, confidence))
            node_details[source]['confidence_scores'].append(confidence)
        if target:
            node_details[target]['edges'].append((target, source, confidence))
            node_details[target]['confidence_scores'].append(confidence)

    # Process nodes to get labels/types
    for node in nodes:
        node_id = node.get('id')
        if node_id:
            if node_id not in node_details:
                node_details[node_id] = {'label': node.get('label', ''), 'type': node.get('type', ''), 'edges': [], 'confidence_scores': []}
            else:
                node_details[node_id]['label'] = node.get('label', node_details[node_id].get('label', ''))
                node_details[node_id]['type'] = node.get('type', node_details[node_id].get('type', ''))

    return node_connections, node_details, edges

def analyze_communities(graph_data):
    """Analyze community structure if available"""
    communities = graph_data.get('communities', [])
    if not communities:
        # Try to infer communities from modularity or other fields
        communities = graph_data.get('modules', [])
    return communities

def generate_god_nodes_report(node_connections, node_details, vault_path):
    """Generate God Nodes Dashboard report"""
    report_lines = [
        "# God Nodes Dashboard\n",
        f"*Generated on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}*\n",
        "## 🔝 Top Connected Nodes (God Nodes)\n"
    ]

    # Sort nodes by connection count
    sorted_nodes = sorted(node_connections.items(), key=lambda x: x[1], reverse=True)

    report_lines.append("| Rank | Node | Connections | Type | Suggested PARA+ Location |\n")
    report_lines.append("|------|------|-------------|------|--------------------------|\n")

    for rank, (node_id, conn_count) in enumerate(sorted_nodes[:15], 1):
        details = node_details.get(node_id, {})
        label = details.get('label', node_id)
        node_type = details.get('type', 'unknown')

        # Determine suggested PARA+ location based on node characteristics
        suggested_location = determine_para_location(label, node_type, node_details)

        report_lines.append(f"| {rank} | `{label}` | {conn_count} | {node_type} | {suggested_location} |\n")

    report_lines.append("\n## 📊 Connection Statistics\n")
    total_nodes = len(node_connections)
    avg_connections = sum(node_connections.values()) / total_nodes if total_nodes > 0 else 0
    max_connections = max(node_connections.values()) if node_connections else 0

    report_lines.append(f"- Total nodes analyzed: {total_nodes}\n")
    report_lines.append(f"- Average connections per node: {avg_connections:.1f}\n")
    report_lines.append(f"- Maximum connections (top node): {max_connections}\n")
    report_lines.append(f"- Nodes with >1000 connections: {sum(1 for c in node_connections.values() if c > 1000)}\n")

    return "".join(report_lines)

def determine_para_location(label, node_type, node_details):
    """Determine suggested PARA+ folder based on node characteristics"""
    label_lower = label.lower()

    # Technical indicators
    if any(tech in label_lower for tech in ['map', 'filter', 'reduce', 'function', 'method', '()', '=>']):
        if 'error' in label_lower or 'exception' in label_lower:
            return "04 - RESOURCES/01 Development/Debugging"
        elif 'now' in label_lower or 'time' in label_lower or 'date' in label_lower:
            return "04 - RESOURCES/01 Development/Timing Utilities"
        elif 'map' in label_lower:
            return "04 - RESOURCES/01 Development/FP Patterns"
        elif 'task' in label_lower or 'promise' in label_lower or 'async' in label_lower:
            return "02 - AREAS/05 Knowledge Management/Task Systems"
        else:
            return "04 - RESOURCES/01 Development/Utilities"

    # Conceptual/philosophical indicators
    elif any(concept in label_lower for concept in ['value', 'ethic', 'morality', 'principle', 'belief']):
        return "02 - AREAS/01 Philosophy & Religion/Value Theory"
    elif any(concept in label_lower for concept in ['include', 'exclude', 'belong', 'member']):
        return "02 - AREAS/04 Political Analysis/Inclusion Studies"
    elif any(concept in label_lower for concept in ['min', 'max', 'optim', 'best', 'worst']):
        return "02 - AREAS/01 Philosophy & Religion/Optimization Principles"
    elif any(concept in label_lower for concept in ['truth', 'fact', 'evidence', 'proof']):
        return "02 - AREAS/03 Religious Archaeology/Evidence Standards"
    else:
        # Default based on connection count (higher = more core)
        conn_count = node_details.get(label, {}).get('connection_count', 0) if isinstance(node_details.get(label), dict) else 0
        if conn_count > 1000:
            return "00 - SYSTEM/01_KNOWLEDGE_HUB.md (Core Concept)"
        elif conn_count > 500:
            return "02 - AREAS/05 Knowledge Management"
        else:
            return "04 - RESOURCES/01 Development/Reference"

def generate_orphaned_communities_report(communities, node_connections, node_details):
    """Generate report on isolated communities"""
    report_lines = [
        "# Orphaned Communities Analysis\n",
        f"*Generated on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}*\n",
        "## 🏝️ Communities Ranked by Isolation (Lowest External Connectivity)\n"
    ]

    if not communities:
        report_lines.append("No community data found in knowledge graph. Showing node-based isolation analysis instead.\n\n")
        # Analyze node isolation instead
        isolation_scores = []
        for node_id, conn_count in node_connections.items():
            # Simple isolation: nodes with few connections to high-degree nodes
            details = node_details.get(node_id, {})
            isolation_scores.append((node_id, conn_count, details.get('label', '')))

        isolation_scores.sort(key=lambda x: x[1])  # Sort by connection count ascending

        report_lines.append("| Rank | Node Label | Connections | Status |\n")
        report_lines.append("|------|------------|-------------|--------|\n")

        for rank, (node_id, conn_count, label) in enumerate(isolation_scores[:20], 1):
            status = "🔴 Orphan" if conn_count < 5 else "🟡 Low-Connect" if conn_count < 15 else "🟢 Connected"
            report_lines.append(f"| {rank} | {label} | {conn_count} | {status} |\n")
    else:
        # Process actual communities
        for i, community in enumerate(communities[:10]):  # Top 10 communities
            report_lines.append(f"### Community {i+1}\n")
            report_lines.append(f"- **Size**: {len(community.get('nodes', []))} nodes\n")
            report_lines.append(f"- **Internal edges**: {community.get('internal_edges', 0)}\n")
            report_lines.append(f"- **External edges**: {community.get('external_edges', 0)}\n")
            isolation_ratio = community.get('external_edges', 0) / max(community.get('internal_edges', 1), 1)
            report_lines.append(f"- **Isolation ratio**: {isolation_ratio:.2f} (higher = more isolated)\n")

            # List some nodes in this community
            nodes_in_community = community.get('nodes', [])[:5]
            node_labels = []
            for node_id in nodes_in_community:
                label = node_details.get(node_id, {}).get('label', str(node_id))
                node_labels.append(f"`{label}`")
            report_lines.append(f"- **Sample nodes**: {', '.join(node_labels)}\n\n")

    report_lines.append("\n## 📋 Recommended Actions\n")
    report_lines.append("1. **Review orphans** (conn < 5): Consider deleting or merging\n")
    report_lines.append("2. **Strengthen low-connect** (5 ≤ conn < 15): Add links to related notes\n")
    report_lines.append("3. **Check for duplicates**: Look for similar-named nodes in different communities\n")

    return "".join(report_lines)

def generate_bridge_notes_report(node_connections, node_details, edges):
    """Generate report on bridge notes between technical and non-technical domains"""
    report_lines = [
        "# Bridge Notes Analysis\n",
        f"*Generated on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}*\n",
        "## 🌉 Notes Connecting Technical ↔ Non-Technical Domains\n"
    ]

    # Define domain keywords
    technical_keywords = {'map', 'filter', 'reduce', 'function', 'method', 'error', 'task', 'promise', 'async', 'now', 'time', 'date', 'trim', 'min', 'max', 'includes', 'has', 'values'}
    philosophy_keywords = {'value', 'ethic', 'morality', 'principle', 'belief', 'truth', 'good', 'justice', 'beauty', 'virtue'}
    political_keywords = {'power', 'authority', 'governance', 'policy', 'rights', 'freedom', 'justice', 'equality', 'democracy'}
    religious_keywords = {'god', 'divine', 'sacred', 'ritual', 'myth', 'scripture', 'faith', 'spiritual', 'theology'}

    bridge_candidates = []

    for node_id, conn_count in node_connections.items():
        details = node_details.get(node_id, {})
        label = details.get('label', '').lower()
        node_type = details.get('type', '').lower()

        # Check if node has technical AND non-technical connections
        tech_score = sum(1 for kw in technical_keywords if kw in label)
        phil_score = sum(1 for kw in philosophy_keywords if kw in label)
        pol_score = sum(1 for kw in political_keywords if kw in label)
        rel_score = sum(1 for kw in religious_keywords if kw in label)

        non_tech_score = phil_score + pol_score + rel_score

        if tech_score > 0 and non_tech_score > 0 and conn_count > 50:  # Meaningful bridge
            bridge_candidates.append({
                'id': node_id,
                'label': details.get('label', node_id),
                'connections': conn_count,
                'tech_score': tech_score,
                'non_tech_score': non_tech_score,
                'type': details.get('type', 'unknown'),
                'domains': []
            })

            if tech_score > 0:
                bridge_candidates[-1]['domains'].append('Technical')
            if phil_score > 0:
                bridge_candidates[-1]['domains'].append('Philosophy')
            if pol_score > 0:
                bridge_candidates[-1]['domains'].append('Political Analysis')
            if rel_score > 0:
                bridge_candidates[-1]['domains'].append('Religious Archaeology')

    # Sort by connection count
    bridge_candidates.sort(key=lambda x: x['connections'], reverse=True)

    if bridge_candidates:
        report_lines.append("| Node | Label | Connections | Tech Score | Non-Tech Score | Domains |\n")
        report_lines.append("|------|-------|-------------|------------|----------------|---------|\n")

        for candidate in bridge_candidates[:10]:
            domains_str = ", ".join(candidate['domains'])
            report_lines.append(f"| `{candidate['id']}` | {candidate['label']} | {candidate['connections']} | {candidate['tech_score']} | {candidate['non_tech_score']} | {domains_str} |\n")
    else:
        report_lines.append("No strong bridge nodes detected with current keyword matching.\n")
        report_lines.append("Try running with lower connection threshold or check edge analysis for inferred connections.\n")

    report_lines.append("\n## 🔍 Edge-Based Bridge Analysis\n")
    report_lines.append("Looking at inferred edges (AI-discovered connections) for hidden bridges...\n")

    # Analyze edges for bridge characteristics
    tech_to_nontech_edges = 0
    total_inferred = 0

    for edge in edges:
        source_id = edge.get('source')
        target_id = edge.get('target')
        confidence = edge.get('confidence', 1.0)
        is_inferred = edge.get('inferred', False) or confidence < 0.9  # Assume lower confidence = inferred

        if is_inferred:
            total_inferred += 1

            source_label = node_details.get(source_id, {}).get('label', '').lower() if source_id else ''
            target_label = node_details.get(target_id, {}).get('label', '').lower() if target_id else ''

            source_is_tech = any(kw in source_label for kw in technical_keywords)
            target_is_tech = any(kw in target_label for kw in technical_keywords)

            source_is_nontech = any(kw in source_label for kw in (philosophy_keywords | political_keywords | religious_keywords))
            target_is_nontech = any(kw in target_label for kw in (philosophy_keywords | political_keywords | religious_keywords))

            if (source_is_tech and target_is_nontech) or (source_is_nontech and target_is_tech):
                tech_to_nontech_edges += 1

    report_lines.append(f"- Total inferred edges: {total_inferred}\n")
    report_lines.append(f"- Inferred edges connecting technical ↔ non-technical: {tech_to_nontech_edges}\n")
    if total_inferred > 0:
        percentage = (tech_to_nontech_edges / total_inferred) * 100
        report_lines.append(f"- Percentage of inferred edges that are bridges: {percentage:.1f}%\n")

    return "".join(report_lines)

def generate_edge_confidence_report(node_connections, node_details, edges):
    """Generate report on edge confidence and extraction vs inferred breakdown"""
    report_lines = [
        "# Edge Confidence Analysis\n",
        f"*Generated on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}*\n",
        "## 📊 Extraction vs. Inferred Edge Breakdown\n"
    ]

    # Analyze edges by confidence
    extracted_edges = []  # High confidence (explicit wikilinks)
    inferred_edges = []   # Lower confidence (AI-discovered)
    ambiguous_edges = []  # Very low confidence

    for edge in edges:
        confidence = edge.get('confidence', 1.0)
        if confidence >= 0.9:
            extracted_edges.append(edge)
        elif confidence >= 0.6:
            inferred_edges.append(edge)
        else:
            ambiguous_edges.append(edge)

    total_edges = len(edges)

    report_lines.append(f"| Edge Type | Count | Percentage | Description |\n")
    report_lines.append(f"|-----------|-------|------------|-------------|\n")
    report_lines.append(f"| Extracted (explicit links) | {len(extracted_edges)} | {len(extracted_edges)/total_edges*100:.1f}% | High confidence (≥0.9), likely manual [[wikilinks]] |\n")
    report_lines.append(f"| Inferred (AI-discovered) | {len(inferred_edges)} | {len(inferred_edges)/total_edges*100:.1f}% | Medium confidence (0.6-0.89), AI-generated connections |\n")
    report_lines.append(f"| Ambiguous (weak links) | {len(ambiguous_edges)} | {len(ambiguous_edges)/total_edges*100:.1f}% | Low confidence (<0.6), needs review |\n")
    report_lines.append(f"| **TOTAL** | {total_edges} | 100% | |\n")

    report_lines.append("\## 🎯 Per-God-Node Confidence Analysis\n")

    # Get top God nodes
    top_nodes = sorted(node_connections.items(), key=lambda x: x[1], reverse=True)[:10]

    report_lines.append("| God Node | Total Edges | Extracted | Inferred | Ambiguous | Avg Confidence |\n")
    report_lines.append("|----------|-------------|-----------|----------|-----------|----------------|\n")

    for node_id, conn_count in top_nodes:
        node_edges = [e for e in edges if e.get('source') == node_id or e.get('target') == node_id]
        if not node_edges:
            continue

        node_extracted = [e for e in node_edges if e.get('confidence', 1.0) >= 0.9]
        node_inferred = [e for e in node_edges if 0.6 <= e.get('confidence', 1.0) < 0.9]
        node_ambiguous = [e for e in node_edges if e.get('confidence', 1.0) < 0.6]

        avg_conf = sum(e.get('confidence', 1.0) for e in node_edges) / len(node_edges) if node_edges else 0

        label = node_details.get(node_id, {}).get('label', node_id)
        report_lines.append(f"| `{label}` | {len(node_edges)} | {len(node_extracted)} | {len(node_inferred)} | {len(node_ambiguous)} | {avg_conf:.2f} |\n")

    report_lines.append("\n## 🔧 Recommended Actions\n")
    report_lines.append("1. **Strengthen weak inferred links**: For edges with confidence < 0.6, consider:\n")
    report_lines.append("   - Adding explicit `[[wikilinks]]` in Obsidian\n")
    report_lines.append("   - Merging duplicate/similar notes\n")
    report_lines.append("   - Adding clarifying content to justify the connection\n")
    report_lines.append("2. **Review ambiguous edges**: Manually verify if connections < 0.6 confidence are valid\n")
    report_lines.append("3. **Increase extracted ratio**: Aim to convert inferred edges to explicit links through better note linking\n")

    return "".join(report_lines)

def generate_action_plan_report(node_connections, node_details, edges, communities):
    """Generate master action plan with checkboxes"""
    report_lines = [
        "# Master Action Plan\n",
        f"*Generated on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}*\n",
        "## ✅ Phase 1: Immediate Actions (This Week)\n"
    ]

    # Calculate metrics
    total_nodes = len(node_connections)
    high_conn_nodes = sum(1 for c in node_connections.values() if c > 1000)
    orphan_nodes = sum(1 for c in node_connections.values() if c < 5)
    low_conn_nodes = sum(1 for c in node_connections.values() if 5 <= c < 15)

    # Edge analysis
    extracted_edges = sum(1 for e in edges if e.get('confidence', 1.0) >= 0.9)
    total_edges = len(edges)
    extracted_percentage = (extracted_edges / total_edges * 100) if total_edges > 0 else 0

    report_lines.append("- [ ] Create MOC for God nodes: `00 - SYSTEM/01_KNOWLEDGE_HUB.md`\n")
    report_lines.append("- [ ] Create/toplink top 5 God node notes\n")
    report_lines.append("- [ ] Review and tag orphan nodes (<5 connections): `#orphan`\n")
    report_lines.append("- [ ] Strengthen low-connection nodes (5-15 connections): Add 2-3 relevant links each\n")
    report_lines.append("- [ ] Run Dataview queries to identify bridge notes\n")
    report_lines.append(f"- [ ] Improve extracted edge ratio from {extracted_percentage:.1f}% → 60%+\n")

    report_lines.append("\n## 📈 Phase 2: Short-Term Goals (2-4 Weeks)\n")
    report_lines.append("- [ ] Review and merge duplicate communities\n")
    report_lines.append("- [ ] Create community-based MOCs for major themes\n")
    report_lines.append("- [ ] Establish linking convention: Technical ↔ Philosophical bridges\n")
    report_lines.append("- [ ] Set up weekly graph review ritual\n")
    report_lines.append("- [ ] Achieve 70%+ extracted edge ratio\n")

    report_lines.append("\n## 🎯 Phase 3: Long-Term Vision (1-3 Months)\n")
    report_lines.append("- [ ] Develop specialized dashboards for each PARA+ area\n")
    report_lines.append("- [ ] Create automated link suggestions based on graph analysis\n")
    report_lines.append("- [ ] Integrate with task management system via `Task` god node\n")
    report_lines.append("- [ ] Reach 80%+ extracted edge ratio\n")
    report_lines.append("- [ ] Publish insights from bridge note analysis\n")

    report_lines.append("\n## 📊 Progress Tracking\n")
    report_lines.append("| Metric | Current | Target (1w) | Target (4w) | Target (12w) |\n")
    report_lines.append("|--------|---------|-------------|-------------|--------------|\n")
    report_lines.append(f"| Total Nodes | {total_nodes} | {total_nodes} | {total_nodes} | {total_nodes} |\n")
    report_lines.append(f"| God Nodes (>1000 conn) | {high_conn_nodes} | {high_conn_nodes} | {high_conn_nodes} | {high_conn_nodes} |\n")
    report_lines.append(f"| Orphan Nodes (<5 conn) | {orphan_nodes} | max({orphan_nodes-5}, 0) | max({orphan_nodes-10}, 0) | 0 |\n")
    report_lines.append(f"| Extracted Edge Ratio | {extracted_percentage:.1f}% | {min(extracted_percentage+10, 60):.1f}% | {min(extracted_percentage+20, 70):.1f}% | {min(extracted_percentage+30, 80):.1f}% |\n")
    report_lines.append(f"| Communities | {len(communities) if communities else 'N/A'} | Review top 20 | Merge similar | Optimize structure |\n")

    report_lines.append("\n## 🔄 Weekly Maintenance Ritual\n")
    report_lines.append("1. **Monday**: Run vault analyzer and update reports\n")
    report_lines.append("2. **Wednesday**: Review `#orphan` notes - delete, merge, or develop\n")
    report_lines.append("3. **Friday**: Strengthen weak inferred links (add 5 explicit `[[wikilinks]]`)\n")
    report_lines.append("4. **Weekly**: Update action plan checkboxes\n")

    return "".join(report_lines)

def save_reports(reports, output_dir):
    """Save all reports to the output directory"""
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    for filename, content in reports.items():
        file_path = output_path / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Saved {file_path}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 vault_analyzer.py <knowledge-graph.json> <vault-root-path>")
        print("Example: python3 vault_analyzer.py .understand-anything/knowledge-graph.json .")
        sys.exit(1)

    json_path = sys.argv[1]
    vault_path = sys.argv[2]

    print("🔍 Loading knowledge graph...")
    graph_data = load_knowledge_graph(json_path)

    print("📊 Analyzing nodes and edges...")
    node_connections, node_details, edges = analyze_nodes(graph_data)
    communities = analyze_communities(graph_data)

    print(f"   Found {len(node_connections)} nodes and {len(edges)} edges")
    print(f"   Found {len(communities)} communities")

    # Generate reports
    print("📝 Generating reports...")
    reports = {
        "01_god_nodes_dashboard.md": generate_god_nodes_report(node_connections, node_details, vault_path),
        "02_orphaned_communities.md": generate_orphaned_communities_report(communities, node_connections, node_details),
        "03_bridge_notes.md": generate_bridge_notes_report(node_connections, node_details, edges),
        "04_edge_confidence.md": generate_edge_confidence_report(node_connections, node_details, edges),
        "05_master_action_plan.md": generate_action_plan_report(node_connections, node_details, edges, communities)
    }

    # Save reports
    output_dir = Path(vault_path) / "00 - SYSTEM" / "Graph Reports"
    save_reports(reports, output_dir)

    print(f"\n🎉 Analysis complete! Reports saved to: {output_dir}")
    print("\n📋 Next steps:")
    print("1. Copy 00_Master_MOC_God_Nodes.md to your KNOWLEDGE_HUB or Master MOC")
    print("2. Review the reports in 00 - SYSTEM/Graph Reports/")
    print("3. Start with Phase 1 actions in 05_master_action_plan.md")
    print("4. Use the Dataview queries from DATAVIEW_QUERIES.md")

if __name__ == "__main__":
    main()