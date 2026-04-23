#!/usr/bin/env python3
"""
Professional Wiki Analyzer for Obsidian Vault
Analyzes link density, orphaned notes, and cross-area opportunities
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict, Counter
import datetime

def get_vault_path():
    """Get the Obsidian vault path"""
    return Path("/home/sunny77/Documents/Obsidian Vault")

def get_wiki_path():
    """Get the wiki path"""
    return get_vault_path() / "wiki"

def safe_read_file(file_path):
    """Safely read a file, returning empty string on error"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}")
        return ""

def extract_links(content):
    """Extract all wiki-style links from content"""
    # Pattern for [[link]] or [[link|alias]]
    pattern = r'\[\[([^\]]+)\]\]'
    matches = re.findall(pattern, content)
    # Clean links (remove aliases)
    links = []
    for match in matches:
        # Handle aliases like [[Page Name|Alias]]
        clean_link = match.split('|')[0].strip()
        if clean_link:  # Ignore empty links
            links.append(clean_link)
    return links

def get_all_notes():
    """Get all markdown notes in the vault (excluding templates and system files)"""
    vault_path = get_vault_path()
    notes = []

    # Areas to scan (based on observed structure)
    scan_areas = [
        "00 - SYSTEM",
        "01 - Projects",
        "02 - AREAS",
        "03 - RESOURCES",
        "04 - ARCHIVES",
        "Attachments",
        "wiki"  # Include wiki for completeness
    ]

    for area in scan_areas:
        area_path = vault_path / area
        if area_path.exists():
            # Find all markdown files
            for md_file in area_path.rglob("*.md"):
                # Skip template files and system files
                if "_templates" not in str(md_file) and ".openclaude" not in str(md_file):
                    notes.append(md_file)

    return notes

def analyze_link_density():
    """Analyze link density per vault area"""
    vault_path = get_vault_path()

    # Define areas to analyze
    areas = {
        "00 - SYSTEM": "System & Knowledge Hub",
        "01 - Projects": "Active Projects",
        "02 - AREAS": "Knowledge Areas",
        "03 - RESOURCES": "Reference Materials",
        "04 - ARCHIVES": "Archived Items",
        "Attachments": "Media Files",
        "wiki": "LLM Wiki System"
    }

    results = {}

    for area_path, area_name in areas.items():
        full_path = vault_path / area_path
        if not full_path.exists():
            results[area_name] = {
                'notes': 0,
                'total_links': 0,
                'avg_links_per_note': 0,
                'link_density': 'N/A (Area not found)'
            }
            continue

        # Find all markdown files in this area
        md_files = []
        for md_file in full_path.rglob("*.md"):
            if "_templates" not in str(md_file) and ".openclaude" not in str(md_file):
                md_files.append(md_file)

        total_links = 0
        total_notes = len(md_files)

        # Count links in each note
        for note in md_files:
            content = safe_read_file(note)
            links = extract_links(content)
            total_links += len(links)

        avg_links = total_links / max(total_notes, 1)

        # Determine density category
        if avg_links >= 10:
            density = 'Very High'
        elif avg_links >= 6:
            density = 'High'
        elif avg_links >= 3:
            density = 'Medium'
        elif avg_links >= 1:
            density = 'Low'
        else:
            density = 'Very Low'

        results[area_name] = {
            'notes': total_notes,
            'total_links': total_links,
            'avg_links_per_note': round(avg_links, 2),
            'link_density': density
        }

    return results

def find_orphaned_notes():
    """Find notes with zero incoming links"""
    vault_path = get_vault_path()

    # Build map of all note titles to files (using stem as title)
    all_notes = {}  # title -> file_path
    note_titles = set()

    # Scan all areas for notes
    scan_areas = [
        "00 - SYSTEM",
        "01 - Projects",
        "02 - AREAS",
        "03 - RESOURCES",
        "04 - ARCHIVES",
        "Attachments",
        "wiki"
    ]

    for area in scan_areas:
        area_path = vault_path / area
        if area_path.exists():
            for md_file in area_path.rglob("*.md"):
                if "_templates" not in str(md_file) and ".openclaude" not in str(md_file):
                    # Use filename stem as the note title
                    title = md_file.stem
                    all_notes[title] = md_file
                    note_titles.add(title)

    # Find all referenced notes
    referenced_notes = set()

    for area in scan_areas:
        area_path = vault_path / area
        if not area_path.exists():
            continue

        for md_file in area_path.rglob("*.md"):
            if "_templates" not in str(md_file) and ".openclaude" not in str(md_file):
                content = safe_read_file(md_file)
                links = extract_links(content)
                # Clean links for comparison
                for link in links:
                    # Normalize for comparison (remove extra spaces, etc.)
                    normalized = link.strip()
                    if normalized:
                        referenced_notes.add(normalized)

    # Orphans = notes that exist but are never referenced
    orphans = []
    for title, filepath in all_notes.items():
        # Skip expected orphans (like index files, templates)
        if title.lower() in ['index', 'readme', 'license', 'contributing']:
            continue
        if title not in referenced_notes:
            orphans.append((title, filepath))

    return orphans

def find_cross_area_opportunities():
    """Find notes that mention concepts from other areas but don't link to them"""
    vault_path = get_vault_path()

    # Define areas
    areas = {
        "00 - SYSTEM": "System & Knowledge Hub",
        "01 - Projects": "Active Projects",
        "02 - AREAS": "Knowledge Areas",
        "03 - RESOURCES": "Reference Materials",
        "04 - ARCHIVES": "Archived Items",
        "Attachments": "Media Files",
        "wiki": "LLM Wiki System"
    }

    # Build map of area -> set of note titles (concepts)
    area_concepts = defaultdict(set)

    for area_path, area_name in areas.items():
        full_path = vault_path / area_path
        if not full_path.exists():
            continue

        for md_file in full_path.rglob("*.md"):
            if "_templates" not in str(md_file) and ".openclaude" not in str(md_file):
                # Use filename stem as concept/note title
                concept_title = md_file.stem
                area_concepts[area_name].add(concept_title)

    # Find cross-area mentions without links
    opportunities = []

    for source_area_path, source_area_name in areas.items():
        source_path = vault_path / source_area_path
        if not source_path.exists():
            continue

        # Scan all notes in source area
        for md_file in source_path.rglob("*.md"):
            if "_templates" not in str(md_file) and ".openclaude" not in str(md_file):
                content = safe_read_file(md_file)

                # Extract potential concept mentions (capitalized phrases)
                # Look for sequences like "Concept Name" or "Concept One Two"
                concept_pattern = r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b'
                potential_concepts = re.findall(concept_pattern, content)

                # Get links actually present in this note
                present_links = set(extract_links(content))

                # Check each potential concept
                for concept in potential_concepts:
                    # Filter out very short or common false positives
                    if len(concept) < 3 or concept in ['The', 'And', 'Or', 'But', 'For', 'With', 'This', 'That', 'PDF', 'URL', 'HTML', 'CSS', 'JS', 'AI', 'LLM', 'API', 'UI', 'UX']:
                        continue

                    # Check if this concept exists as a note in ANY other area
                    found_in_other_area = False
                    target_area_name = None

                    for target_area_name, target_concepts in area_concepts.items():
                        if target_area_name == source_area_name:
                            continue  # Skip same area
                        if concept in target_concepts:
                            found_in_other_area = True
                            break

                    # If concept exists elsewhere and is NOT linked, it's an opportunity
                    if found_in_other_area and concept not in present_links:
                        opportunities.append({
                            'source_note': str(md_file.relative_to(vault_path)),
                            'source_note_title': md_file.stem,
                            'mentioned_concept': concept,
                            'target_area': target_area_name,
                            'suggested_link': f'[[{concept}]]',
                            'context': _get_context_around_mention(content, concept)
                        })

    # Deduplicate and prioritize
    # Group by (source_note, mentioned_concept) to avoid duplicates
    seen = set()
    unique_opportunities = []
    for opp in opportunities:
        key = (opp['source_note'], opp['mentioned_concept'])
        if key not in seen:
            seen.add(key)
            unique_opportunities.append(opp)

    # Sort by source note for easier review
    unique_opportunities.sort(key=lambda x: (x['source_note'], x['mentioned_concept']))

    return unique_opportunities

def _get_context_around_mention(content, concept, context_length=100):
    """Get text around a concept mention for context"""
    # Find the concept in content (case sensitive)
    pos = content.find(concept)
    if pos == -1:
        return ""

    start = max(0, pos - context_length)
    end = min(len(content), pos + len(concept) + context_length)
    return content[start:end].strip()

def analyze_graph_communities():
    """Analyze graph communities based on existing graphify data"""
    # Try to read existing graphify report
    graph_report_path = get_vault_path() / "graphify-out" / "GRAPH_REPORT.md"

    if not graph_report_path.exists():
        return {
            'error': 'Graphify report not found. Run graphify analysis first.',
            'communities': 0,
            'nodes': 0,
            'edges': 0,
            'isolated_nodes': [],
            'thin_communities': []
        }

    content = safe_read_file(graph_report_path)

    # Extract basic info from the report
    # This is a simplified extraction - in practice would parse more deeply
    nodes_match = re.search(r'(\d+)\s+nodes', content, re.IGNORECASE)
    edges_match = re.search(r'(\d+)\s+edges', content, re.IGNORECASE)
    communities_match = re.search(r'(\d+)\s+communities', content, re.IGNORECASE)

    nodes = int(nodes_match.group(1)) if nodes_match else 0
    edges = int(edges_match.group(1)) if edges_match else 0
    communities = int(communities_match.group(1)) if communities_match else 0

    # Look for isolated nodes and thin communities mentions
    isolated_nodes = []
    thin_communities = []

    # Simple pattern matching for now
    if 'isolated' in content.lower():
        isolated_nodes = ["See graphify report for details"]  # Placeholder

    if 'thin' in content.lower() or '<3' in content:
        thin_communities = ["See graphify report for details"]  # Placeholder

    return {
        'nodes': nodes,
        'edges': edges,
        'communities': communities,
        'isolated_nodes': isolated_nodes,
        'thin_communities': thin_communities,
        'note': 'Detailed analysis requires parsing graphify output more deeply'
    }

def generate_link_density_report():
    """Generate and save link density report"""
    wiki_path = get_wiki_path()
    analysis_path = wiki_path / "analysis"
    analysis_path.mkdir(exist_ok=True)

    report_path = analysis_path / "link-density-report.md"

    results = analyze_link_density()

    # Generate markdown report
    report_content = f"""# Link Density Analysis Report
*Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*

## Summary
This report analyzes the average number of wiki-style links per note in each vault area.

## Results by Area

| Area | Notes | Total Links | Avg Links/Note | Density |
|------|-------|-------------|----------------|---------|
"""

    for area_name, data in results.items():
        report_content += f"| {area_name} | {data['notes']} | {data['total_links']} | {data['avg_links_per_note']} | {data['link_density']} |\n"

    report_content += """
## Analysis
- **Very High Density** (10+ links/note): Highly interconnected knowledge
- **High Density** (6-9 links/note): Well-connected
- **Medium Density** (3-5 links/note): Moderately connected
- **Low Density** (1-2 links/note): Could benefit from more connections
- **Very Low Density** (<1 link/note): Largely isolated or orphaned

## Recommendations
1. Focus enhancement efforts on areas with Low or Very Low density
2. Use orphaned notes report to find specific notes needing connections
3. Leverage cross-area opportunities to build bridges between knowledge domains
4. Consider creating hub notes for areas with many low-density notes

---
*This analysis is additive-only and safe to run repeatedly.*
"""

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)

    print(f"Link density report generated: {report_path}")
    return str(report_path)

def generate_orphaned_notes_report():
    """Generate and save orphaned notes report"""
    wiki_path = get_wiki_path()
    analysis_path = wiki_path / "analysis"
    analysis_path.mkdir(exist_ok=True)

    report_path = analysis_path / "orphan-notes-report.md"

    orphans = find_orphaned_notes()

    # Generate markdown report
    report_content = f"""# Orphaned Notes Report
*Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*

## Summary
This report identifies notes that exist in the vault but have zero incoming links from other notes.
These notes are "orphans" in the knowledge graph and may benefit from intentional connections.

## Total Orphaned Notes Found: {len(orphans)}

## Orphaned Notes List

| Note Title | File Path | Suggested Connections |
|------------|-----------|----------------------|
"""

    if not orphans:
        report_content += "| None found | - | - |\n"
    else:
        for title, filepath in orphans[:50]:  # Limit to first 50 for readability
            relative_path = filepath.relative_to(get_vault_path())
            # Suggest potential connections based on title
            suggested = f"[[{title}]]"  # Basic suggestion - could be enhanced
            report_content += f"| {title} | {relative_path} | {suggested} |\n"

        if len(orphans) > 50:
            report_content += f"| ... and {len(orphans) - 50} more | See full list in data | - |\n"

    report_content += """
## Analysis
Orphaned notes represent knowledge that is not connected to your broader knowledge network.
While some orphans may be intentional (like standalone reference materials), many represent
missed opportunities for knowledge discovery and synthesis.

## Recommended Actions
1. **Review each orphan**: Determine if it should remain standalone or be connected
2. **Identify natural connections**: What other notes does this concept relate to?
3. **Add contextual links**: Insert links in appropriate contexts within related notes
4. **Consider hub notes**: For thematic groups of orphans, create connecting hub notes
5. **Use cross-analysis**: Check cross-area opportunities for connection suggestions

## Safety Note
All suggested connections are additive-only - they will only add links, never remove or modify existing content.

---
*This analysis is additive-only and safe to run repeatedly.*
"""

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)

    print(f"Orphaned notes report generated: {report_path}")
    return str(report_path)

def generate_cross_area_opportunities_report():
    """Generate and save cross-area opportunities report"""
    wiki_path = get_wiki_path()
    analysis_path = wiki_path / "analysis"
    analysis_path.mkdir(exist_ok=True)

    report_path = analysis_path / "cross-area-opportunities.md"

    opportunities = find_cross_area_opportunities()

    # Generate markdown report
    report_content = f"""# Cross-Area Linking Opportunities Report
*Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*

## Summary
This report identifies opportunities where concepts are mentioned in notes but not linked to their corresponding notes in other areas.
These represent chances to build bridges between knowledge domains.

## Total Opportunities Found: {len(opportunities)}

## Top Opportunities

| Source Note | Mentioned Concept | Suggested Link | Target Area | Context Preview |
|-------------|------------------|----------------|-------------|-----------------|
"""

    if not opportunities:
        report_content += "| None found | - | - | - | - |\n"
    else:
        for opp in opportunities[:30]:  # Limit to first 30
            source_note = opp['source_note']
            concept = opp['mentioned_concept']
            suggested_link = opp['suggested_link']
            target_area = opp['target_area']
            context = opp['context'][:50] + "..." if len(opp['context']) > 50 else opp['context']

            report_content += f"| {source_note} | {concept} | {suggested_link} | {target_area} | {context} |\n"

        if len(opportunities) > 30:
            report_content += f"| ... and {len(opportunities) - 30} more | See full data | - | - | - |\n"

    report_content += """
## Analysis
These opportunities represent moments where your knowledge already contains the concepts
that would benefit from linking, but the explicit connections are missing.
Adding these links will:
- Strengthen cross-disciplinary connections
- Improve knowledge discoverability
- Enhance the overall coherence of your knowledge graph
- Create pathways for serendipitous discovery

## Recommended Actions
1. **Review opportunities**: Validate that suggested connections make sense
2. **Prioritize by relevance**: Focus on connections that add genuine knowledge value
3. **Add contextually**: Insert links where they naturally flow in the text
4. **Consider bidirectionality**: If A mentions B, does B also mention or relate to A?
5. **Batch process**: Handle similar opportunities together for consistency

## Safety Note
All suggested connections are additive-only - they will only add links in appropriate contexts,
never remove or modify existing content.

---
*This analysis is additive-only and safe to run repeatedly.*
"""

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)

    print(f"Cross-area opportunities report generated: {report_path}")
    return str(report_path)

def generate_graph_communities_report():
    """Generate and save graph communities report"""
    wiki_path = get_wiki_path()
    analysis_path = wiki_path / "analysis"
    analysis_path.mkdir(exist_ok=True)

    report_path = analysis_path / "graph-communities-report.md"

    analysis = analyze_graph_communities()

    # Generate markdown report
    report_content = f"""# Graph Communities Analysis Report
*Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*

## Summary
This report analyzes the community structure of your knowledge graph based on graphify analysis.

## Overall Graph Statistics
- **Nodes (Concepts/Notes)**: {analysis.get('nodes', 'N/A')}
- **Edges (Connections)**: {analysis.get('edges', 'N/A')}
- **Communities (Knowledge Clusters)**: {analysis.get('communities', 'N/A')}

## Community Health Indicators
"""

    if 'isolated_nodes' in analysis:
        isolated_count = len(analysis['isolated_nodes']) if isinstance(analysis['isolated_nodes'], list) else 0
        report_content += f"- **Isolated Nodes**: {isolated_count} notes with no connections\n"

    if 'thin_communities' in analysis:
        thin_count = len(analysis['thin_communities']) if isinstance(analysis['thin_communities'], list) else 0
        report_content += f"- **Thin Communities (<3 nodes)**: {thin_count} small/isolated knowledge clusters\n"

    report_content += """
## Detailed Analysis
"""

    if 'error' in analysis:
        report_content += f"⚠️ **Note**: {analysis['error']}\n\n"
        report_content += "To get detailed community analysis, please run graphify analysis first:\n"
        report_content += "```bash\npython3 -c \"from graphify.watch import _rebuild_code; from pathlib import Path; _rebuild_code(Path('.'))\"\n```\n\n"

    report_content += """## Interpretation
- **Nodes**: Individual concepts or notes in your knowledge graph
- **Edges**: Explicit links between notes ([[link]] style)
- **Communities**: Clusters of tightly interconnected knowledge
- **Isolated Notes**: Knowledge that exists but isn't connected to anything else
- **Thin Communities**: Small knowledge clusters that may benefit from bridging connections

## Recommended Actions Based on Graph Analysis
1. **Address isolated notes**: Use orphaned notes report to find and connect them
2. **Strengthen thin communities**: Look for cross-area opportunities to bridge small clusters
3. **Enhance hub nodes**: Strengthen connections for high-betweenness nodes (like Config, LLMClient)
4. **Balance communities**: Work toward more evenly sized, interconnected knowledge clusters
5. **Monitor progress**: Re-run this analysis periodically to track improvement

## Integration with LLM Wiki System
This analysis complements the LLM Wiki system by:
- Identifying where the LLM should focus enrichment efforts
- Providing feedback on knowledge graph health
- Guiding query-to-wiki savings toward under-connected areas
- Informing linting routines about connection gaps

---
*Analysis based on existing graphify data. For latest insights, run graphify analysis.*
"""

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)

    print(f"Graph communities report generated: {report_path}")
    return str(report_path)

def main():
    """Main function for command line usage"""
    import sys

    if len(sys.argv) < 2:
        print("Usage: wiki_analyzer.py <command>")
        print("Commands:")
        print("  density     - Analyze link density by area")
        print("  orphans     - Find orphaned notes (zero incoming links)")
        print("  opportunities - Find cross-area linking opportunities")
        print("  communities - Analyze graph communities and structure")
        print("  all         - Run all analyses and generate reports")
        print("  help        - Show this help")
        return

    command = sys.argv[1].lower()

    if command == "density":
        print("🔍 Analyzing link density by area...")
        report_path = generate_link_density_report()
        print(f"✅ Link density report saved to: {report_path}")

    elif command == "orphans":
        print("🔍 Finding orphaned notes...")
        report_path = generate_orphaned_notes_report()
        print(f"✅ Orphaned notes report saved to: {report_path}")

    elif command == "opportunities":
        print("🔍 Finding cross-area linking opportunities...")
        report_path = generate_cross_area_opportunities_report()
        print(f"✅ Cross-area opportunities report saved to: {report_path}")

    elif command == "communities":
        print("🔍 Analyzing graph communities...")
        report_path = generate_graph_communities_report()
        print(f"✅ Graph communities report saved to: {report_path}")

    elif command == "all":
        print("🔍 Running complete analysis suite...")
        print("   1/4 Link density analysis...")
        density_path = generate_link_density_report()
        print("   2/4 Orphaned notes analysis...")
        orphans_path = generate_orphaned_notes_report()
        print("   3/4 Cross-area opportunities analysis...")
        opp_path = generate_cross_area_opportunities_report()
        print("   4/4 Graph communities analysis...")
        comm_path = generate_graph_communities_report()
        print("✅ All reports generated:")
        print(f"   • Link Density: {density_path}")
        print(f"   • Orphaned Notes: {orphans_path}")
        print(f"   • Cross-Area Opportunities: {opp_path}")
        print(f"   • Graph Communities: {comm_path}")

    elif command == "help":
        main()  # Recursive call to show help
        return

    else:
        print(f"Unknown command: {command}")
        print("Run 'wiki_analyzer.py help' for usage information")

if __name__ == "__main__":
    main()