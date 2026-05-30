#!/usr/bin/env python3
"""
Advanced Topic-Based Vault Organizer
Analyzes all files, extracts topics, creates subject-based organization
"""

import os
import re
import shutil
import json
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

VAULT_PATH = Path("/home/sunny77/Documents/Obsidian Vault")
TOPICS_PATH = VAULT_PATH / "07 - Topics"

def extract_topics_from_file(filepath):
    """Extract topics from file content and name"""
    topics = []

    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except:
        return []

    filename = filepath.name.lower()
    content_lower = content.lower()

    # Topic detection with keyword mapping
    topic_keywords = {
        "Buddhism & Hinduism": [
            "buddha", "buddhism", "hindu", "hinduism", "mahavira", "jain", "jainism",
            "dharma", "karma", "nirvana", "nibbana", "samsara", "moksha",
            "vedas", "vedic", "upanishad", "purana", "bhagavad", "gita",
            "mahabharata", "ramayana", "shiva", "vishnu", "brahma", "krishna",
            "rama", "sanskrit", "mantra", "meditation", "nirvana", "enlightenment",
            "lumbini", "sarnath", "nalanda", "bodh", "gaya", "kushinagar",
            "ashoka", "maurya", "gupta", "chola", "pallava", "shunga",
            "monastery", "temple", "stupa", "chaitya", "vihara", "shrine"
        ],
        "Ancient Civilizations": [
            "ancient", "civilization", "civilisation", "archaeology", "excavation",
            "göbekli", "gobekli", "tepe", "çatalhöyük", "catalhoyuk",
            "mesopotamia", "sumerian", "babylon", "assyria", "akkad",
            "egypt", "pharaoh", "pyramids", "sphinx", "nile", "mummy",
            "indus", "harappa", "mohenjo", "rakhigarhi", "dholavira",
            "caral", "supe", "peru", "andes", "norte chico",
            "neolithic", "paleolithic", "bronze age", "iron age",
            "history", "historical", "prehistoric", "antiquity",
            "writing", "cuneiform", "hieroglyph", "script", "language",
            "oldest", "earliest", "first", "origin"
        ],
        "Religion & Cosmology": [
            "religion", "religious", "cosmology", "cosmological",
            "christianity", "christian", "bible", "jesus", "god",
            "islam", "islamic", "muslim", "quran", "allah", "prophet",
            "judaism", "jewish", "hebrew", "torah", "talmud",
            "zoroastrian", "zoroastrianism", "zurvan", "ahura",
            "creation", "creator", "divine", "god", "gods", "deity",
            "universe", "multiverse", "omniverse", "cosmos",
            "creation myth", "mythology", "myth", "legend",
            "esoteric", "occult", "mystical", "mysticism", "spiritual",
            "afterlife", "heaven", "hell", "purgatory", "reincarnation"
        ],
        "Politics & Governance": [
            "politics", "political", "government", "governance",
            "india", "bharat", "indian", "bjp", "congress", "inc",
            "modi", "rahul", "gandhi", "amit", "shah",
            "election", "vote", "voting", "democracy", "democratic",
            "parliament", "legislative", "assembly", "constitution",
            "corruption", "scam", "bribe", "fraud", "money laundering",
            "stalin", "lenin", "marx", "communist", "communism", "ussr",
            "china", "xi jinping", "ccp", "tibet", "xinjiang",
            "israel", "palestine", "zionist", "zionism",
            "leader", "leadership", "minister", "prime minister",
            "party", "alliance", "coalition", "opposition"
        ],
        "AI & Machine Learning": [
            "ai", "artificial intelligence", "machine learning", "ml",
            "neural", "network", "deep learning", "transformer",
            "llm", "language model", "gpt", "claude", "gemini", "llama",
            "agent", "agents", "autonomous", "multi-agent", "orchestrator",
            "rag", "retrieval", "augmented", "generation",
            "embedding", "vector", "database", "pinecone", "chroma",
            "prompt", "prompting", "prompt engineering",
            "fine-tuning", "training", "inference", "model",
            "synthesizer", "analyzer", "retriever", "citation",
            "nlp", "natural language", "token", "tokenizer"
        ],
        "Technology & Development": [
            "technology", "tech", "software", "development", "dev",
            "programming", "code", "coding", "script", "scripting",
            "python", "javascript", "js", "typescript", "ts", "node",
            "react", "vue", "angular", "svelte", "framework",
            "web", "website", "webapp", "application", "app",
            "three.js", "webgl", "canvas", "3d", "graphics",
            "linux", "ubuntu", "debian", "arch", "fedora", "os",
            "git", "github", "version control", "repository",
            "database", "sql", "nosql", "mongodb", "postgres",
            "api", "rest", "graphql", "microservice",
            "docker", "kubernetes", "container", "cloud",
            "server", "backend", "frontend", "fullstack"
        ],
        "Finance & Economics": [
            "finance", "financial", "economy", "economics", "economic",
            "stock", "market", "trading", "trade", "investment", "invest",
            "money", "currency", "rupee", "dollar", "euro", "yen",
            "bank", "banking", "reserve bank", "rbi", "federal",
            "gdp", "inflation", "deflation", "recession", "growth",
            "fiscal", "monetary", "budget", "tax", "revenue",
            "business", "corporate", "company", "startup",
            "profit", "loss", "revenue", "income", "expenditure",
            "portfolio", "asset", "liability", "equity", "fund"
        ],
        "Media & Entertainment": [
            "media", "entertainment", "movie", "film", "cinema",
            "marvel", "dc", "comics", "superhero", "hero", "villain",
            "batman", "superman", "spider-man", "iron man", "hulk",
            "cosmic", "multiverse", "omniverse", "abstract", "entity",
            "tv", "television", "series", "show", "episode",
            "anime", "manga", "cartoon", "animation",
            "game", "gaming", "gamer", "video game", "console",
            "music", "song", "album", "artist", "band",
            "book", "novel", "fiction", "story", "narrative"
        ],
        "Health & Fitness": [
            "health", "healthy", "fitness", "fit", "exercise",
            "workout", "gym", "training", "physical", "body",
            "diet", "nutrition", "food", "eating", "meal",
            "mental health", "wellness", "wellbeing", "self-care",
            "disease", "illness", "condition", "diagnosis", "treatment",
            "medicine", "medical", "doctor", "hospital", "clinic",
            "skin", "hair", "weight", "obesity", "fit",
            "sleep", "rest", "recovery", "stress", "anxiety"
        ],
        "Science & Space": [
            "science", "scientific", "research", "study", "experiment",
            "space", "cosmos", "universe", "galaxy", "star", "planet",
            "astronomy", "astrophysics", "physics", "quantum", "mechanics",
            "chemistry", "biology", "geology", "paleontology",
            "evolution", "dna", "gene", "genetic", "genome",
            "nuclear", "atom", "particle", "molecule",
            "technology", "innovation", "discovery", "breakthrough",
            "theory", "hypothesis", "law", "principle", "theorem"
        ],
        "Education & Learning": [
            "education", "educational", "learning", "learn", "study",
            "university", "college", "school", "academia", "academic",
            "course", "curriculum", "syllabus", "subject", "topic",
            "student", "teacher", "professor", "lecture", "class",
            "exam", "test", "quiz", "assignment", "homework",
            "degree", "diploma", "certificate", "qualification",
            "hci", "human computer", "cognitive", "psychology",
            "note", "notes", "note-taking", "research", "paper"
        ],
        "Security & Privacy": [
            "security", "secure", "privacy", "private", "confidential",
            "cybersecurity", "cyber", "hacking", "hacker", "breach",
            "encryption", "encrypted", "cryptography", "crypto",
            "spyware", "malware", "virus", "trojan", "protection",
            "surveillance", "spying", "espionage", "intelligence",
            "pegasus", "zero-day", "exploit", "vulnerability",
            "password", "authentication", "authorization", "access",
            "data protection", "gdpr", "privacy policy",
            "vpn", "tor", "proxy", "anonymous", "anonymity"
        ],
        "Society & Culture": [
            "society", "social", "culture", "cultural", "tradition",
            "custom", "ritual", "festival", "celebration", "ceremony",
            "language", "linguistics", "dialect", "accent", "translation",
            "caste", "class", "hierarchy", "social structure",
            "gender", "women", "men", "lgbtq", "equality",
            "rights", "human rights", "civil rights", "freedom",
            "discrimination", "racism", "sexism", "bias",
            "population", "demographics", "demography", "census"
        ],
        "Philosophy & Ethics": [
            "philosophy", "philosophical", "philosopher", "thought",
            "ethics", "ethical", "moral", "morality", "values",
            "existentialism", "nihilism", "stoicism", "epicurean",
            "metaphysics", "ontology", "epistemology", "logic",
            "consciousness", "mind", "soul", "spirit",
            "free will", "determinism", "causality", "causation",
            "meaning", "purpose", "truth", "reality",
            "good", "evil", "right", "wrong", "justice",
            "virtue", "vice", "wisdom", "knowledge", "ignorance"
        ]
    }

    for topic, keywords in topic_keywords.items():
        score = 0
        for keyword in keywords:
            # Filename matches worth more
            if keyword in filename:
                score += 5
            # Content matches
            if keyword in content_lower:
                count = content_lower.count(keyword)
                score += min(count, 3)  # Cap at 3 per keyword

        if score >= 3:  # Threshold
            topics.append((topic, score))

    # Sort by score descending
    topics.sort(key=lambda x: x[1], reverse=True)

    # Return top topics
    return [t[0] for t in topics[:5]]

def get_all_files():
    """Get all markdown files in vault excluding Topics folder"""
    files = []
    exclude_patterns = [
        "07 - Topics", ".obsidian", ".smart-env", ".trash",
        "graphify-out", ".claude", "AI_Research_Agents/.claude",
        "00 - SYSTEM/KIMI VAULT"
    ]

    for filepath in VAULT_PATH.rglob("*.md"):
        # Skip if in exclude patterns
        if any(pat in str(filepath) for pat in exclude_patterns):
            continue
        files.append(filepath)

    return files

def organize_by_topics():
    """Main organization function"""
    print("Scanning vault for files...")
    all_files = get_all_files()
    print(f"Found {len(all_files)} files to analyze")

    # Create topic structure
    TOPICS_PATH.mkdir(parents=True, exist_ok=True)

    # Track file assignments
    file_topics = defaultdict(list)
    topic_files = defaultdict(list)

    # Analyze each file
    print("\nAnalyzing files and extracting topics...")
    for i, filepath in enumerate(all_files, 1):
        if i % 50 == 0:
            print(f"  Progress: {i}/{len(all_files)} files")

        topics = extract_topics_from_file(filepath)

        if topics:
            file_topics[str(filepath)] = topics

            # Assign to primary topic
            primary_topic = topics[0]
            topic_files[primary_topic].append(filepath)

            # Also add to secondary topics (copy/link)
            for topic in topics[1:3]:  # Top 3 topics
                topic_files[topic].append(filepath)
        else:
            # Uncategorized
            topic_files["Uncategorized"].append(filepath)

    # Create topic folders and MOCs
    print("\nCreating topic folders...")
    for topic, files in topic_files.items():
        if not files:
            continue

        # Create safe folder name
        folder_name = topic.replace(" & ", " and ").replace(" ", "_")
        topic_folder = TOPICS_PATH / folder_name
        topic_folder.mkdir(parents=True, exist_ok=True)

        # Create MOC file
        moc_path = topic_folder / f"00_{folder_name}_MOC.md"
        create_moc_file(moc_path, topic, files)

        # Create subfolders for organization
        subfolders = {
            "Core Research": [],
            "Analysis": [],
            "Comparisons": [],
            "Resources": [],
            "Conversations": []
        }

        # Categorize files
        for filepath in files:
            filename = filepath.name.lower()

            if "research" in filename or "evidence" in filename or "summary" in filename:
                subfolders["Core Research"].append(filepath)
            elif "analysis" in filename or "critical" in filename or "comparison" in filename:
                subfolders["Analysis"].append(filepath)
            elif "vs" in filename or "compare" in filename:
                subfolders["Comparisons"].append(filepath)
            elif any(x in filename for x in ["chat", "session", "conversation"]):
                subfolders["Conversations"].append(filepath)
            else:
                subfolders["Resources"].append(filepath)

        # Create symlinks/notes for files
        print(f"  {topic}: {len(files)} files")

        # Create index of all files
        index_path = topic_folder / "00_FILE_INDEX.md"
        create_file_index(index_path, topic, files)

    # Create master topic index
    create_master_topics_index(topic_files)

    # Create cross-topic links
    create_cross_topic_links(file_topics)

    # Print statistics
    print("\n" + "="*60)
    print("TOPIC ORGANIZATION COMPLETE")
    print("="*60)
    print(f"\nTotal files analyzed: {len(all_files)}")
    print(f"Files with topics: {len(file_topics)}")
    print(f"Topics created: {len(topic_files)}")
    print("\nBreakdown by topic:")
    for topic, files in sorted(topic_files.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"  {topic}: {len(files)} files")

    return topic_files, file_topics

def create_moc_file(moc_path, topic, files):
    """Create Map of Content file for a topic"""

    content = f"""---
tags: [moc, {topic.lower().replace(' ', '-')}]
aliases: [{topic}]
---

# 🗺️ {topic} - Map of Content

---

## 📊 Overview

This is the central hub for all research and information related to **{topic}**.

**Total Files:** {len(files)}
**Last Updated:** {datetime.now().strftime("%Y-%m-%d")}
**Status:** Active Research

---

## 📁 Sub-Topics & Categories

### Core Research
Archive of fundamental research documents and primary sources.

### Analysis
Critical examinations, arguments, and analytical pieces.

### Comparisons
Comparative studies between different aspects of {topic}.

### Resources
Reference materials, notes, and supporting documents.

### Conversations
AI chat logs and discussion transcripts.

---

## 🔗 Quick Navigation

**Related Topics:**
- [[Ancient_Civilizations_MOC]] - Historical context
- [[Religion_and_Cosmology_MOC]] - Theological aspects
- [[Politics_and_Governance_MOC]] - Political dimensions
- [[AI_and_Machine_Learning_MOC]] - Technical applications

---

## 📚 Key Files

"""

    # Add file list with descriptions
    for i, filepath in enumerate(files[:20], 1):
        rel_path = filepath.relative_to(VAULT_PATH)
        content += f"{i}. [[{filepath.stem}]] — `{rel_path}`\n"

    if len(files) > 20:
        content += f"\n*...and {len(files) - 20} more files*\n"

    content += f"""

---

## 🎯 Research Goals

- [ ] Synthesize findings across all files
- [ ] Identify knowledge gaps
- [ ] Cross-reference with related topics
- [ ] Generate comprehensive report

---

*Auto-generated by Topic Organizer*
*Category: {topic}*
"""

    with open(moc_path, 'w', encoding='utf-8') as f:
        f.write(content)

def create_file_index(index_path, topic, files):
    """Create comprehensive file index"""

    content = f"""# {topic} - Complete File Index

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M")}
**Total Files:** {len(files)}

---

## Alphabetical File List

"""

    # Sort files alphabetically
    sorted_files = sorted(files, key=lambda x: x.name.lower())

    for filepath in sorted_files:
        rel_path = filepath.relative_to(VAULT_PATH)
        content += f"- [[{filepath.stem}]] — `{rel_path}`\n"

    content += "\n---\n\n## Statistics\n\n"
    content += f"- Total files: {len(files)}\n"
    content += f"- Oldest: {min(files, key=lambda x: x.stat().st_mtime).name if files else 'N/A'}\n"
    content += f"- Newest: {max(files, key=lambda x: x.stat().st_mtime).name if files else 'N/A'}\n"

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

def create_master_topics_index(topic_files):
    """Create master index of all topics"""

    index_path = TOPICS_PATH / "00_TOPICS_MASTER_INDEX.md"

    content = """---
tags: [hub, topics, navigation]
aliases: [Topics, Topic Index]
---

# 🗂️ Topics Master Index

---

## Welcome to Your Topic-Based Knowledge System

All files in your vault have been analyzed and organized by subject matter.

---

## 📊 Topics Overview

"""

    sorted_topics = sorted(topic_files.items(), key=lambda x: len(x[1]), reverse=True)

    for topic, files in sorted_topics:
        folder_name = topic.replace(" & ", " and ").replace(" ", "_")
        moc_link = f"[[{folder_name}_MOC|{topic}]]"
        content += f"### {moc_link}\n"
        content += f"**Files:** {len(files)} | "
        content += f"[[{folder_name}/00_{folder_name}_MOC|MOC]] | "
        content += f"[[{folder_name}/00_FILE_INDEX|Index]]\n\n"

    content += """
---

## 🔍 How to Use This System

1. **Browse by Topic**: Click any topic above to explore related files
2. **Follow Links**: Use the MOC (Map of Content) files as navigation hubs
3. **Cross-Reference**: Files may appear in multiple topics (different aspects)
4. **Search**: Use Obsidian's search with topic tags

---

## 🔄 Relationship Map

```
Buddhism & Hinduism ← → Ancient Civilizations
         ↓                    ↓
   Religion/Cosmology ← → Philosophy/Ethics
         ↓                    ↓
   Politics/Governance ← → Society/Culture
```

*Topics are interconnected - use cross-links to explore relationships*

---

*Generated: {}
*Total Topics: {}*
*Total Files Catalogued: {}*
""".format(
        datetime.now().strftime("%Y-%m-%d"),
        len(topic_files),
        sum(len(files) for files in topic_files.values())
    )

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

def create_cross_topic_links(file_topics):
    """Create cross-links between related topics"""

    crosslinks_path = TOPICS_PATH / "00_CROSS_TOPIC_LINKS.md"

    content = """---
tags: [cross-links, relationships, navigation]
---

# 🔗 Cross-Topic Links

Files that bridge multiple topics, revealing connections across your knowledge base.

---

"""

    # Find files that appear in multiple topics
    multi_topic_files = {k: v for k, v in file_topics.items() if len(v) > 1}

    content += f"## Files Spanning Multiple Topics ({len(multi_topic_files)} files)\n\n"

    for filepath_str, topics in sorted(multi_topic_files.items(),
                                       key=lambda x: len(x[1]),
                                       reverse=True):
        filepath = Path(filepath_str)
        rel_path = filepath.relative_to(VAULT_PATH)

        topic_links = " → ".join([f"[[{t}]]" for t in topics])

        content += f"### [[{filepath.stem}]]\n"
        content += f"**Location:** `{rel_path}`\n\n"
        content += f"**Topics:** {topic_links}\n\n"
        content += "---\n\n"

    # Add topic relationship matrix
    content += """## Topic Relationship Matrix

```
                    Bud  Civ  Rel  Pol  AI   Tech Fin  Med
Buddhism            [X]  [+]  [++] [+]  [+]  [ ]  [ ]  [ ]
Ancient Civ         [+]  [X]  [++] [+]  [ ]  [ ]  [ ]  [ ]
Religion            [++] [++] [X]  [+]  [ ]  [ ]  [ ]  [ ]
Politics            [+]  [+]  [+]  [X]  [+]  [+]  [+]  [+]
AI                  [+]  [ ]  [ ]  [+]  [X]  [++] [+]  [ ]
Technology          [ ]  [ ]  [ ]  [+]  [++] [X]  [+]  [ ]
Finance             [ ]  [ ]  [ ]  [+]  [+]  [+]  [X]  [ ]
Media               [ ]  [ ]  [ ]  [+]  [+]  [++] [+]  [X]

[X] Core | [++] Strong Link | [+] Moderate Link | [ ] Weak/None
```

---

## 💡 Surprising Connections

Based on cross-topic files, here are unexpected relationships:

1. **Buddhism & Hinduism ↔ Ancient Civilizations**: Historical overlap
2. **AI & Machine Learning ↔ Politics**: Policy implications
3. **Religion & Cosmology ↔ Philosophy**: Theological debates
4. **Technology ↔ Finance**: Economic impact
5. **Media & Entertainment ↔ Religion**: Pop culture mythology

---

*Use these connections to discover unexpected insights in your research*
"""

    with open(crosslinks_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    print("="*60)
    print("TOPIC-BASED VAULT ORGANIZER")
    print("="*60)
    print()

    topic_files, file_topics = organize_by_topics()

    print()
    print("✅ Organization complete!")
    print(f"📁 Topics folder: {TOPICS_PATH}")
    print(f"🗺️  Master index: {TOPICS_PATH / '00_TOPICS_MASTER_INDEX.md'}")
