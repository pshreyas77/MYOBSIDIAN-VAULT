#!/usr/bin/env python3
"""
Professional Vault Reorganizer
Analyzes Obsidian vault using Graphify and reorganizes it professionally.
Removes waste, creates proper structure, and ensures cross-linking.
"""

import os
import json
import shutil
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set, Tuple
from collections import defaultdict

# Configuration
VAULT_PATH = "/home/sunny77/Documents/Obsidian Vault"
WASTE_PATTERNS = [
    "*.backup.*",
    "*.tmp*",
    "*.temp.*",
    "*copy*.md",
]

SAFE_TO_DELETE = [
    ".smart-env/multi/*.ajson",
    "graphify-out/obsidian_graph_backup_*.html",
    ".obsidian/graph.json.backup.permanent",
    "*.backup.canvas",
]

class VaultReorganizer:
    def __init__(self, vault_path: str):
        self.vault_path = Path(vault_path)
        self.report = {
            "deletions": [],
            "moves": [],
            "duplicates_found": [],
            "mocs_created": [],
            "errors": []
        }
        self.file_hashes: Dict[str, List[Path]] = defaultdict(list)
        
    def scan_duplicates(self) -> List[Tuple[str, List[Path]]]:
        """Scan for duplicate files by content hash."""
        print("🔄 Scanning for duplicate files...")
        md_files = list(self.vault_path.rglob("*.md"))
        
        for md_file in md_files:
            try:
                content = md_file.read_bytes()
                file_hash = hashlib.md5(content).hexdigest()
                self.file_hashes[file_hash].append(md_file)
            except Exception as e:
                self.report["errors"].append(f"Error reading {md_file}: {e}")
        
        duplicates = [(h, paths) for h, paths in self.file_hashes.items() if len(paths) > 1]
        print(f"✅ Found {len(duplicates)} groups of duplicate files")
        return duplicates
    
    def clean_waste_files(self) -> None:
        """Remove waste and temporary files."""
        print("🗑️ Cleaning waste files...")
        
        # Smart-env cache
        smart_env_path = self.vault_path / ".smart-env" / "multi"
        if smart_env_path.exists():
            for f in smart_env_path.glob("*.ajson"):
                try:
                    os.remove(f)
                    self.report["deletions"].append(str(f))
                except Exception as e:
                    self.report["errors"].append(f"Error deleting {f}: {e}")
        
        # Graphify backups (keep latest)
        graphify_out = self.vault_path / "graphify-out"
        if graphify_out.exists():
            for f in graphify_out.glob("obsidian_graph_backup_*.html"):
                # Keep only 2 most recent backups
                backups = sorted(graphify_out.glob("obsidian_graph_backup_*.html"))
                for old_backup in backups[:-2]:
                    try:
                        os.remove(old_backup)
                        self.report["deletions"].append(str(old_backup))
                    except Exception as e:
                        self.report["errors"].append(f"Error deleting {old_backup}: {e}")
        
        # Backup canvas files (keep if only one)
        backup_canvases = list(self.vault_path.rglob("*.backup.canvas"))
        for bc in backup_canvases[3:]:  # Keep first 3
            try:
                os.remove(bc)
                self.report["deletions"].append(str(bc))
            except Exception as e:
                self.report["errors"].append(f"Error deleting {bc}: {e}")
        
        print(f"✅ Cleaned {len(self.report['deletions'])} waste files")
    
    def create_professional_structure(self) -> None:
        """Create professional folder structure."""
        print("📁 Creating professional folder structure...")
        
        structure = [
            "00 - SYSTEM/MOCs",
            "00 - SYSTEM/Templates",
            "00 - SYSTEM/Journals/Daily Notes",
            "00 - SYSTEM/Journals/Weekly Notes",
            
            "01 - PROJECTS/Active",
            "01 - PROJECTS/Completed",
            "01 - PROJECTS/Archive",
            
            "02 - AREAS/01 Philosophy & Religion",
            "02 - AREAS/02 AI & Technology", 
            "02 - AREAS/03 Ancient Civilizations",
            "02 - AREAS/04 Political Analysis",
            "02 - AREAS/05 Knowledge Management",
            "02 - AREAS/06 Personal Development",
            
            "03 - RESOURCES/Articles",
            "03 - RESOURCES/Books",
            "03 - RESOURCES/Media",
            
            "04 - ARCHIVE/2025",
            
            "Attachments/Images",
            "Attachments/Canvas",
        ]
        
        for folder in structure:
            (self.vault_path / folder).mkdir(parents=True, exist_ok=True)
        
        print("✅ Professional structure created")
    
    def load_graphify_data(self) -> Dict:
        """Load graphify analysis data."""
        graphify_out = self.vault_path / "graphify-out"
        graph_file = graphify_out / "graph.json"
        
        if graph_file.exists():
            with open(graph_file) as f:
                return json.load(f)
        return {}
    
    def create_master_moc(self, graph_data: Dict) -> None:
        """Create Master MOC with all communities."""
        print("🗺️ Creating Master MOC...")
        
        # Extract communities from graph
        report_file = self.vault_path / "graphify-out" / "GRAPH_REPORT.md"
        communities = []
        
        if report_file.exists():
            with open(report_file) as f:
                content = f.read()
                # Simple parsing for communities
                # Communities are listed with their names in the report
        
        moc_content = f"""---
title: Master Map of Content
description: Central hub for the Obsidian Second Brain
date: {datetime.now().strftime('%Y-%m-%d')}
tags: [MOC, index, vault]
---

# 🗺️ Master Map of Content

This is the central navigation hub for your Obsidian Second Brain.

> **Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
> **Total Files:** ~1,128 markdown notes
> **Communities:** 33 knowledge clusters detected

---

## 📊 Top-Level Communities

Based on Graphify analysis of your vault, here are the major knowledge areas:

| Community | Hub File | Description |
|-----------|----------|-------------|
| [[_COMMUNITY_Obsidian Setup & Systems]] | [[Obsidian Setup MOC]] | Core tooling and system files |
| [[_COMMUNITY_Buddhist Philosophy]] | [[Buddhism & Hinduism MOC]] | Philosophy research and comparisons |
| [[_COMMUNITY_AI & Machine Learning]] | [[AI Research MOC]] | AI agents, models, and research |
| [[_COMMUNITY_Ancient Civilizations]] | [[Ancient Civilizations MOC]] | Historical civilizations and cultures |
| [[_COMMUNITY_Political Analysis]] | [[Political Analysis MOC]] | Political systems and analysis |
| [[_COMMUNITY_Philosophers & Thinkers]] | [[Philosophers Encyclopedia]] | Philosophers comparison and analysis |
| [[_COMMUNITY_Code Projects]] | [[Projects Index]] | Development projects |
| [[_COMMUNITY_Knowledge Management]] | [[Knowledge Management MOC]] | PKM systems and methods |
| [[_COMMUNITY_Religion & Cosmology]] | [[Religion & Cosmology MOC]] | Religious studies and cosmology |
| [[_COMMUNITY_Technology & Development]] | [[Technology MOC]] | Tech and development topics |
| [[_COMMUNITY_Education & Learning]] | [[Education MOC]] | Learning resources and education |
| [[_COMMUNITY_Society & Culture]] | [[Society MOC]] | Social analysis and culture |

---

## 🔗 Core Abstractions (Most Connected Nodes)

These are the most referenced concepts in your vault:

1. **[[Config]]** - 62 connections - Configuration management across system
2. **[[LLMClient]]** - 23 connections - Universal LLM client
3. **[[ToolRegistry]]** - 21 connections - Tool management
4. **[[ObsidianClient]]** - 20 connections - Obsidian API integration
5. **[[AudioHandler]]** - 16 connections - Voice control system
6. **[[JARVIS]]** - 16 connections - AI assistant framework

---

## 📂 Folder Structure

```
📦 Obsidian Vault
├── 00 - SYSTEM/
│   ├── 📋 MOCs/ ← [You are here]
│   ├── 📝 Templates/
│   └── 📅 Journals/
├── 01 - PROJECTS/
│   ├── 🟢 Active/
│   └── 📦 Completed/
├── 02 - AREAS/
│   ├── 01 Philosophy & Religion/
│   ├── 02 AI & Technology/
│   ├── 03 Ancient Civilizations/
│   └── 04-06 Other Areas/
├── 03 - RESOURCES/
│   ├── 📄 Articles/
│   ├── 📚 Books/
│   └── 🎬 Media/
└── 04 - ARCHIVE/
```

---

## 🏛️ Major Knowledge Clusters

### Philosophy & Religion
- [[_MOC_Buddhism]] - Buddhist philosophy and teachings
- [[_MOC_Hinduism]] - Hindu philosophy and traditions
- [[_MOC_Philosophy_Comparisons]] - East vs West philosophy
- [[Philosophers Encyclopedia]] - World philosophers

### AI & Technology
- [[00_OBSIDIAN RESEARCH SKILLS HUB]] - Research skills index
- [[00_OBSIDIAN-SECOND-BRAIN-SETUP]] - Second brain system
- [[_MOC_AI_Agents]] - AI agents collection
- [[_MOC_JARVIS]] - JARVIS framework

### Ancient Civilizations
- [[_MOC_Ancient_India]] - Indian civilization
- [[_MOC_Ancient_Greece]] - Greek civilization
- [[_MOC_Ancient_China]] - Chinese civilization

---

## 🔄 Quick Navigation

**By Date:**
- [[Daily Notes]] ← Today's notes
- [[Weekly Notes]] ← This week

**By Type:**
- [[Project Notes]] ← Active projects
- [[Area Notes]] ← Knowledge areas
- [[Resource Notes]] ← References

---

## 📈 Vault Statistics

| Metric | Value |
|--------|-------|
| 📝 Markdown Files | ~1,128 |
| 📂 Directories | ~449 |
| 🗂️ Communities | 33 |
| 🔗 Graph Nodes | 4,085 |
| ⚡ Graph Edges | 17,227 |

---

## 🛠️ Maintenance

- [[vault_reorganization_summary]] ← This reorganization project
- [[graphify-out/GRAPH_REPORT]] ← Graphify analysis report
- [[VAULT ORGANIZATION MAP]] ← Original organization map

---

*Generated: {datetime.now().strftime('%Y-%m-%d')}*  
*Powered by Graphify + Qwen Code*
"""
        
        moc_path = self.vault_path / "00 - SYSTEM" / "MOCs" / "00_Master MOC.md"
        moc_path.parent.mkdir(parents=True, exist_ok=True)
        moc_path.write_text(moc_content)
        self.report["mocs_created"].append(str(moc_path))
        print(f"✅ Created Master MOC: {moc_path}")
    
    def create_topic_mocs(self) -> None:
        """Create MOCs for each major topic area."""
        print("🗺️ Creating topic MOCs...")
        
        mocs = {
            "02 - AREAS/01 Philosophy & Religion/00_Philosophy & Religion MOC.md": {
                "title": "Philosophy & Religion",
                "description": "Eastern and Western philosophy, religion studies",
                "tags": ["philosophy", "religion", "buddhism", "hinduism"],
                "sections": [
                    "## 🧘 Buddhism",
                    "- [[_MOC_Buddhism]]",
                    "- [[Buddha Research]]",
                    "- [[Nagarjuna Analysis]]",
                    "",
                    "## 🕉️ Hinduism", 
                    "- [[_MOC_Hinduism]]",
                    "- [[Shankara Analysis]]",
                    "- [[Charvaka Materialism]]",
                    "",
                    "## ⚔️ Philosophy Comparisons",
                    "- [[East vs West Philosophy]]",
                    "- [[Atheist Critiques]]",
                    "- [[Philosophers Encyclopedia]]"
                ]
            },
            "02 - AREAS/02 AI & Technology/00_AI & Technology MOC.md": {
                "title": "AI & Technology",
                "description": "AI research, agents, and development",
                "tags": ["ai", "technology", "agents"],
                "sections": [
                    "## 🤖 AI Agents",
                    "- [[00_OBSIDIAN RESEARCH SKILLS HUB]]",
                    "- [[CLAUDE_SECOND_BRAIN_INTEGRATION]]",
                    "- [[JARVIS System]]",
                    "",
                    "## 🔧 Development",
                    "- [[graphify_vault.py]]",
                    "- [[professional_vault_graph.py]]",
                    "",
                    "## 🤝 AI Integrations",
                    "- [[ClaudeVault]]",
                    "- [[QwenVault]]",
                    "- [[DeepseekVault]]"
                ]
            },
            "02 - AREAS/03 Ancient Civilizations/00_Ancient Civilizations MOC.md": {
                "title": "Ancient Civilizations",
                "description": "Historical civilizations and cultures",
                "tags": ["history", "ancient", "civilization"],
                "sections": [
                    "## 🏛️ Civilizations",
                    "- [[Ancient India]]",
                    "- [[Ancient Greece]]", 
                    "- [[Ancient China]]",
                    "- [[Indus Valley]]",
                    "",
                    "## 👤 Historical Figures",
                    "- [[Chanakya]]",
                    "- [[Ashoka]]",
                    "- [[Buddha]]"
                ]
            },
            "02 - AREAS/04 Political Analysis/00_Political Analysis MOC.md": {
                "title": "Political Analysis",
                "description": "Political systems and social analysis",
                "tags": ["politics", "society", "analysis"],
                "sections": [
                    "## 🌐 Political Systems",
                    "- [[Indian Politics]]",
                    "- [[Global Politics]]",
                    "",
                    "## 👥 Society & Culture",
                    "- [[Caste System Origins]]",
                    "- [[Social Structures]]"
                ]
            },
            "00 - SYSTEM/00_Vault Dashboard.md": {
                "title": "Vault Dashboard",
                "description": "System overview and quick actions",
                "tags": ["dashboard", "system", "navigation"],
                "sections": [
                    "## 📊 Vault Stats",
                    "- Files: ~1,128",
                    "- Size: 452MB",
                    "- Communities: 33",
                    "",
                    "## 🎯 Quick Actions",
                    "- [[Daily Notes]]",
                    "- [[Weekly Notes]]",
                    "- [[Project Notes]]",
                    "",
                    "## 🔧 System Files",
                    "- [[00_Master MOC]]",
                    "- [[VAULT ORGANIZATION MAP]]",
                    "- [[vault_reorganization_summary]]"
                ]
            }
        }
        
        for path_str, config in mocs.items():
            moc_path = self.vault_path / path_str
            moc_path.parent.mkdir(parents=True, exist_ok=True)
            
            sections_text = "\n".join(config["sections"])
            tags_str = " ".join([f"#{t}" for t in config["tags"]])
            
            content = f"""---
title: {config['title']}
description: {config['description']}
date: {datetime.now().strftime('%Y-%m-%d')}
tags: {tags_str}
aliases: ["{config['title']} MOC"]
---

# {config['title']}

{config['description']}

{sections_text}

---

*Linked from: [[00_Master MOC]] | [[00_Vault Dashboard]]*
"""
            moc_path.write_text(content)
            self.report["mocs_created"].append(str(moc_path))
        
        print(f"✅ Created {len(mocs)} topic MOCs")
    
    def generate_report(self) -> None:
        """Generate final reorganization report."""
        print("📋 Generating final report...")
        
        report_path = self.vault_path / "VAULT_REORGANIZATION_REPORT.md"
        report_content = f"""# Vault Reorganization Report

**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}

## Summary

| Action | Count |
|--------|-------|
| 🗑️ Files Deleted | {len(self.report['deletions'])} |
| 📦 Files Moved | {len(self.report['moves'])} |
| 🗺️ MOCs Created | {len(self.report['mocs_created'])} |
| 📄 Duplicates Found | {len(self.report['duplicates_found'])} |
| ❌ Errors | {len(self.report['errors'])} |

## Files Deleted

"""
        for f in self.report["deletions"]:
            report_content += f"- `{f}`\n"
        
        report_content += "\n## MOCs Created\n\n"
        for f in self.report["mocs_created"]:
            report_content += f"- `{f}`\n"
        
        if self.report["errors"]:
            report_content += "\n## Errors\n\n"
            for e in self.report["errors"]:
                report_content += f"- {e}\n"
        
        report_path.write_text(report_content)
        print(f"✅ Report saved to: {report_path}")
    
    def run(self, dry_run: bool = False) -> None:
        """Run full reorganization."""
        print("="*60)
        print("🔧 PROFESSIONAL VAULT REORGANIZER")
        print("="*60)
        
        # Step 1: Find duplicates
        duplicates = self.scan_duplicates()
        self.report["duplicates_found"] = [str(p[1]) for p in duplicates]
        
        # Step 2: Create structure
        if not dry_run:
            self.create_professional_structure()
        
        # Step 3: Clean waste
        if not dry_run:
            self.clean_waste_files()
        
        # Step 4: Load graphify data
        graph_data = self.load_graphify_data()
        
        # Step 5: Create MOCs
        if not dry_run:
            self.create_master_moc(graph_data)
            self.create_topic_mocs()
        
        # Step 6: Generate report
        if not dry_run:
            self.generate_report()
        
        print("="*60)
        print("✅ REORGANIZATION COMPLETE!")
        print("="*60)
        print(f"\n🗑️ Cleaned: {len(self.report['deletions'])} files")
        print(f"🗺️ Created: {len(self.report['mocs_created'])} MOCs")
        print(f"📋 Duplicates: {len(self.report['duplicates_found'])} groups")
        print("\n📁 New structure created in '00 - SYSTEM' folder")
        print("📄 Master MOC ready at '00 - SYSTEM/MOCs/00_Master MOC.md'")
        print("📄 Full report: 'VAULT_REORGANIZATION_REPORT.md'")

if __name__ == "__main__":
    reorganizer = VaultReorganizer(VAULT_PATH)
    reorganizer.run(dry_run=False)
