#!/usr/bin/env python3
"""
Professional Obsidian Vault Organizer
Uses content analysis to categorize files into PARA structure
"""

import os
import re
import shutil
from pathlib import Path
from collections import defaultdict

VAULT_PATH = Path("/home/sunny77/Documents/Obsidian Vault")

def analyze_file(filepath):
    """Analyze file content and return categories"""
    categories = []

    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read().lower()
            filename = filepath.name.lower()
    except:
        return ['04 - Archive/General']

    # Keyword mapping
    keywords = {
        '02 - Areas/Buddhism & Hinduism': [
            'buddha', 'buddhism', 'hinduism', 'hindu', 'mahavira', 'jainism', 'jain',
            'vedas', 'vedic', 'upanishad', 'bhagavad', 'mahabharata', 'ramayana',
            'sanskrit', 'puja', 'temple', 'monastery', 'lumbini', 'sarnath', 'nalanda',
            'bodhi', 'dharma', 'karma', 'nirvana', 'nibbana', 'samsara', 'mandir'
        ],
        '02 - Areas/Ancient Civilizations': [
            'göbekli', 'gobekli', 'çatalhöyük', 'catalhoyuk', 'mesopotamia', 'sumerian',
            'indus valley', 'harappan', 'mohenjo-daro', 'rakhigarhi', 'caral',
            'egypt', 'pyramids', 'pharaoh', 'ancient', 'civilization', 'archaeology',
            'excavation', 'artefact', 'artifact', 'cuneiform', 'ruins'
        ],
        '02 - Areas/Religion & Cosmology': [
            'cosmology', 'religion', 'theology', 'cosmic', 'multiverse', 'omniverse',
            'christianity', 'islam', 'muslim', 'abrahamic', 'judaism', 'zionism',
            'creation myth', 'eschatology', 'esoteric', 'mystical', 'spiritual'
        ],
        '02 - Areas/Political Analysis': [
            'bjp', 'congress', 'modi', 'gandhi', 'rahul', 'amit', 'shah',
            'politics', 'political', 'election', 'legislative', 'parliament',
            'corruption', 'scam', 'bribe', 'electoral', 'democracy', 'authoritarian',
            'india', 'barat', 'country', 'nation', 'geopolitics', 'foreign policy',
            'stalin', 'lenin', 'marx', 'communist', 'socialism', 'ussr', 'soviet'
        ],
        '02 - Areas/AI Research & Agents': [
            'agent', 'ai', 'artificial intelligence', 'llm', 'model', 'gpt', 'claude',
            'neural', 'deep learning', 'machine learning', 'ml', 'transformer',
            'rag', 'retrieval', 'embedding', 'vector', 'orchestrator', 'synthesizer',
            'analyzer', 'citation', 'fact check', 'research pipeline'
        ],
        '02 - Areas/Technology & Projects': [
            'react', 'javascript', 'python', 'node', 'three.js', 'webgl',
            'website', 'portfolio', 'app', 'application', 'software', 'code',
            'linux', 'os', 'ubuntu', 'feren', 'database', 'server', 'api',
            'docker', 'git', 'github'
        ],
        '02 - Areas/Economics & Finance': [
            'stock', 'market', 'trading', 'invest', 'finance', 'economy', 'gdp',
            'fiscal', 'monetary', 'inflation', 'rupee', 'dollar', 'currency',
            'bank', 'reserve', 'rbi', 'securities', 'nifty', 'sensex'
        ],
        '02 - Areas/Education & Learning': [
            'btech', 'university', 'college', 'academic', 'hci', 'human computer',
            'cognitive', 'learning', 'course', 'education', 'study', 'notes'
        ],
        '03 - Resources/Data & Exports': [
            'index', 'export', 'data', 'csv', 'json', 'graph', 'visualization'
        ],
        '00 - SYSTEM/Templates': [
            'template', 'daily note', 'template'
        ]
    }

    # Check content and filename
    for category, words in keywords.items():
        for word in words:
            if word in content or word in filename:
                if category not in categories:
                    categories.append(category)
                break

    # Cross-category priority rules
    if '02 - Areas/Buddhism & Hinduism' in categories and '02 - Areas/Ancient Civilizations' in categories:
        # Ancient wins if archaeology-related
        if any(k in content for k in ['archaeology', 'excavation', 'temple structure']):
            categories.remove('02 - Areas/Buddhism & Hinduism')

    # Default for uncategorized
    if not categories:
        # Check if it's a conversation export
        if '20' in filename and '-' in filename:
            categories = ['03 - Resources/Data & Exports/AI Conversations']
        elif 'index' in filename or '00_' in filename:
            categories = ['00 - SYSTEM/Dashboard & Navigation']
        else:
            categories = ['03 - Resources/General Research']

    return categories

def safe_move(src, dest_folder):
    """Safely move file with duplicate handling"""
    dest_folder = VAULT_PATH / dest_folder
    dest_folder.mkdir(parents=True, exist_ok=True)

    dest = dest_folder / src.name

    if dest.exists():
        # Add timestamp suffix if duplicate
        stem = src.stem
        suffix = src.suffix
        counter = 1
        while dest.exists():
            dest = dest_folder / f"{stem}_{counter}{suffix}"
            counter += 1

    shutil.move(str(src), str(dest))
    return dest

def organize_vault():
    """Main organization function"""
    stats = defaultdict(int)

    # Move all files from QwenVault
    qwen_path = VAULT_PATH / "QwenVault"
    if qwen_path.exists():
        for file in qwen_path.rglob("*.md"):
            categories = analyze_file(file)
            primary_category = categories[0]
            safe_move(file, primary_category)
            stats[primary_category] += 1

    # Move all files from ClaudeVault
    claude_path = VAULT_PATH / "ClaudeVault"
    if claude_path.exists():
        for file in claude_path.rglob("*.md"):
            # Skip certain system files
            if 'SKILL.md' in file.name:
                continue
            categories = analyze_file(file)
            primary_category = categories[0]
            safe_move(file, primary_category)
            stats[primary_category] += 1

    # Move DeepseekVault
    deepseek_path = VAULT_PATH / "DeepseekVault"
    if deepseek_path.exists():
        for file in deepseek_path.rglob("*.md"):
            categories = analyze_file(file)
            primary_category = categories[0]
            safe_move(file, primary_category)
            stats[primary_category] += 1

    # Move KIWI VAULT (keep structure but move)
    kimi_path = VAULT_PATH / "KIMI VAULT"
    if kimi_path.exists():
        shutil.move(str(kimi_path), str(VAULT_PATH / "00 - SYSTEM/KIMI VAULT"))

    # Print stats
    print("\n=== VAULT ORGANIZATION COMPLETE ===")
    print(f"\nTotal files moved: {sum(stats.values())}")
    print("\nBreakdown by category:")
    for category, count in sorted(stats.items()):
        print(f"  {category}: {count} files")

    return stats

if __name__ == "__main__":
    organize_vault()
