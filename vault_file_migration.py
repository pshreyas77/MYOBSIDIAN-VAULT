#!/usr/bin/env python3
"""
Vault File Migration Script
Migrates scattered files into organized structure based on content analysis.
Creates cross-links between related topics.
"""

import os
import shutil
import hashlib
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set, Tuple, Optional
from collections import defaultdict

VAULT_ROOT = Path("/home/sunny77/Documents/Obsidian Vault")

# Mapping patterns for file categorization
CATEGORY_PATTERNS = {
    "02 - AREAS/01 Philosophy & Religion/": [
        r"(?i)buddha",
        r"(?i)buddhis",
        r"(?i)hindu",
        r"(?i)nagarjuna",
        r"(?i)shankara",
        r"(?i)charvaka",
        r"(?i)advaita",
        r"(?i)vedanta",
        r"(?i)jain",
        r"(?i)sramana",
        r"(?i)shramana",
        r"(?i)philosoph",
        r"(?i)atheist",
        r"(?i)materialis",
        r"(?i)osho",
        r"(?i)krishnamurt",
        r"(?i)comparative_.*religion",
        r"(?i)religious",
        r"(?i)theology",
        r"(?i)dharma",
        r"(?i)karma",
        r"(?i)maya",
        r"(?i)nirvana",
        r"(?i)meditation",
        r"(?i)spiritual",
    ],
    "02 - AREAS/02 AI & Technology/": [
        r"(?i)ai",
        r"(?i)llm",
        r"(?i)agent",
        r"(?i)claude",
        r"(?i)openai",
        r"(?i)gpt",
        r"(?i)machine.learning",
        r"(?i)neural",
        r"(?i)model",
        r"(?i)api",
        r"(?i)code",
        r"(?i)programming",
        r"(?i)python",
        r"(?i)javascript",
        r"(?i)development",
        r"(?i)software",
        r"(?i)system",
        r"(?i)jarvis",
        r"(?i)automation",
        r"(?i)bot",
        r"(?i)chatbot",
        r"(?i)obsidian.*api",
        r"(?i)rest.*api",
        r"(?i)plugin",
    ],
    "02 - AREAS/03 Ancient Civilizations/": [
        r"(?i)ancient",
        r"(?i)civilization",
        r"(?i)chanakya",
        r"(?i)ashoka",
        r"(?i)maurya",
        r"(?i)indus.*valley",
        r"(?i)harappa",
        r"(?i)mesopotami",
        r"(?i)egypt",
        r"(?i)greek",
        r"(?i)rome",
        r"(?i)roman",
        r"(?i)history",
        r"(?i)göbekli",
        r"(?i)goebekli",
        r"(?i)sumerian",
        r"(?i)babylonia",
        r"(?i)phoenician",
        r"(?i)historical",
        r"(?i)archaeolog",
        r"(?i)excavation",
    ],
    "02 - AREAS/04 Political Analysis/": [
        r"(?i)politic",
        r"(?i)government",
        r"(?i)democracy",
        r"(?i)election",
        r"(?i)party",
        r"(?i)policy",
        r"(?i)constitution",
        r"(?i)law",
        r"(?i)legislation",
        r"(?i)governance",
        r"(?i)power",
        r"(?i)authority",
        r"(?i)state",
        r"(?i)nation",
        r"(?i)marx",
        r"(?i)communist",
        r"(?i)socialist",
        r"(?i)liberal",
        r"(?i)conservative",
        r"(?i)revolution",
        r"(?i)war",
    ],
    "02 - AREAS/05 Knowledge Management/": [
        r"(?i)obsidian",
        r"(?i)second.brain",
        r"(?i)knowledge",
        r"(?i)pkm",
        r"(?i)zettelkasten",
        r"(?i)graph",
        r"(?i)map.of.content",
        r"(?i)moc",
        r"(?i)index",
        r"(?i)organization",
        r"(?i)system",
        r"(?i)workflow",
        r"(?i)template",
        r"(?i)methodology",
        r"(?i)research",
        r"(?i)note.taking",
    ],
    "02 - AREAS/06 Society & Culture/": [
        r"(?i)society",
        r"(?i)culture",
        r"(?i)social",
        r"(?i)caste",
        r"(?i)class",
        r"(?i)caste.*system",
        r"(?i)brahmin",
        r"(?i)dalit",
        r"(?i)tribe",
        r"(?i)community",
        r"(?i)tradition",
        r"(?i)custom",
        r"(?i)ritual",
        r"(?i)anthropolog",
        r"(?i)sociolog",
    ],
}

# Special file mappings (explicit mappings)
SPECIAL_MAPPINGS = {
    "BUDDHA/ANCIENT_CIVILIZATIONS_COMPARATIVE_RESEARCH_2026-04-19.md": "02 - AREAS/03 Ancient Civilizations/",
    "BUDDHA/Buddhism - Statue Statistics.md": "02 - AREAS/01 Philosophy & Religion/Buddhism/",
    "BUDDHA/Jainism - Statue Statistics.md": "02 - AREAS/01 Philosophy & Religion/Jainism/",
    "BUDDHA/00_BUDDHA_RESEARCH_HUB.md": "02 - AREAS/01 Philosophy & Religion/Buddhism/",
    "BUDDHA/IVC_Shramana_Buddhism_Jainism_Comparison.md": "02 - AREAS/01 Philosophy & Religion/",
    "BUDDHA/IVC_Sramana_Deep_Research_Report.md": "02 - AREAS/03 Ancient Civilizations/",
    "BUDDHA/01_CORE_EVIDENCE.md": "02 - AREAS/01 Philosophy & Religion/Buddhism/",
    "BUDDHA/02_COMPARATIVE_ANALYSIS.md": "02 - AREAS/01 Philosophy & Religion/",
    "BUDDHA/BUDDHA_GRAPH_REPORT.md": "02 - AREAS/05 Knowledge Management/Reports/",
    "BUDDHA/BUDDHA_DEEP_GRAPH_REPORT.md": "02 - AREAS/05 Knowledge Management/Reports/",
    
    # Philosophy files migration from 07 - Topics
    "07 - Topics/Philosophy_and_Ethics/Shankara_Caste_Brahminism_Promotion_Analysis.md": "02 - AREAS/01 Philosophy & Religion/",
    "07 - Topics/Philosophy_and_Ethics/Charvaka_Materialism_Analysis.md": "02 - AREAS/01 Philosophy & Religion/",
    "07 - Topics/Philosophy_and_Ethics/Nagarjuna_Charvaka_vs_Shankara_Cage_Match.md": "02 - AREAS/01 Philosophy & Religion/",
    "07 - Topics/Philosophy_and_Ethics/Shankara_vs_Greek_Philosophers_Showdown.md": "02 - AREAS/01 Philosophy & Religion/",
    "07 - Topics/Philosophy_and_Ethics/Ambedkar_Buddhism_Choice_Analysis.md": "02 - AREAS/01 Philosophy & Religion/",
    "07 - Topics/Philosophy_and_Ethics/Shankara_vs_Socrates_Diogenes_Triangular_Showdown.md": "02 - AREAS/01 Philosophy & Religion/",
    "07 - Topics/Philosophy_and_Ethics/Atheist_Hall_of_Fame_Shankara_Defeat_Rankings.md": "02 - AREAS/01 Philosophy & Religion/",
    "07 - Topics/Philosophy_and_Ethics/Osho_Krishnamurtis_vs_Shankara_Showdown.md": "02 - AREAS/01 Philosophy & Religion/",
    "07 - Topics/Philosophy_and_Ethics/Shankara_vs_Chinese_Philosophers_Showdown.md": "02 - AREAS/01 Philosophy & Religion/",
    "07 - Topics/Philosophy_and_Ethics/Shankara_Atheist_Critique.md": "02 - AREAS/01 Philosophy & Religion/",
    "07 - Topics/Philosophy_and_Ethics/Charvaka_vs_Shankara_Atheist_Scorecard.md": "02 - AREAS/01 Philosophy & Religion/",
    
    "07 - Topics/Philosophy_Debates_Research/PHILOSOPHERS_DEBATE_ANALYSIS.md": "02 - AREAS/01 Philosophy & Religion/",
}

class VaultMigrator:
    def __init__(self, vault_root: Path):
        self.vault_root = vault_root
        self.migration_plan: Dict[Path, Path] = {}  # source -> destination
        self.links_to_update: Dict[Path, List[Tuple[str, str]]] = defaultdict(list)  # file -> [(old_link, new_link)]
        self.errors: List[str] = []
        self.moved_count = 0
        
    def scan_all_files(self) -> List[Path]:
        """Scan all markdown files excluding system folders."""
        print("🔍 Scanning vault for markdown files...")
        md_files = []
        exclude = {
            '.git', '.obsidian', '.smart-env', '.claude', '.claude-plugin', '.qwen', 
            'graphify-out', '.trash', '.raw'
        }
        
        for path in self.vault_root.rglob("*.md"):
            # Check if any parent is excluded
            parts = set(path.parts)
            if not any(ex in parts for ex in exclude):
                md_files.append(path)
        
        print(f"✅ Found {len(md_files)} markdown files")
        return md_files
    
    def analyze_file_content(self, file_path: Path) -> Tuple[str, float]:
        """Analyze file content to determine best category."""
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')[:5000]  # First 5000 chars
            filename = file_path.name
            
            scores = defaultdict(float)
            
            # Check patterns against content and filename
            for category, patterns in CATEGORY_PATTERNS.items():
                for pattern in patterns:
                    # Content matches (weight: 2x)
                    content_matches = len(re.findall(pattern, content))
                    scores[category] += content_matches * 2
                    
                    # Filename matches (weight: 3x - stronger signal)
                    filename_matches = len(re.findall(pattern, filename))
                    scores[category] += filename_matches * 3
            
            # Special boost for philosophy files
            if "Buddha" in filename or "Shankara" in filename or "Nagarjuna" in filename:
                scores["02 - AREAS/01 Philosophy & Religion/"] += 10
            
            # Get best match
            if scores:
                best_category = max(scores, key=scores.get)
                best_score = scores[best_category]
                
                # Only categorize if score is significant
                if best_score >= 3:
                    return best_category, best_score
            
            return None, 0
            
        except Exception as e:
            print(f"⚠️ Error analyzing {file_path}: {e}")
            return None, 0
    
    def build_migration_plan(self, files: List[Path]) -> None:
        """Build comprehensive migration plan."""
        print("📋 Building migration plan...")
        
        for file_path in files:
            rel_path = file_path.relative_to(self.vault_root)
            str_path = str(rel_path)
            
            # Skip already organized files
            if str_path.startswith("02 - AREAS/") or str_path.startswith("01 - PROJECTS/"):
                if "Philosophy" not in str_path or "07 - Topics" not in str_path:
                    continue  # Already in final location
            
            # Check special mappings first
            if str_path in SPECIAL_MAPPINGS:
                dest_dir = self.vault_root / SPECIAL_MAPPINGS[str_path]
                self.migration_plan[file_path] = dest_dir / file_path.name
                continue
            
            # Check if parent folder suggests a category
            parent = file_path.parent.name.lower()
            
            # Known topic folders
            category_hint = None
            if "buddh" in parent or "hindu" in parent or "philosoph" in parent:
                category_hint = "02 - AREAS/01 Philosophy & Religion/"
            elif "ai" in parent or "tech" in parent:
                category_hint = "02 - AREAS/02 AI & Technology/"
            elif "ancient" in parent or "civilization" in parent or "history" in parent:
                category_hint = "02 - AREAS/03 Ancient Civilizations/"
            elif "politic" in parent:
                category_hint = "02 - AREAS/04 Political Analysis/"
            elif "knowledge" in parent or "obsidian" in parent:
                category_hint = "02 - AREAS/05 Knowledge Management/"
            elif "society" in parent or "culture" in parent:
                category_hint = "02 - AREAS/06 Society & Culture/"
            
            if category_hint:
                dest_dir = self.vault_root / category_hint
                self.migration_plan[file_path] = dest_dir / file_path.name
                continue
            
            # Analyze content for categorization
            category, score = self.analyze_file_content(file_path)
            if category:
                dest_dir = self.vault_root / category
                self.migration_plan[file_path] = dest_dir / file_path.name
            else:
                # Uncategorized - put in Resources or Archive
                if file_path.parent == self.vault_root:
                    self.migration_plan[file_path] = self.vault_root / "03 - RESOURCES" / file_path.name
        
        print(f"✅ Migration plan: {len(self.migration_plan)} files to move")
    
    def create_missing_directories(self) -> None:
        """Create all destination directories."""
        print("📁 Creating directories...")
        
        # Core structure
        dirs = [
            "02 - AREAS/01 Philosophy & Religion/Buddhism",
            "02 - AREAS/01 Philosophy & Religion/Hinduism",
            "02 - AREAS/01 Philosophy & Religion/Jainism",
            "02 - AREAS/01 Philosophy & Religion/Comparative",
            "02 - AREAS/02 AI & Technology/Agents",
            "02 - AREAS/02 AI & Technology/Projects",
            "02 - AREAS/02 AI & Technology/Research",
            "02 - AREAS/03 Ancient Civilizations",
            "02 - AREAS/04 Political Analysis",
            "02 - AREAS/05 Knowledge Management/Reports",
            "02 - AREAS/06 Society & Culture",
            "03 - RESOURCES",
        ]
        
        for dir_path in dirs:
            (self.vault_root / dir_path).mkdir(parents=True, exist_ok=True)
        
        print("✅ Directories created")
    
    def find_source_links(self, file_path: Path) -> Set[str]:
        """Find all wiki links in a file."""
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
            # Find [[...]] links
            links = set(re.findall(r'\[\[([^\]]+)\]\]', content))
            return links
        except:
            return set()
    
    def update_file_links(self, file_path: Path, old_name: str, new_name: str) -> None:
        """Update links in a file when target is moved."""
        try:
            content = file_path.read_text(encoding='utf-8', errors='ignore')
            
            # Find all references to the old file name
            old_base = old_name.replace('.md', '')
            new_base = new_name.replace('.md', '')
            
            # Update [[old_name]] to [[new_name]]
            updated_content = re.sub(
                rf'\[\[{re.escape(old_base)}\]\]',
                f'[[{new_base}]]',
                content
            )
            
            # Update [[old_name|...]] to [[new_name|...]]
            updated_content = re.sub(
                rf'\[\[{re.escape(old_base)}\|([^\]]+)\]\]',
                rf'[[{new_base}|\1]]',
                updated_content
            )
            
            if content != updated_content:
                file_path.write_text(updated_content, encoding='utf-8')
                print(f"  📝 Updated links in {file_path.name}")
                
        except Exception as e:
            self.errors.append(f"Error updating links in {file_path}: {e}")
    
    def execute_migration(self) -> None:
        """Execute the migration plan."""
        print("\n🚚 Executing migration...")
        
        # First pass: move files
        moves_completed = []
        for source, dest in self.migration_plan.items():
            try:
                # Handle filename collisions
                if dest.exists():
                    base = dest.stem
                    ext = dest.suffix
                    counter = 1
                    while dest.exists():
                        dest = dest.parent / f"{base}_{counter}{ext}"
                        counter += 1
                
                # Create parent dir if needed
                dest.parent.mkdir(parents=True, exist_ok=True)
                
                # Move file
                shutil.move(str(source), str(dest))
                moves_completed.append((source, dest))
                self.moved_count += 1
                
                if self.moved_count % 10 == 0:
                    print(f"  ✅ Moved {self.moved_count} files...")
                    
            except Exception as e:
                self.errors.append(f"Failed to move {source} -> {dest}: {e}")
        
        print(f"✅ Moved {self.moved_count} files")
        
        # Second pass: update cross-links
        print("\n🔗 Updating cross-links...")
        for old_path, new_path in moves_completed:
            old_name = old_path.name
            new_name = new_path.name
            
            if old_name != new_name:
                # Update all references to this file
                for md_file in self.vault_root.rglob("*.md"):
                    # Skip system folders
                    if any(ex in str(md_file) for ex in ['.smart-env', '.obsidian', '.git']):
                        continue
                    self.update_file_links(md_file, old_name, new_name)
        
        print("✅ Cross-links updated")
    
    def create_related_links_section(self) -> None:
        """Add 'Related Links' section to key files."""
        print("\n🔗 Creating related links sections...")
        
        related_files = [
            # Philosophy cluster
            ("02 - AREAS/01 Philosophy & Religion/", [
                "Nagarjuna_Charvaka_vs_Shankara_Cage_Match",
                "Shankara_vs_Greek_Philosophers_Showdown", 
                "Shankara_vs_Chinese_Philosophers_Showdown",
                "Charvaka_Materialism_Analysis",
                "Ambedkar_Buddhism_Choice_Analysis",
            ]),
            # Buddhism cluster
            ("02 - AREAS/01 Philosophy & Religion/Buddhism/", [
                "00_BUDDHA_RESEARCH_HUB",
                "IVC_Sramana_Deep_Research_Report",
                "IVC_Shramana_Buddhism_Jainism_Comparison",
            ]),
        ]
        
        for folder, files in related_files:
            folder_path = self.vault_root / folder
            if not folder_path.exists():
                continue
                
            for file_pattern in files:
                matching_files = list(folder_path.glob(f"*{file_pattern}*"))
                if matching_files:
                    file_path = matching_files[0]
                    try:
                        content = file_path.read_text(encoding='utf-8', errors='ignore')
                        
                        # Check if already has related links
                        if "## Related" in content or "## Links" in content:
                            continue
                        
                        # Find other files to link to
                        other_files = [f for f in matching_files if f != file_path]
                        if other_files:
                            related_section = "\n\n## 🔗 Related\n\n"
                            for other in other_files[:5]:  # Top 5 related
                                name = other.stem
                                related_section += f"- [[{name}]]\n"
                            
                            # Append to file
                            file_path.write_text(content + related_section, encoding='utf-8')
                            print(f"  ✨ Added related links to {file_path.name}")
                    except Exception as e:
                        self.errors.append(f"Error adding links to {file_path}: {e}")
        
        print("✅ Related links created")
    
    def generate_migration_report(self) -> None:
        """Generate final migration report."""
        report_path = self.vault_root / "VAULT_MIGRATION_REPORT.md"
        
        report = f"""# Vault Migration Report

**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Status:** {'✅ Complete' if not self.errors else '⚠️ Completed with errors'}

## Summary

| Metric | Value |
|--------|-------|
| Files Moved | {self.moved_count} |
| Errors | {len(self.errors)} |

## File Migrations

"""
        
        for source, dest in self.migration_plan.items():
            rel_source = source.relative_to(self.vault_root)
            rel_dest = dest.relative_to(self.vault_root)
            report += f"- `{rel_source}` → `{rel_dest}`\n"
        
        if self.errors:
            report += "\n## Errors\n\n"
            for error in self.errors:
                report += f"- ⚠️ {error}\n"
        
        report_path.write_text(report, encoding='utf-8')
        print(f"\n📄 Migration report saved: {report_path}")
    
    def run(self) -> None:
        """Run the full migration."""
        print("="*60)
        print("🔄 VAULT FILE MIGRATION")
        print("="*60)
        
        # Step 1: Scan files
        files = self.scan_all_files()
        
        # Step 2: Build plan
        self.build_migration_plan(files)
        
        # Step 3: Create directories
        self.create_missing_directories()
        
        # Step 4: Execute migration
        self.execute_migration()
        
        # Step 5: Create related links
        self.create_related_links_section()
        
        # Step 6: Generate report
        self.generate_migration_report()
        
        print("="*60)
        print("✅ MIGRATION COMPLETE!")
        print("="*60)
        print(f"\n📦 {self.moved_count} files reorganized")
        print(f"🔗 Cross-links updated across vault")
        print(f"📄 Report: VAULT_MIGRATION_REPORT.md")

if __name__ == "__main__":
    migrator = VaultMigrator(VAULT_ROOT)
    migrator.run()
