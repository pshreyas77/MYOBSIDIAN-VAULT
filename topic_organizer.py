#!/usr/bin/env python3
"""
Topic-Based Vault Organizer
Analyzes content and creates topic folders with intelligent interlinking.
"""

import os
import re
import shutil
from pathlib import Path
from collections import defaultdict

VAULT_ROOT = Path("/home/sunny77/Documents/Obsidian Vault")

class TopicOrganizer:
    def __init__(self):
        self.areas = {
            "01 Philosophy & Religion": [],
            "02 AI & Technology": [],
            "03 Ancient Civilizations": [],
            "04 Political Analysis": [],
            "05 Knowledge Management": [],
            "06 Personal Development": [],
            "06 Society & Culture": [],
        }
        self.topic_clusters = defaultdict(list)

    def analyze_files(self):
        """Analyze all files in areas and identify topics."""
        areas_dir = VAULT_ROOT / "02 - AREAS"

        for area in areas_dir.iterdir():
            if not area.is_dir():
                continue

            area_name = area.name
            md_files = list(area.glob("*.md"))

            for file in md_files:
                if file.name.startswith("00_") or file.name.startswith("Index") or file.name.startswith("README"):
                    continue

                topics = self.extract_topics(file)
                self.topic_clusters[(area_name, tuple(topics))].append(file)

    def extract_topics(self, file_path):
        """Extract topics from filename and content."""
        filename = file_path.stem.lower()
        topics = set()

        # Extract from filename patterns
        topic_patterns = {
            # Technology
            "ai": ["ai", "artificial intelligence", "chatbot", "llm", "claude", "gpt", "machine learning", "deep learning"],
            "web-dev": ["web", "website", "frontend", "backend", "html", "css", "javascript", "react"],
            "programming": ["python", "code", "script", "programming", "software"],
            "data-science": ["data", "analysis", "pandas", "numpy", "visualization"],
            "security": ["security", "cryptography", "privacy", "spyware"],
            "os-systems": ["linux", "windows", "os", "system", "docker"],

            # Philosophy
            "philosophy-comparison": ["shankara", "vs", "philosopher", "comparison", "greek", "chinese"],
            "buddhism": ["buddha", "buddhism", "nirvana", "dharma", "sangha"],
            "hinduism": ["hindu", "hinduism", "vedic", "vedas", "brahman"],
            "atheism": ["atheist", "atheism", "critical", "rational"],
            "metaphysics": ["metaphysics", "consciousness", "reality", "illusion"],

            # Ancient Civilizations
            "indus-valley": ["ivc", "indus", "mohenjo", "harappa"],
            "sumeria": ["sumerian", "mesopotamia", "cuneiform"],
            "ancient-india": ["chanakya", "mauryan", "ashoka", "ancient"],
            "egypt": ["egypt", "pharaoh", "pyramid"],

            # Politics
            "indian-politics": ["bjp", "congress", "india politics", "election"],
            "world-politics": ["global", "conflict", "geopolitics", "international"],
            "zionism": ["zionism", "israel", "hindutva", "nationalism"],
            "communism": ["communist", "ussr", "stalin", "mao", "marx"],

            # Comics/Cosmology
            "marvel-dc": ["marvel", "dc", "comics", "superhero", "cosmic", "multiverse"],
            "power-scaling": ["power", "battle", "vs", "cosmology"],

            # Society
            "caste": ["caste", "varna", "brahmin", "dalit"],
            "social-systems": ["society", "social", "culture", "community"],

            # Personal Development
            "productivity": ["productivity", "system", "habit", "routine"],
            "career": ["job", "career", "interview", "resume", "work"],
            "knowledge": ["moc", "reflection", "learning", "study"],

            # Media
            "movies": ["movie", "film", "cinema", "media"],
            "games": ["game", "gaming", "interactive"],
        }

        # Check filename against patterns
        for topic, keywords in topic_patterns.items():
            for keyword in keywords:
                if keyword in filename:
                    topics.add(topic)
                    break

        # Add date-based organization
        date_match = re.match(r'(\d{4})-(\d{2})-(\d{2})', file_path.stem)
        if date_match:
            year = date_match.group(1)
            topics.add(f"year-{year}")

        return sorted(topics)

    def create_topic_structure(self):
        """Create topic-based folder structure."""
        areas_dir = VAULT_ROOT / "02 - AREAS"

        for area in areas_dir.iterdir():
            if not area.is_dir():
                continue

            area_name = area.name
            md_files = list(area.glob("*.md"))

            # Categorize files
            topic_files = defaultdict(list)

            for file in md_files:
                if file.name.startswith("00_") or file.name.startswith("Index") or file.name.startswith("README"):
                    continue

                topics = self.extract_topics(file)

                # Use first topic or "Other"
                if topics:
                    primary_topic = topics[0]
                else:
                    primary_topic = "Other"

                topic_files[primary_topic].append(file)

            # Create topic folders
            for topic, files in topic_files.items():
                if len(files) >= 2:  # Only create folder if 2+ files
                    topic_folder = area / topic.replace(" ", "_")
                    if not topic_folder.exists():
                        print(f"Creating: {topic_folder}")
                        topic_folder.mkdir(parents=True)

                    # Move files to topic folder
                    for file in files:
                        dest = topic_folder / file.name
                        if not dest.exists():
                            shutil.move(str(file), str(dest))
                            print(f"  → {file.name}")

    def generate_topic_mocs(self):
        """Generate topic-level MOCs with interlinking."""
        areas_dir = VAULT_ROOT / "02 - AREAS"

        for area in areas_dir.iterdir():
            if not area.is_dir():
                continue

            area_name = area.name
            topic_folders = [d for d in area.iterdir() if d.is_dir() and not d.name.startswith(".")]

            for topic_folder in topic_folders:
                if topic_folder.name.startswith("00_"):
                    continue

                topic_files = list(topic_folder.glob("*.md"))
                if not topic_files:
                    continue

                # Create topic MOC
                moc_name = f"00_{topic_folder.name}_MOC.md"
                moc_path = topic_folder / moc_name

                content = self.generate_moc_content(area_name, topic_folder.name, topic_files)
                moc_path.write_text(content, encoding='utf-8')
                print(f"Created MOC: {moc_path}")

    def generate_moc_content(self, area_name, topic_name, files):
        """Generate MOC content for a topic."""
        # Get related topics (other folders in same area)
        area = VAULT_ROOT / "02 - AREAS" / area_name
        related_topics = [d.name for d in area.iterdir() if d.is_dir() and d.name != topic_name and not d.name.startswith(".") and not d.name.startswith("00_")]

        content = f"""---
tags: [moc, topic, {topic_name.lower().replace("_", "-")}]
date: 2026-04-20
aliases: [{topic_name.replace("_", " ")} Map of Content]
---

# 🗺️ {topic_name.replace("_", " ")} — Map of Content

**Area:** [[{area_name.replace(" ", "_")}_MOC|{area_name}]]  
**Topic:** {topic_name.replace("_", " ")}  
**Files:** {len(files)}  
**Updated:** 2026-04-20

---

## 📑 Files in This Topic

"""

        # Group by year if applicable
        files_by_year = defaultdict(list)
        for f in files:
            date_match = re.match(r'(\d{4})-(\d{2})-(\d{2})', f.stem)
            if date_match:
                year = date_match.group(1)
                files_by_year[year].append(f)
            else:
                files_by_year["Other"].append(f)

        for year in sorted(files_by_year.keys(), reverse=True):
            if year != "Other":
                content += f"### {year}\n\n"
            else:
                content += f"### Other\n\n"

            for f in sorted(files_by_year[year], key=lambda x: x.name, reverse=True):
                # Clean title
                title = re.sub(r'^(\d{4}-\d{2}-\d{2})_', '', f.stem)
                title = title.replace('_', ' ').replace('-', ' ').title()
                content += f"- [[{f.stem}|{title}]]\n"

            content += "\n"

        if related_topics:
            content += f"""
---

## 🔗 Related Topics

"""
            for related in related_topics[:5]:
                moc_file = f"00_{related}_MOC"
                content += f"- [[{moc_file}|{related.replace('_', ' ').title()}]]\n"

        content += f"""
---

## 💡 Connection Ideas

- How does this topic relate to your other areas of study?
- What patterns emerge across these files?
- What questions remain unanswered?
"""

        return content

    def update_area_mocs(self):
        """Update area MOCs to include topic links."""
        areas_dir = VAULT_ROOT / "02 - AREAS"

        for area in areas_dir.iterdir():
            if not area.is_dir():
                continue

            area_name = area.name
            moc_files = list(area.glob("*_MOC.md"))

            if not moc_files:
                # Create main MOC
                moc_name = f"00_{area_name.replace(' ', '_')}_MOC.md"
                moc_path = area / moc_name
            else:
                moc_path = moc_files[0]

            # Get topic folders
            topic_folders = [d for d in area.iterdir() if d.is_dir() and not d.name.startswith(".") and not d.name.startswith("00_")]

            if topic_folders:
                # Append topics section to MOC
                content = moc_path.read_text(encoding='utf-8') if moc_path.exists() else ""

                if "## 📂 Topic Clusters" not in content:
                    content += """\n\n## 📂 Topic Clusters\n\n"""
                    for folder in sorted(topic_folders, key=lambda x: x.name):
                        topic_moc = f"00_{folder.name}_MOC"
                        content += f"- [[{topic_moc}|{folder.name.replace('_', ' ').title()}]]\n"

                    moc_path.write_text(content, encoding='utf-8')
                    print(f"Updated MOC: {moc_path}")

    def run(self):
        """Execute full organization."""
        print("="*80)
        print("TOPIC-BASED VAULT ORGANIZER")
        print("="*80)
        print()

        print("Step 1: Analyzing files and creating topic structure...")
        self.create_topic_structure()
        print()

        print("Step 2: Generating topic MOCs...")
        self.generate_topic_mocs()
        print()

        print("Step 3: Updating area MOCs...")
        self.update_area_mocs()
        print()

        print("="*80)
        print("Organization Complete!")
        print("="*80)

if __name__ == "__main__":
    organizer = TopicOrganizer()
    organizer.run()
