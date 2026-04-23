#!/usr/bin/env python3
"""
LLM Wiki Query Helper
A simple script to demonstrate how query answers can be saved back to the wiki.
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

def save_query_answer(question, answer, related_pages=None):
    """Save a query answer as a new wiki page"""
    if related_pages is None:
        related_pages = []

    wiki_path = get_wiki_path()
    comparisons_dir = wiki_path / "comparisons"
    comparisons_dir.mkdir(exist_ok=True)

    # Create a safe filename from the question
    # Take first few words or create a summary
    words = question.split()[:6]  # First 6 words
    safe_title = "_".join(words)
    # Clean up the title
    safe_title = "".join(c for c in safe_title if c.isalnum() or c in (' ', '-', '_')).rstrip()
    safe_title = safe_title.replace(' ', '_')
    if not safe_title:
        safe_title = "query_answer"

    # Avoid duplicate filenames
    counter = 1
    original_title = safe_title
    while (comparisons_dir / f"{safe_title}.md").exists():
        safe_title = f"{original_title}_{counter}"
        counter += 1

    question_file = comparisons_dir / f"{safe_title}.md"

    # Get template or create a simple one for query answers
    template_path = get_templates_path() / "concept.md"  # Reuse concept template for now
    if template_path.exists():
        with open(template_path, 'r') as f:
            template = f.read()
    else:
        template = """---
title: [[Concept Name]]
type: concept
aliases: [Alternative Names]
date: {{DATE}}
updated: {{DATE}}
related_entities: []
---

# [[Concept Name]]

## Definition
[Clear definition]

## Applications/Domains
- Domain 1: [[Entity]] in [[Context]]
- Domain 2: [[Entity]] in [[Context]]

## Relationships
- Connects: [[Entity1]] and [[Entity2]]
- Similar to: [[Related Concept]]
- Contrasts with: [[Opposing Concept]]

## Sources
- [[Source Title]] - How it defines/explains the concept

## Examples
- Example 1: [Description]
- Example 2: [Description]

## Notes
[Debates, evolving understanding, open questions]

## Last Updated
{{DATE}}
"""

    # Fill template
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    # Make the title more readable
    display_title = " ".join(words)
    content = template.replace("[[Concept Name]]", display_title)
    content = content.replace("{{DATE}}", now)
    content = content.replace("[Clear definition]", f"Answer to: {question}")
    content = content.replace("- Domain 1: [[Entity]] in [[Context]]", f"- Based on wiki knowledge synthesis")
    content = content.replace("- Domain 2: [[Entity]] in [[Context]]", f"- Related pages: {', '.join([f'[[{p}]]' for p in related_pages]) if related_pages else '- None specified'}")
    content = content.replace("- Connects: [[Entity1]] and [[Entity2]]", f"- Connects question to answer through knowledge synthesis")
    content = content.replace("- Similar to: [[Related Concept]]", f"- Similar to: [[Query Answers]]")
    content = content.replace("- Contrasts with: [[Opposing Concept]]", f"- Contrasts with: [[Unknown/Unverified Information]]")
    content = content.replace("- [[Source Title]] - How it defines/explains the concept", f"- [[LLM Wiki Pattern]] - Provides framework for this synthesis")
    content = content.replace("- Example 1: [Description]", f"- Example 1: This very answer demonstrating the query-to-wiki pattern")
    content = content.replace("- Example 2: [Description]", f"- Example 2: Building compounding knowledge over time")
    content = content.replace("[Debates, evolving understanding, open questions]", f"Open questions: How to improve automatic linking? What sources could enhance this answer?")
    content = content.replace("# [[Concept Name]]\n\n", f"# {display_title}\n\n")

    # Write file
    with open(question_file, 'w') as f:
        f.write(content)

    print(f"Saved query answer: {question_file}")
    return question_file

def update_index_after_query():
    """Update the index after a query answer is added"""
    # Reuse the index update from the ingest helper
    from wiki_ingest_helper import update_index
    update_index()

def log_query(question, answer_summary, related_pages=None):
    """Log a query operation"""
    log_path = get_log_path()
    now = datetime.datetime.now().strftime("%Y-%m-%d")

    related_str = ", ".join(related_pages) if related_pages else "None"
    log_entry = f"""
## [{now}] query | {question[:50]}{'...' if len(question) > 50 else ''}
- Question: {question}
- Answer summary: {answer_summary}
- Related pages consulted: {related_str}
- New insights saved as: [[{question.split()[0]}_{question.split()[1] if len(question.split()) > 1 else 'answer'}]]
- Follow-up questions suggested:
  - How could this answer be improved with additional sources?
  - What contradictions might exist in the current wiki?
  - What related concepts should be explored next?
"""

    with open(log_path, 'a') as f:
        f.write(log_entry)

    print(f"Logged query: {question[:50]}...")

def main():
    """Main function for command line usage"""
    if len(sys.argv) < 3:
        print("Usage: wiki_query_helper.py <question> '<answer_summary>' [related_pages...]")
        print("Example: wiki_query_helper.py 'What is LLM wiki?' 'A pattern for building personal knowledge bases using LLMs' [[Second Brain]] [[Knowledge Compounding]]")
        return

    question = sys.argv[1]
    answer_summary = sys.argv[2]
    related_pages = sys.argv[3:] if len(sys.argv) > 3 else []

    # Save the answer
    saved_file = save_query_answer(question, answer_summary, related_pages)

    # Update index
    update_index_after_query()

    # Log the query
    log_query(question, answer_summary, related_pages)

    print(f"\nQuery processed successfully!")
    print(f"Question: {question}")
    print(f"Answer saved to: {saved_file.name}")
    print(f"Related pages: {', '.join(related_pages) if related_pages else 'None'}")

if __name__ == "__main__":
    main()