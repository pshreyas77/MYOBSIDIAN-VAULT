#!/usr/bin/env python3
"""
Generate professional Obsidian graph.json with category-based color groups.

Run this script to update .obsidian/graph.json with the latest color scheme.
"""

import json
from pathlib import Path

# Professional color palette - dark theme compatible
# Format: (hex_string, rgb_int_for_obsidian)
COLOR_GROUPS = [
    # === STRUCTURAL (Blues) ===
    {
        "name": "🗺️ MOCs (Maps of Content)",
        "query": "tag:#moc",
        "color": "#4E79A7",
        "description": "Orientation maps for each domain"
    },
    {
        "name": "📁 Active Projects",
        "query": "path:\"03 - PROJECTS\"",
        "color": "#A0C4E8",
        "description": "Current active project hubs"
    },
    {
        "name": "📅 Daily Notes",
        "query": "path:\"04 - DAILY\" OR path:\"Daily Notes\"",
        "color": "#6BA4D6",
        "description": "Chronological daily captures"
    },
    
    # === RESEARCH DOMAINS (Warm Spectrum) ===
    {
        "name": "🗳️ Politics & Governance",
        "query": "tag:#indian-politics OR tag:#dravidian-movement OR tag:#bjp OR tag:#rss OR path:\"Research/Politics\"",
        "color": "#E15759",
        "description": "Indian political history, parties, elections"
    },
    {
        "name": "🧘 Philosophy & Religion",
        "query": "tag:#philosophy OR tag:#religion OR tag:#anti-caste OR tag:#rationalism OR path:\"Research/Philosophy\"",
        "color": "#B07AA1",
        "description": "Indian philosophy, rationalism, anti-caste"
    },
    {
        "name": "🏛️ Ancient History & Archaeology",
        "query": "tag:#civilizations OR tag:#archaeology OR tag:#ivc OR path:\"02 - AREAS/03 Ancient Civilizations\"",
        "color": "#9C755F",
        "description": "Ancient civilizations, IVC, archaeology"
    },
    {
        "name": "🧬 Population Genetics",
        "query": "tag:#population-genetics OR tag:#ancient-dna OR tag:#admixture OR path:\"05 - MAPS/Population Genetics\"",
        "color": "#76B7B2",
        "description": "aDNA, admixture modeling, ANI/ASI/AASI"
    },
    {
        "name": "📝 Historical Linguistics",
        "query": "tag:#historical-linguistics OR tag:#comparative-method OR tag:#indo-european OR path:\"05 - MAPS/Historical Linguistics\"",
        "color": "#59A14F",
        "description": "PIE reconstruction, Mitanni IA, sound laws"
    },
    {
        "name": "🏺 Epigraphy & Evidence",
        "query": "tag:#epigraphy OR tag:#inscriptions OR tag:#evidence-grading OR path:\"05 - MAPS/Epigraphy\"",
        "color": "#EDC948",
        "description": "Inscriptions, dating, evidence tiers"
    },
    {
        "name": "🤖 AI & Technology",
        "query": "tag:#ai OR tag:#autonomous-agents OR tag:#mcp OR tag:#ollama OR path:\"Research/AI Tools\" OR path:\"05 - MAPS/AI\"",
        "color": "#F28E2B",
        "description": "Local LLMs, agents, MCP, tool stack"
    },
    {
        "name": "💪 Health & Fitness",
        "query": "tag:#health OR tag:#fitness OR tag:#supplements OR path:\"05 - MAPS/Health\"",
        "color": "#FF9DA7",
        "description": "12-week protocol, supplements, genomics"
    },
    {
        "name": "🌱 PKM & Digital Garden",
        "query": "tag:#digital-garden OR tag:#pkm OR tag:#knowledge-graph OR tag:#progressive-summarization OR path:\"05 - MAPS/Digital Garden\"",
        "color": "#4E79A7",
        "description": "Garden methodology, writing pipeline, graphs"
    },
    
    # === ENTITY TYPES ===
    {
        "name": "👤 Historical Figures",
        "query": "path:\"wiki/entities\" AND (tag:#person OR tag:#historical-figure)",
        "color": "#E15759",
        "description": "People entities: Ambedkar, Periyar, Kabir, etc."
    },
    {
        "name": "🏛️ Organizations & Movements",
        "query": "path:\"wiki/entities\" AND (tag:#organization OR tag:#party OR tag:#movement)",
        "color": "#F28E2B",
        "description": "Parties, orgs: DK, DMK, AIADMK, RSS, TVK"
    },
    {
        "name": "💭 Concepts & Theories",
        "query": "path:\"wiki/concepts\"",
        "color": "#B07AA1",
        "description": "Abstract concepts: Shramana, ANI-ASI, etc."
    },
    {
        "name": "📍 Places & Geography",
        "query": "tag:#place OR tag:#geography",
        "color": "#59A14F",
        "description": "Geographic entities"
    },
    
    # === NOTE TYPES ===
    {
        "name": "📚 Literature Notes",
        "query": "path:\"01 - LITERATURE\" OR path:\"1-desk/article\"",
        "color": "#76B7B2",
        "description": "External source notes, papers, articles"
    },
    {
        "name": "✨ Outputs & Essays",
        "query": "path:\"06 - OUTPUTS\"",
        "color": "#EDC948",
        "description": "Finished essays, synthesis, publications"
    },
    {
        "name": "⚙️ System & Templates",
        "query": "path:\"00 - SYSTEM\" OR path:\"07 - SYSTEM\" OR path:\"00 - SYSTEM/Templates\"",
        "color": "#BAB0AC",
        "description": "Templates, configs, system files"
    },
    {
        "name": "📥 Inbox & Fleeting",
        "query": "path:\"00 - INBOX\" OR path:\"inbox\" OR path:\"fleeting\" OR path:\"QUEUE\"",
        "color": "#BAB0AC",
        "description": "Unprocessed captures, fleeting notes"
    },
]


def generate_graph_json():
    """Generate the graph.json configuration."""
    color_groups = []
    
    for group in COLOR_GROUPS:
        hex_color = group["color"]
        rgb_int = int(hex_color.lstrip('#'), 16)
        
        color_groups.append({
            "query": group["query"],
            "color": {
                "a": 1,
                "rgb": rgb_int
            }
        })
    
    config = {
        "collapse-filter": False,
        "search": "",
        "showTags": True,
        "showAttachments": False,
        "hideUnresolved": True,
        "showOrphans": True,
        "collapse-color-groups": True,
        "collapse-display": True,
        "showArrow": True,
        "textFadeMultiplier": 0,
        "nodeSizeMultiplier": 1.2,
        "lineSizeMultiplier": 1,
        "collapse-forces": False,
        "centerStrength": 0.35,
        "repelStrength": 8.5,
        "linkStrength": 0.85,
        "linkDistance": 220,
        "scale": 0.02,
        "close": False,
        "colorGroups": color_groups
    }
    
    return config


def main():
    vault_path = Path(r"E:\_Knowledge\ObsidianVault")
    graph_path = vault_path / ".obsidian" / "graph.json"
    
    config = generate_graph_json()
    
    # Ensure .obsidian directory exists
    graph_path.parent.mkdir(exist_ok=True)
    
    # Write the config
    with open(graph_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)
    
    print(f"✅ Generated {graph_path}")
    print(f"   Color groups: {len(config['colorGroups'])}")
    print(f"   Groups:")
    for i, g in enumerate(config['colorGroups']):
        hex_color = f"#{g['color']['rgb']:06x}"
        print(f"     {i+1:2d}. {hex_color} — {g['query'][:60]}...")


if __name__ == "__main__":
    main()