#!/usr/bin/env python3
"""
Interlinking System - Creates connections between related topics
"""

from pathlib import Path
from collections import defaultdict
import re

VAULT_ROOT = Path("/home/sunny77/Documents/Obsidian Vault")

# Topic relationship mapping
TOPIC_RELATIONSHIPS = {
    "buddhism": ["hinduism", "ivc-connection", "shankara", "jainism", "religion-origins"],
    "shankara": ["atheism", "hinduism", "buddhism", "philosophy-comparison", "caste"],
    "atheism": ["shankara", "charvaka", "philosophy-comparison"],
    "hinduism": ["buddhism", "shankara", "caste", "ivc-connection", "zionism"],
    "caste": ["hinduism", "shankara", "brahminism"],
    "ivc-connection": ["buddhism", "hinduism", "sramana", "shramana"],

    # Technology connections
    "ai": ["tech-tools", "data-analysis", "career", "future-trends"],
    "marvel-dc": ["cosmology", "power-scaling", "philosophy"],
    "philosophy-comparison": ["shankara", "greek", "chinese", "nagarjuna"],
    "data-science": ["ai", "analysis", "career"],
    "os-systems": ["tech-tools", "linux", "performance"],

    # Ancient connections
    "sumeria": ["ancient-egypt", "indus-valley", "oldest-civilization"],
    "ancient-egypt": ["sumeria", "mesopotamia", "pharaohs"],
    "indus-valley": ["sramana", "buddhism", "sumeria", "ancient-india"],

    # Political connections
    "communism": ["ussr", "stalin", "mao", "world-politics"],
    "indian-politics": ["bjp", "congress", "elections", "nationalism"],
    "world-politics": ["communism", "geopolitics", "international-relations"],
}

def extract_wiki_links(file_path):
    """Extract all wiki-style links from a file."""
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    links = re.findall(r'\[\[(.+?)(?:\|.+?)?\]\]', content)
    return links

def find_related_files():
    """Find files that should be interlinked."""
    areas_dir = VAULT_ROOT / "02 - AREAS"
    all_files = {}

    for area in areas_dir.iterdir():
        if not area.is_dir():
            continue

        for md_file in area.rglob("*.md"):
            if md_file.name.startswith("00_"):
                continue

            all_files[md_file.stem] = md_file

    return all_files

def suggest_connections(all_files, target_file):
    """Suggest connections for a file based on content analysis."""
    suggestions = []
    content = target_file.read_text(encoding='utf-8', errors='ignore').lower()
    filename = target_file.stem.lower()

    # Check for keyword matches in filename
    keywords = {
        "shankara": ["shankara", "advaita", "brahman", "atman"],
        "buddha": ["buddha", "buddhism", "nirvana", "dharma"],
        "nagarjuna": ["nagarjuna", "madhyamaka", "emptiness"],
        "charvaka": ["charvaka", "materialist", "lokayata"],
        "ivc": ["ivc", "indus", "harappa", "mohenjo"],
        "sumeria": ["sumerian", "mesopotamia", "cuneiform"],
        "dc": ["dc", "comics", "marvel", "cosmic", "multiverse"],
        "ai": ["ai", "claude", "llm", "chatbot"],
        "claude": ["claude", "anthropic", "llm"],
        "politics": ["politics", "bjp", "congress", "election"],
        "caste": ["caste", "brahmin", "varna", "dalit"],
    }

    for concept, terms in keywords.items():
        score = 0
        for term in terms:
            if term in filename:
                score += 2
            if term in content[:5000]:  # Check first 5000 chars
                score += 1

        if score >= 2:
            # Find files related to this concept
            for other_stem, other_path in all_files.items():
                if other_path == target_file:
                    continue
                other_filename = other_stem.lower()
                for term in terms:
                    if term in other_filename:
                        if other_path not in suggestions:
                            suggestions.append((other_path, score))
                        break

    # Sort by score
    suggestions.sort(key=lambda x: x[1], reverse=True)
    return suggestions[:5]  # Top 5 suggestions

def generate_related_links_section(file_path, all_files):
    """Generate a "Related Links" section for a file."""
    suggestions = suggest_connections(all_files, file_path)

    if not suggestions:
        return None

    section = "\n\n---\n\n## 🔗 Related Notes\n\n"
    added = set()

    for suggested_path, score in suggestions:
        if suggested_path.stem in added:
            continue
        added.add(suggested_path.stem)

        # Clean title
        title = suggested_path.stem.replace('_', ' ')
        title = re.sub(r'^\d{4}-\d{2}-\d{2}\s+', '', title)
        title = title.replace('showdown', 'comparison').title()

        section += f"- [[{suggested_path.stem}|{title}]]\n"

    return section

def process_all_files():
    """Process all files and add related links."""
    all_files = find_related_files()
    updated_count = 0

    print("Generating interlinks for all files...")
    print(f"Total files: {len(all_files)}")
    print()

    for stem, file_path in list(all_files.items())[:100]:  # Process first 100
        content = file_path.read_text(encoding='utf-8')

        # Skip if already has a Related Notes section
        if "## 🔗 Related Notes" in content:
            continue

        # Generate related links
        related_section = generate_related_links_section(file_path, all_files)

        if related_section:
            new_content = content + related_section
            file_path.write_text(new_content, encoding='utf-8')
            updated_count += 1
            print(f"✓ {file_path.name}")

    print()
    print(f"Updated {updated_count} files with interlinks")

def update_area_mocs():
    """Update area MOCs with topic links."""
    areas_dir = VAULT_ROOT / "02 - AREAS"

    for area in areas_dir.iterdir():
        if not area.is_dir():
            continue

        # Find MOC files
        moc_files = list(area.glob("*_MOC.md"))
        if not moc_files:
            continue

        for moc in moc_files:
            content = moc.read_text(encoding='utf-8')

            # Add topic cluster section if not present
            if "## 📂 Topic Clusters" not in content:
                # Get topic folders
                topic_folders = [
                    d for d in area.iterdir()
                    if d.is_dir() and not d.name.startswith(".") and not d.name.startswith("00_")
                ]

                if topic_folders:
                    section = "\n\n## 📂 Topic Clusters\n\n"
                    for folder in sorted(topic_folders, key=lambda x: x.name):
                        topic_file = folder / f"00_{folder.name}_MOC.md"
                        if topic_file.exists():
                            section += f"- [[00_{folder.name}_MOC|{folder.name.replace('_', ' ').title()}]]\n"
                        else:
                            section += f"- [[./{folder.name}/|{folder.name.replace('_', ' ').title()}]]\n"

                    new_content = content + section
                    moc.write_text(new_content, encoding='utf-8')
                    print(f"✓ Updated {moc.name}")

if __name__ == "__main__":
    print("="*80)
    print("VAULT INTERLINKING SYSTEM")
    print("="*80)
    print()

    update_area_mocs()
    process_all_files()

    print()
    print("="*80)
    print("Interlinking Complete!")
    print("="*80)
