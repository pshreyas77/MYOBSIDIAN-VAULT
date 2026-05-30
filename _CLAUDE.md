# Claude Operating Manual — Obsidian Vault

> Read this file before doing anything in this vault.
> This is the single source of truth for how Claude operates here.
> Current system: MemPalace + obsidian-second-brain + obsidian-skills + Graphify

---

## Vault Identity

- **Owner:** Researcher
- **Primary purpose:** Research knowledge base — Buddhism, Hinduism, Ancient Civilizations, Cosmology, AI Research
- **Total files:** ~526 files indexed
- **Last updated:** 2026-04-18
- **Graphify stats:** 263 nodes, 434 edges, 27 communities

---

## Folder Map

| Folder | Purpose |
|--------|---------|
| `00 - SYSTEM/` | System files, dashboards, indexes |
| `01 - Projects/` | Active research projects |
| `02 - Areas/` | Knowledge areas (Buddhism, Civilizations, etc.) |
| `03 - Resources/` | Reference materials, sources |
| `04 - Archive/` | Completed/archived research |
| `07 - Topics/` | Topic-based organization |
| `BUDDHA/` | Core Buddhism research (9 files) |
| `OLDEST CIVILIZATION/` | Ancient civilizations (8 files) |
| `COSMOLOGY/` | Religious cosmology comparison |
| `QwenVault/` | Claude conversations archive |
| `ClaudeVault/` | AI research agents framework |
| `KIMI VAULT/` | Personal knowledge base |
| `DeepseekVault/` | Deep research materials |
| `wiki/` | Wiki structure (entities, concepts, sources) |
| `graphify-out/` | Knowledge graph outputs |
| `.claude/skills/` | Installed Claude skills |

---

## Key Files

- **Research Hub:** `[[RESEARCH HUB]]` — Main navigation
- **Master Links:** `[[MASTER LINK INDEX]]` — Cross-references
- **Comprehensive Summary:** `[[COMPREHENSIVE RESEARCH SUMMARY]]` — 13 threads
- **Graph Visualization:** `graphify-out/obsidian_graph.html`
- **Hot Cache:** `wiki/meta/hot.md` — Session persistence

---

## Active Context

**Current research areas:**
1. Buddhism origins & Hinduism comparison
2. Ancient civilizations (Göbekli Tepe → Indus Valley)
3. Religious cosmology comparison
4. AI Research Agents framework

**Key entities:** Buddha, Göbekli Tepe, Çatalhöyük, Indus Valley, Siddhartha Gautama

---

## AI Tools Integrated

| Tool | Command | Purpose |
|------|---------|---------|
| MemPalace | `mempalace search "query"` | Semantic search (21,228 drawers) |
| MemPalace | `mempalace status` | Palace overview |
| MemPalace | `mempalace wake-up` | Load context |
| Graphify | `graphify query "..."` | Query knowledge graph |
| Graphify | `graphify path "A" "B"` | Find connections |

---

## Slash Commands Available

### obsidian-second-brain
- `/obsidian-save` — Extract decisions/tasks from conversation
- `/obsidian-ingest <URL/file>` — Process content into vault
- `/obsidian-daily` — Create daily note
- `/obsidian-challenge` — Find contradictions
- `/obsidian-emerge` — Surface patterns
- `/obsidian-world` — Load full vault context
- `/obsidian-visualize` — Generate canvas
- `/obsidian-reconcile` — Resolve contradictions
- `/obsidian-synthesize` — Create synthesis

### obsidian-skills
- `/obsidian-markdown` — Format markdown
- `/json-canvas` — Create canvas
- `/obsidian-bases` — Database operations

---

## Auto-Save Rules

**Claude should auto-save:** (using obsidian-second-brain)
- Decisions → Project notes + daily note
- New entities → wiki/entities/ + wiki/meta/hot.md
- Tasks → Daily note + task board
- Research findings → Relevant topic files + wiki/
- Contradictions → Flag in wiki with `>[!contradiction]`

---

## Naming Conventions

- Daily notes: `YYYY-MM-DD.md`
- Entity pages: `Entity Name.md` with `#entity` tag
- Concept pages: `Concept Name.md` with `#concept` tag
- Wiki pages: `wiki/<type>/Name.md`
- Canvas files: `Name.canvas`

---

## Frontmatter Requirements

```yaml
---
title: Note Title
date: YYYY-MM-DD
tags:
  - entity|concept|source|daily
---
```

---

## Wiki Structure

| Type | Location | Tag |
|------|----------|-----|
| Entities | `wiki/entities/` | `#entity` |
| Concepts | `wiki/concepts/` | `#concept` |
| Sources | `wiki/sources/` | `#source` |
| Meta | `wiki/meta/` | `#meta` |

---

## Propagation Rules

| Event | Also update |
|-------|-------------|
| New entity | wiki/meta/index.md + hot.md + graphify |
| New concept | wiki/meta/index.md + related entities |
| Research finding | Topic file + wiki/synthesis/ + daily note |
| Contradiction found | Flag both sources + create reconciliation |
| New source ingested | raw/ + wiki/sources/ + mempalace mine |

---

## Research Themes (13 Threads)

1. Ancient Civilizations Timeline (Göbekli Tepe → Indus Valley)
2. Buddhism-Hinduism Chronology
3. Temple Destruction Evidence
4. Political Construction of History
5. Vishnu Avatar Theory Debunked
6-8. Science & Religion Comparison
9. Buddhism Origins
10. Temple Chronology
11. Archaeological Evidence
12. Hindu Nationalism Critique
13. Comparative Cosmology

---

## Do Not Touch

- `graphify-out/*` — Generated, will overwrite on re-run
- `wiki/_templates/` — Templates for future use
- `.obsidian/` — Obsidian settings
- `mempalace.yaml` — MemPalace configuration

---

## Environment

```
MEMPALACE_PALACE=/home/sunny77/.mempalace/obsidian_vault
MEMPAL_DIR=/home/sunny77/Documents/Obsidian Vault
```

---

## Usage Patterns

### Research Session:
```
1. /obsidian-daily → Create daily note
2. mempalace search "topic" → Find existing context
3. Work with Claude...
4. /obsidian-save → Extract findings
5. graphify query "connections" → Find patterns
```

### Content Ingestion:
```
1. /obsidian-ingest <URL> → Process into vault
2. mempalace mine . → Add to palace
3. graphify /path --update → Update knowledge graph
4. /obsidian-emerge → Find new patterns
```

---

**Current system version:** Second Brain v3.0
**Components:** MemPalace + obsidian-second-brain + obsidian-skills + Graphify

---

*This file was generated for the integrated AI-second-brain system.*
*Regenerate with: "Update my _CLAUDE.md"*
