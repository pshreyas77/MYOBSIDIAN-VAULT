#!/usr/bin/env python3
"""
LLM Wiki Lint Helper
A simple script to perform health checks on the LLM Wiki second brain system.
"""

import os
import sys
import datetime
import json
from pathlib import Path
import re

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

def find_orphan_pages():
    """Find wiki pages with no incoming links"""
    wiki_path = get_wiki_path()

    # Get all markdown files (excluding templates)
    all_md_files = list(wiki_path.rglob("*.md"))
    content_files = [f for f in all_md_files if "_templates" not in str(f)]

    # Build a map of page names to files
    page_to_file = {}
    for md_file in content_files:
        # Use the filename without extension as the page name
        page_name = md_file.stem
        page_to_file[page_name] = md_file

    # Find all links in all files
    linked_pages = set()
    link_pattern = r'\[\[([^\]]+)\]\]'

    for md_file in content_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                links = re.findall(link_pattern, content)
                # Clean up links (remove aliases, etc.)
                for link in links:
                    # Handle aliases like [[Page Name|Alias]]
                    clean_link = link.split('|')[0].strip()
                    linked_pages.add(clean_link)
        except Exception as e:
            print(f"Error reading {md_file}: {e}")

    # Find orphan pages (pages that exist but are not linked to)
    orphan_pages = []
    for page_name, file_path in page_to_file.items():
        if page_name not in linked_pages and page_name != "Wiki Home":  # Wiki Home is expected to have fewer links
            orphan_pages.append((page_name, file_path))

    return orphan_pages

def find_stale_claims():
    """Find potential stale claims (simplified - looks for outdated dates or markers)"""
    wiki_path = get_wiki_path()
    content_files = list(wiki_path.rglob("*.md"))
    content_files = [f for f in content_files if "_templates" not in str(f)]

    stale_indicators = []
    outdated_markers = [
        "outdated", "obsolete", "deprecated", "old version",
        "previous version", "formerly", "used to be"
    ]

    for md_file in content_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read().lower()
                for marker in outdated_markers:
                    if marker in content:
                        stale_indicators.append({
                            'file': md_file,
                            'indicator': marker,
                            'context': _get_context(content, marker, 100)
                        })
        except Exception as e:
            print(f"Error reading {md_file}: {e}")

    return stale_indicators

def find_missing_cross_references():
    """Find concepts mentioned but lacking their own page"""
    wiki_path = get_wiki_path()
    content_files = list(wiki_path.rglob("*.md"))
    content_files = [f for f in content_files if "_templates" not in str(f)]

    # Get all existing page names
    existing_pages = set()
    for md_file in content_files:
        existing_pages.add(md_file.stem)

    # Find all mentions of potential concepts (capitalized phrases)
    concept_pattern = r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)\b'
    potential_concepts = set()

    for md_file in content_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                matches = re.findall(concept_pattern, content)
                for match in matches:
                    # Filter out common words and short matches
                    if len(match) > 3 and match not in ['The', 'And', 'Or', 'But', 'For', 'With', 'This', 'That']:
                        potential_concepts.add(match)
        except Exception as e:
            print(f"Error reading {md_file}: {e}")

    # Find concepts that are mentioned but don't have pages
    missing_pages = []
    for concept in potential_concepts:
        # Check if we have a page for this concept (exact match or close variation)
        concept_variations = [
            concept,
            concept.replace(' ', '_'),
            concept.replace(' ', '-')
        ]

        has_page = any(var in existing_pages for var in concept_variations)
        if not has_page:
            missing_pages.append(concept)

    return list(set(missing_pages))[:20]  # Limit to top 20

def _get_context(text, marker, context_length):
    """Get context around a marker"""
    pos = text.find(marker)
    if pos == -1:
        return ""
    start = max(0, pos - context_length)
    end = min(len(text), pos + len(marker) + context_length)
    return text[start:end]

def update_index_after_lint():
    """Update the index after linting"""
    from wiki_ingest_helper import update_index
    update_index()

def log_lint_findings(orphan_count, stale_count, missing_count, issues_found):
    """Log lint operation results"""
    log_path = get_log_path()
    now = datetime.datetime.now().strftime("%Y-%m-%d")

    log_entry = f"""
## [{now}] lint | Health Check
- Issues found: {len(issues_found)} total
  - Orphan pages: {orphan_count}
  - Stale claims: {stale_count}
  - Missing cross-references: {missing_count}
- Actions taken: Generated report, suggested fixes
- Recommendations:
  - Review orphan pages for potential linking or deletion
  - Investigate stale claims for updates or removal
  - Consider creating pages for frequently mentioned missing concepts
"""

    with open(log_path, 'a') as f:
        f.write(log_entry)

    print(f"Logged lint operation: {len(issues_found)} issues found")

def main():
    """Main function for command line usage"""
    if len(sys.argv) < 2:
        print("Usage: wiki_lint_helper.py <command>")
        print("Commands:")
        print("  orphans   - Find orphan pages")
        print("  stale     - Find potential stale claims")
        print("  missing   - Find missing cross-references")
        print("  full      - Run full lint check")
        return

    command = sys.argv[1]

    if command == "orphans":
        orphans = find_orphan_pages()
        print(f"Found {len(orphans)} orphan pages:")
        for page_name, file_path in orphans[:10]:  # Show first 10
            print(f"  - [[{page_name}]] ({file_path.relative_to(get_wiki_path())})")
        if len(orphans) > 10:
            print(f"  ... and {len(orphans) - 10} more")

    elif command == "stale":
        stale = find_stale_claims()
        print(f"Found {len(stale)} potential stale claims:")
        for item in stale[:5]:  # Show first 5
            print(f"  - In {item['file'].relative_to(get_wiki_path())}: '{item['indicator']}'")
            print(f"    Context: ...{item['context']}...")
        if len(stale) > 5:
            print(f"  ... and {len(stale) - 5} more")

    elif command == "missing":
        missing = find_missing_cross_references()
        print(f"Found {len(missing)} concepts mentioned but lacking pages:")
        for concept in missing[:10]:  # Show first 10
            print(f"  - {concept}")
        if len(missing) > 10:
            print(f"  ... and {len(missing) - 10} more")

    elif command == "full":
        print("Running full LLM Wiki lint check...")

        # Check for orphans
        orphans = find_orphan_pages()
        print(f"\n🔍 ORPHAN PAGES ({len(orphans)} found):")
        if orphans:
            for page_name, file_path in orphans[:5]:
                print(f"  - [[{page_name}]]")
            if len(orphans) > 5:
                print(f"  ... and {len(orphans) - 5} more")
        else:
            print("  ✅ No orphan pages found!")

        # Check for stale claims
        stale = find_stale_claims()
        print(f"\n🕰️  STALE CLAIMS ({len(stale)} found):")
        if stale:
            for item in stale[:3]:
                print(f"  - In {item['file'].relative_to(get_wiki_path())}: '{item['indicator']}'")
            if len(stale) > 3:
                print(f"  ... and {len(stale) - 3} more")
        else:
            print("  ✅ No stale claims detected!")

        # Check for missing cross-references
        missing = find_missing_cross_references()
        print(f"\n🔗 MISSING CROSS-REFERENCES ({len(missing)} found):")
        if missing:
            for concept in missing[:5]:
                print(f"  - {concept}")
            if len(missing) > 5:
                print(f"  ... and {len(missing) - 5} more")
        else:
            print("  ✅ All mentioned concepts have corresponding pages!")

        # Summary
        total_issues = len(orphans) + len(stale) + len(missing)
        print(f"\n📊 SUMMARY: {total_issues} total issues found")

        if total_issues > 0:
            print("\n💡 RECOMMENDATIONS:")
            if orphans:
                print(f"  - Review {len(orphans)} orphan pages for linking or cleanup")
            if stale:
                print(f"  - Investigate {len(stale)} potentially stale claims")
            if missing:
                print(f"  - Consider creating pages for {len(missing)} frequently mentioned concepts")
            print("  - Run this lint check regularly to maintain wiki health")
        else:
            print("  🎉 Wiki appears to be in good health!")

        # Update index and log
        update_index_after_lint()
        log_lint_findings(len(orphans), len(stale), len(missing),
                         [{'type': 'orphan', 'count': len(orphans)},
                          {'type': 'stale', 'count': len(stale)},
                          {'type': 'missing', 'count': len(missing)}])

    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()