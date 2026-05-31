---
date: 2026-05-31
tags:
  - entity
  - project
  - python
  - knowledge-graph
type: entity
status: active
---

# graphify-repo

Python knowledge graph extraction tool with 17+ modules for analyzing, building, and exporting knowledge graphs from various sources.

## Overview

graphify-repo is a comprehensive Python toolkit for extracting knowledge graphs from documents, code, and other data sources. It supports clustering, scoring, export to multiple formats, and more.

## Structure

```
graphify-repo/
├── graphify/
│   ├── __init__.py     # Lazy-import module
│   ├── analyze.py      # Analysis logic
│   ├── benchmark.py    # Performance benchmarking
│   ├── build.py        # Graph building
│   ├── cache.py        # Caching layer
│   ├── cluster.py      # Clustering algorithms
│   ├── detect.py       # Detection utilities
│   ├── export.py       # Export functionality
│   ├── extract.py      # Extraction engine
│   ├── hooks.py        # Integration hooks
│   ├── ingest.py       # Data ingestion
│   ├── manifest.py     # Manifest handling
│   ├── report.py       # Reporting
│   ├── security.py     # Security utilities
│   ├── serve.py        # Server functionality
│   ├── transcribe.py   # Transcription
│   ├── validate.py     # Validation
│   ├── wiki.py         # Wiki integration
├── tests/             # Full test suite
└── skills/             # Skill definitions
```

## Key Functions

- `extract()` — Extract knowledge from sources
- `build_from_json()` — Build graph from JSON
- `cluster()` — Cluster related entities
- `score_all()` — Score node importance
- `god_nodes()` — Identify central nodes
- `surprising_connections()` — Find unexpected links
- `suggest_questions()` — Generate research questions
- `to_json()`, `to_html()`, `to_svg()`, `to_canvas()`, `to_wiki()` — Export formats

## Related

- [[wiki/entities/GitNexus]] — AI Git analysis tool
- [[wiki/entities/genericagent]] — Python autonomous agent
- [[wiki/entities/tolaria]] — Tauri + React app

## Source

`E:\_Knowledge\ObsidianVault\graphify-repo\`