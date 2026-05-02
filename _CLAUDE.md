# Claude Operating Manual — Shreyas Patel's Vault

> Read this file before doing anything in this vault.
> This is the single source of truth for how Claude operates here.

---

## Vault Identity

- **Owner:** Shreyas Patel
- **Primary purpose:** Life OS — philosophy, AI, technology, political analysis, knowledge management, and personal research
- **Last updated:** 2026-04-24

---

## Folder Map

| Folder | Purpose |
|---|---|
| `00 - SYSTEM` | System notes, knowledge hub, MOCs, and meta-structure |
| `01 - PROJECTS` | Active and archived projects (PARA) |
| `02 - AREAS` | Areas of responsibility and topic clusters (PARA) |
| `03 - RESOURCES` | Reference materials, raw sources, and external links (PARA) |
| `04 - ARCHIVE` | Archived and inactive items (PARA) |
| `Attachments` | File attachments for notes |
| `BUDDHA` | Buddhist philosophy and research notes |
| `Daily Notes` | Daily journal and log notes (YYYY-MM-DD format) |
| `Templates` | Note templates for different types |
| `wiki` | Evergreen knowledge notes and concept maps |
| `projects` | Alternative project notes (legacy or specific use) |
| `graphify-out` | Generated knowledge graph and analysis |
| `all canvas` | Obsidian canvas files for visual thinking |
| `.claude` | Claude skill configurations and local settings |
| `.git` | Version control repository |
| `.openclaude` | OpenClaude session and task data |
| `.obsidian` | Obsidian application settings |
| `.raw` | Raw source materials (articles, transcripts, PDFs) |
| `.smart-env` | Environment configuration |
| `.trash` | Deleted items (temporary) |
| `Weekly Notes` | Weekly review and planning notes |
| `QwenVault` | Experimental AI vault or test space |
| `project_OB__AI` | Specific AI project notes |
| `03 - RESORCES` | (Typo variant of RESOURCES) |
| `04 - RESOURCES` | (Duplicate resources folder) |
| `genericagent` | Test or experimental agent code |
| `entities.json` | Extracted entities from knowledge graph |
| `DUPLICATE_ANALYSIS_REPORT.json` | Report from duplicate file analysis |
| `DUPLICATE_CLEANUP_LOG.json` | Log from duplicate cleanup operation |
| `Buddhism_Hinduism_Research_Report *.docx` | Research reports in Word format |

---

## Naming Conventions

- **Date format:** `YYYY-MM-DD` for dated notes (e.g., `2026-04-24 — Daily Note.md`)
- **Evergreen notes:** `Title.md` (no date prefix)
- **Separators:** Use em dash ` — ` between date and title
- **No special characters** in filenames except ` — `

---

## Frontmatter Standards

Every note must include frontmatter. Minimum:
```yaml
---
date: 2026-04-24
tags:
  - <note-type>
---
```
Note types and their tags:
- `daily`: For daily notes
- `project`: For project notes
- `area`: For area/topic notes
- `resource`: For reference materials
- `knowledge`: For evergreen knowledge notes
- `task`: For task items
- `person`: For people notes
- `meeting`: For meeting notes
- `idea`: For idea captures
- `decision`: For decision records
- `concept`: For concept explanations
- `template`: For note templates

---

## Kanban Board System

This vault uses a hybrid system:
- Primary task management through Obsidian Kanban plugin (if enabled)
- Alternative: Task notes in `Tasks/` folder (to be created) linked from project notes
- Weekly and daily notes for time-based tracking
- Graph view for visual task and project relationships

Board columns (when using Kanban):
- `📥 Backlog` — Items not yet started
- `📋 This Week` — Items to work on this week
- `🔨 In Progress` — Active work items
- `✅ Done` — Completed items (with strikethrough and date)

---

## Automation & Preferences

- **Auto-save:** Save conversations after 10+ exchanges or when logical work blocks complete
- **Links:** Use `[[Note Name]]` for internal links. Always link to people, projects, and jobs.
- **Dates:** ISO format (`YYYY-MM-DD`) in frontmatter. Human format (`April 24`) in body text.
- **Bi-temporal facts:** For changing facts (role, location, etc.), use `timeline:` array with event time and learned time.
- **Critical facts:** Maintain `CRITICAL_FACTS.md` with timezone, current role, and location.
- **Index:** Update `00 - SYSTEM/index.md` (or equivalent) when new notes are created.
- **Log:** Append to `00 - SYSTEM/log.md` with format: `## [YYYY-MM-DD] action | Description`

---

## Special Handling

- **People notes:** Create in `People/` folder (to be created) with role, company, and interaction history.
- **Project notes:** Link to related kanban board items and daily notes.
- **Decisions:** Add to project note's `## Key Decisions` section with date.
- **Ideas:** Capture in `Ideas/` folder (to be created) or append to existing idea notes.
- **Dev logs:** Save to `Dev Logs/` folder (to be created) with project name and technical details.
- **Knowledge ingestion:** Save raw sources to `03 - RESOURCES/raw/` and processed notes to `wiki/`.

---

## MCP Server Recommendation

For enhanced performance, connect the Obsidian MCP server:
```bash
claude mcp add obsidian-vault -s user -- npx -y mcp-obsidian "/home/sunny77/Documents/Obsidian Vault"
```

---

## Graphify Knowledge Graph

- The vault maintains a knowledge graph at `graphify-out/`
- Before answering architecture or codebase questions, read `graphify-out/GRAPH_REPORT.md` for god nodes and community structure
- After modifying code files, run the rebuild command to keep the graph current:
  ```bash
  python3 -c "from graphify.watch import _rebuild_code; from pathlib import Path; _rebuild_code(Path('.'))"
  ```
- Use the graph view for visual exploration of connections between notes.

---

## Vault Maintenance

- Run `/obsidian-health` monthly to check for duplicates, broken links, and missing frontmatter
- Use `/obsidian-reconcile` to resolve contradictions in claims
- Run `/obsidian-synthesize` to generate new insight connections
- Keep `index.md` and `log.md` updated for navigation and audit trail

---
*This file is persisted across Claude surfaces. Update it when vault conventions change.*