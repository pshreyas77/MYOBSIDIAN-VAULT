# LLM Wiki Second Brain System

This directory contains the implementation of an LLM Wiki system for your Obsidian vault - a persistent, self-maintaining knowledge base that gets richer with every source added and question asked.

## Overview

The LLM Wiki pattern transforms your Obsidian vault from a static collection of notes into a dynamic, self-organizing second brain where:

1. **Knowledge is compiled once and kept current** - Not re-derived on every query
2. **The LLM handles all bookkeeping** - Cross-references, updates, consistency
3. **Explorations compound in the knowledge base** - Like ingested sources
4. **You focus on sourcing and asking questions** - The LLM does the grunt work

## Core Components

### 1. Index and Logging System
- **`index.md`** - Content-oriented catalog of all wiki pages
- **`log.md`** - Chronological append-only record of all operations

### 2. Ingestion Workflow
Semi-automated process for adding new sources:
```
[New Source] → LLM processes & discusses → Creates/updates summary → Updates index/entities → Logs ingest
```

### 3. Query-to-Wiki Feedback Loop
Valuable answers from queries are saved back to the wiki as new pages.

### 4. Regular Linting & Maintenance
Periodic health checks to detect contradictions, stale claims, orphan pages, and missing cross-references.

## Files Created

### Helper Scripts
- `wiki_ingest_helper.py` - Assists with ingesting new sources
- `wiki_query_helper.py` - Saves query answers as wiki pages
- `wiki_lint_helper.py` - Performs health checks on the wiki
- `wiki.py` - Unified CLI interface for all operations

### Template Directory
- `wiki/_templates/` - Templates for entity, concept, and source pages

### Core Wiki Files
- `wiki/index.md` - Master catalog
- `wiki/log.md` - Operation log
- `wiki/sources/` - Source summary pages
- `wiki/entities/` - Entity pages
- `wiki/concepts/` - Concept pages
- `wiki/comparisons/` - Query answers and analyses

## Usage

### Initialize the System
```bash
python3 wiki.py init
```

### Ingest a New Source
```bash
python3 wiki.py source "04 - RESOURCES/Inbox/article.pdf" "Article Title"
```

### Save a Query Answer
```bash
python3 wiki.py query "What is the LLM wiki pattern?" "It's a pattern for..." "[[Second Brain]] [[Knowledge Compounding]]"
```

### Run Health Checks
```bash
python3 wiki.py lint full
# or specific checks:
python3 wiki.py lint orphans
python3 wiki.py lint stale
python3 wiki.py lint missing
```

### Update Index
```bash
python3 wiki.py index
```

## Integration with Existing Systems

This LLM Wiki system integrates with your existing:

- **MemPalace** - Configured rooms for targeted operations
- **Graphify** - For ongoing knowledge graph analysis
- **Jarvis** - AI assistant capabilities
- **Obsidian Second Brain skill** - Enhanced with LLM Wiki commands

## Next Steps

1. **Regular Linting Schedule** - Run `wiki.py lint full` weekly
2. **Source Ingestion Workflow** - Develop consistent process for adding new materials
3. **Query-to-Wiki Habit** - Always consider saving valuable answers as wiki pages
4. **Graph Analysis** - Periodically run graphify to identify knowledge gaps and bridges
5. **Template Refinement** - Improve templates based on usage patterns

## Benefits

- Reduced time spent on manual organization and bookkeeping
- Increased discovery of serendipitous connections via graph/wiki navigation
- Knowledge base that gets smarter with each source added
- Focus shifted from organization to high-level thinking and sourcing
- Persistent compounding artifact that reflects your learning journey

## Philosophical Foundation

This system implements principles inspired by:
- **Vannevar Bush's Memex** (1945) - Personal knowledge store with associative trails
- **Zettelkasten** - Note-taking method emphasizing connections
- **Second Brain** methodology - Externalizing cognition for better thinking
- **LLM-Augmented Cognition** - Using AI to handle cognitive maintenance tasks

The LLM handles the tedious maintenance work (updating cross-references, keeping summaries current, noting contradictions) so you can focus on the valuable work: curating sources, directing analysis, asking good questions, and synthesizing insights.
## See Also
- [[orphan notes report]] - Identification of notes with zero incoming links
- [[link density report]] - Analysis of linking patterns across vault areas

- [[orphan notes report]] - Identification of notes with zero incoming links