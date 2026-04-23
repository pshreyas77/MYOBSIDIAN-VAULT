#!/usr/bin/env python3
"""
LLM Wiki Ingestion Helper
A simple script to assist with ingesting new sources into the LLM Wiki second brain system.
"""

import os
import sys
import datetime
import json
from pathlib import Path

def get_vault_path():
    """Get the Obsidian vault path"""
    return Path("/home/sunny77/Documents/Obsidian Vault")

def get_wiki_path():
    """Get the wiki path"""
    return get_vault_path() / "wiki"

def get_templates_path():
    """Get the templates path"""
    return get_wiki_path() / "_templates"

def get_index_path():
    """Get the index file path"""
    return get_wiki_path() / "index.md"

def get_log_path():
    """Get the log file path"""
    return get_wiki_path() / "log.md"

def create_source_summary(source_path, title=None):
    """Create a source summary page"""
    if title is None:
        title = Path(source_path).stem

    wiki_path = get_wiki_path()
    sources_dir = wiki_path / "sources"
    sources_dir.mkdir(exist_ok=True)

    # Create source filename
    safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()
    safe_title = safe_title.replace(' ', '_')
    source_file = sources_dir / f"{safe_title}.md"

    # Get template
    template_path = get_templates_path() / "source.md"
    if template_path.exists():
        with open(template_path, 'r') as f:
            template = f.read()
    else:
        template = """---
title: [[Source Title]]
type: source
date: {{DATE}}
added: {{DATE}}
source_type: [article/book/podcast/video/etc]
author: [Author Name]
source_path: [[path/to/original]]
entities_mentioned: []
concepts_discussed: []
---

# [[Source Title]]

## Overview
[Brief summary of source]

## Key Takeaways
- Takeaway 1: [Summary with links to [[Entity]]/[[Concept]]]
- Takeaway 2: [Summary with links to [[Entity]]/[[Concept]]]
- ...

## Entities Mentioned
- [[Entity1]] - Role in source
- [[Entity2]] - Role in source

## Concepts Discussed
- [[Concept1]] - How presented
- [[Concept2]] - How presented

## Relevance to Wiki
- Updates/changes to existing understanding
- Contradictions with current knowledge
- New connections suggested

## Personal Notes
[Why this source was added, relevance to goals]

## Last Updated
{{DATE}}
"""

    # Fill template
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    content = template.replace("[[Source Title]]", title)
    content = content.replace("{{DATE}}", now)
    content = content.replace("[Author Name]", "Unknown")
    content = content.replace("[[path/to/original]]", f"[[{source_path}]]")
    content = content.replace("[article/book/podcast/video/etc]", "unknown")

    # Write file
    with open(source_file, 'w') as f:
        f.write(content)

    print(f"Created source summary: {source_file}")
    return source_file

def update_index():
    """Update the wiki index with basic stats"""
    wiki_path = get_wiki_path()
    index_path = get_index_path()

    # Count files
    md_files = list(wiki_path.rglob("*.md"))
    total_pages = len([f for f in md_files if "_templates" not in str(f)])

    # Rough word count (simplified)
    total_words = 0
    for md_file in md_files:
        if "_templates" not in str(md_file):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    total_words += len(content.split())
            except:
                pass

    # Update index
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    index_content = f"""# Wiki Index

## Recently Updated
- [[Wiki Home]] - Main wiki navigation (Updated: {now})

## By Category
### Entities
- [[Config]] - Central configuration hub
- [[LLMClient]] - Your LLM interface layer
- [[ToolRegistry]] - Tool management system
- [[ObsidianClient]] - Obsidian API integration

### Concepts
- [[Second Brain]] - Personal knowledge management system
- [[LLM Wiki]] - LLM-maintained knowledge base pattern
- [[MemPalace]] - Room-based memory organization
- [[Graphify]] - Knowledge graph analysis

### Sources
- [[LLM Wiki Pattern Document]] - One-line summary (Date: {now})

### Comparisons/Analyses

### Statistics
- Total Pages: {total_pages}
- Last Updated: {now}
- Total Words: {total_words:,}
"""

    with open(index_path, 'w') as f:
        f.write(index_content)

    print(f"Updated index: {index_path}")

def log_operation(operation_type, description):
    """Log an operation to the log file"""
    log_path = get_log_path()
    now = datetime.datetime.now().strftime("%Y-%m-%d")

    log_entry = f"""
## [{now}] {operation_type} | {description}
- Operation completed successfully
- Timestamp: {now}
"""

    with open(log_path, 'a') as f:
        f.write(log_entry)

    print(f"Logged operation: {operation_type}")

def main():
    """Main function for command line usage"""
    if len(sys.argv) < 2:
        print("Usage: wiki_ingest_helper.py <command> [args]")
        print("Commands:")
        print("  init          - Initialize wiki system")
        print("  source <file> - Create source summary for file")
        print("  index         - Update wiki index")
        print("  log <type> <desc> - Log an operation")
        return

    command = sys.argv[1]

    if command == "init":
        # Initialize system
        get_wiki_path().mkdir(exist_ok=True)
        get_templates_path().mkdir(exist_ok=True)
        (get_wiki_path() / "sources").mkdir(exist_ok=True)
        (get_wiki_path() / "entities").mkdir(exist_ok=True)
        (get_wiki_path() / "concepts").mkdir(exist_ok=True)
        (get_wiki_path() / "comparisons").mkdir(exist_ok=True)

        update_index()
        log_operation("init", "LLM Wiki system initialized")
        print("LLM Wiki system initialized!")

    elif command == "source":
        if len(sys.argv) < 3:
            print("Please provide a source file path")
            return
        source_path = sys.argv[2]
        title = sys.argv[3] if len(sys.argv) > 3 else None
        create_source_summary(source_path, title)
        log_operation("source", f"Created source summary for {source_path}")

    elif command == "index":
        update_index()
        log_operation("index", "Updated wiki index")

    elif command == "log":
        if len(sys.argv) < 4:
            print("Please provide operation type and description")
            return
        op_type = sys.argv[2]
        desc = sys.argv[3]
        log_operation(op_type, desc)

    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()