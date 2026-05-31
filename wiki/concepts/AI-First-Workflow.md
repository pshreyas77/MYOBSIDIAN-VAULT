---
date: 2026-05-31
tags:
  - concept
  - pkm
  - obsidian
  - knowledge-management
type: concept
status: active
---

# AI-First Workflow

An operating methodology where an AI assistant (Claude) maintains and structures a personal knowledge management (PKM) vault with minimal user intervention. The AI operates as an autonomous agent managing the vault structure.

## Core Principles

1. **Autopilot Mode** — AI takes full permission to operate without asking for approval
2. **Bi-Temporal Facts** — Never overwrite; append history with `timeline:` frontmatter
3. **Wiki-Structure** — All notes linked via `[[wikilinks]]`
4. **Synthesis** — Patterns across 3+ sources trigger new concept pages
5. **Five-Phase Consolidation** — Nightly automated maintenance

## Vault Structure (AI-First)

```
vault/
├── wiki/
│   ├── entities/     # People, projects, companies
│   ├── concepts/     # Ideas, patterns, syntheses
│   ├── analyses/     # Deep dives
│   └── summaries/    # Topic summaries
├── 04 - DAILY/      # Daily notes
├── 01 - LITERATURE/  # Sources and references
├── 02 - AREAS/       # Areas of focus
├── 03 - PROJECTS/    # Active projects
├── 06 - OUTPUTS/     # Generated content
└── logs/             # Session logs
```

## Five-Phase Nightly Consolidation

| Phase | Action |
|-------|--------|
| 1. Close the Day | Update daily note, move completed kanban items |
| 2. Reconcile | Update entity facts, resolve contradictions |
| 3. Synthesize | Create cross-source concept pages |
| 4. Heal | Link orphaned notes, fix broken references |
| 5. Log | Append to `log.md` |

## Status Values

**Projects:** `active` / `planning` / `completed` / `archived` / `on-hold`
**Tasks:** `in-progress` / `done` / `waiting` / `blocked`

## Naming Conventions

- Daily notes: `YYYY-MM-DD.md`
- Project notes: `YYYY-MM-DD — Title.md`
- Wiki entities: `wiki/entities/Name.md`
- Wiki concepts: `wiki/concepts/Concept-Name.md`

## Slash Commands

| Command | Purpose |
|---------|---------|
| `/obsidian-save` | Save conversation to vault |
| `/obsidian-daily` | Create/find daily note |
| `/obsidian-log` | Add to session log |
| `/obsidian-task` | Create task |
| `/obsidian-person` | Create entity page |
| `/obsidian-decide` | Log decision with rationale |

## Related Concepts

- [[wiki/concepts/Autonomous-Agent-Research]] — AI agents conducting research
- [[wiki/concepts/Knowledge-Graph-Extraction]] — Extracting structured knowledge

## Source

`E:\_Knowledge\ObsidianVault\_CLAUDE.md`