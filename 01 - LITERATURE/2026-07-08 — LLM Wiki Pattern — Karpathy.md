---
date: 2026-07-08
type: literature
subtype: methodology
tags: [pkm, knowledge-management, llm-wiki, karpathy, methodology, reference]
status: active
ai-first: true
source: "Karpathy's 'LLM Wiki' pattern document"
---

# LLM Wiki Pattern — Reference Note

**For future Claude:** Karpathy's foundational pattern for building personal knowledge bases using LLMs. This is the *abstract idea* that Eugeniu Ghelbur's `obsidian-second-brain` repo extends with 44 commands. Understanding the pattern (not the specific commands) lets us instantiate it for any vault, CLI, or LLM.

---

## 1. The Core Idea

**Traditional RAG problem**: Every query re-derives knowledge from fragments. Nothing is built up. Five-document synthesis means five retrievals + five compositions every time.

**LLM Wiki solution**: The LLM **incrementally builds and maintains a persistent wiki** — a structured, interlinked collection of markdown files.

| Aspect | RAG (status quo) | LLM Wiki (this pattern) |
|--------|------------------|------------------------|
| **Source handling** | Index for retrieval | Read, extract, integrate |
| **Updates** | None | Rewrites existing pages, revises claims |
| **Contradictions** | Hidden | Flagged automatically |
| **Synthesis** | Re-derived per query | Compiled once, kept current |
| **Your role** | Write queries | Curate sources, ask questions |
| **LLM role** | Retrieval tool | Bookkeeper + writer |

**Key difference**: *Wiki is a persistent, compounding artifact.*

---

## 2. Architecture — Three Layers

```
┌──────────────────────────────────────────────┐
│  LAYER 1: RAW SOURCES (Immutable)            │
│  Articles, papers, images, data files        │
│  LLM reads but never modifies                │
│  Source of truth                              │
├──────────────────────────────────────────────┤
│  LAYER 2: THE WIKI (LLM-owned)               │
│  Entity pages, concept pages, summaries,     │
│  comparisons, index                          │
│  LLM creates, updates, maintains entirely    │
│  You read; LLM writes                        │
├──────────────────────────────────────────────┤
│  LAYER 3: THE SCHEMA                         │
│  CLAUDE.md / AGENTS.md / system instructions  │
│  Tells LLM HOW the wiki is structured        │
│  Co-evolves with LLM as you figure out what  │
│  works                                       │
└──────────────────────────────────────────────┘
```

The schema is the **key configuration file** — it transforms a "generic chatbot" into a "disciplined wiki maintainer."

---

## 3. Three Operations

### Ingest
When you drop a new source:
1. LLM reads source
2. Discusses key takeaways with you
3. Writes new summary page
4. Updates index
5. **Updates existing entity/concept pages** (cross-referencing)
6. Appends to log

> *"A single source might touch 10–15 wiki pages."*

### Query
When you ask a question:
- LLM searches index → reads relevant pages → synthesizes answer with citations
- Answers can take any form: markdown, comparison table, slide deck (Marp), chart (matplotlib), canvas
- **Good answers can be filed back as new wiki pages** — explorations compound like ingested sources

### Lint
Periodic health checks asking the LLM to find:
- Contradictions between pages
- Stale claims superseded by newer sources
- Orphan pages with no inbound links
- Important concepts mentioned but lacking their own page
- Missing cross-references
- Data gaps that web search could fill

---

## 4. Two Special Files

### `index.md` — Content-Oriented Catalog

| Property | Description |
|----------|-------------|
| **Purpose** | LLM reads FIRST when navigating wiki |
| **Cheaper** than embedding-based RAG |
| **Format** | `- [[Note Name]] — brief description`, grouped by category |
| **Update cadence** | Every ingest |
| **Scale** | Works well up to ~100 sources / ~hundreds of pages |

### `log.md` — Chronological Record

| Property | Description |
|----------|-------------|
| **Format** | Append-only; consistent prefix for parsing |
| **Example** | `## [2026-07-08] ingest | Article Title` |
| **Parseable via** | `grep "^## \[" log.md \| tail -5` |
| **Purpose** | Timeline of wiki evolution |

---

## 5. Mapped to Your Vault

| Karpathy Concept | Your Equivalent | Status |
|------------------|-----------------|--------|
| **Raw sources** | `01 - LITERATURE/`, `1-desk/article/`, `Briefings/`, `Research/Articles/` | ✅ Active |
| **The wiki** | `wiki/entities/`, `wiki/concepts/`, `2-atoms/`, `02 - PERMANENT/` | ✅ Active |
| **Index** | `index.md` at root | ✅ Active, just updated today |
| **Schema** | `_CLAUDE.md`, `house-rules.md`, `genericagent/memory/autonomous_operation_sop.md` | ✅ Active |
| **Log** | `log.md` at root | ✅ Exists |
| **MOCs** | `05 - MAPS/` (your orientation maps) | ✅ Already evolved beyond Karpathy's pattern |
| **Graph view** | `.obsidian/graph.json` (20 color groups) | ✅ Just configured |
| **Operations commands** | Eugeniu Ghelbur's `obsidian-second-brain/` repo (44 commands) | 🔄 Considered, not yet installed |
| **Attribution compliance** | Recency markers, "For future Claude" preamble, confidence levels | ✅ Active in your notes |

---

## 6. Optional CLI Tools

| Tool | Purpose | When Useful |
|------|---------|-------------|
| **[qmd](https://github.com/tobi/qmd)** | Local on-device search over markdown (BM25 + vector + LLM rerank) | When vault exceeds ~100 sources where `index.md` becomes insufficient |
| **Marp** | Markdown slide decks | When you generate presentations from wiki content |
| **Dataview** | Obsidian plugin running queries over frontmatter | Already installed in your vault |
| **Obsidian Web Clipper** | Browser → markdown conversion for sources | Daily use |
| **Obsidian Graph View** | Visualize wiki structure | Already configured |

---

## 7. Tips Karpathy Emphasizes

- **Download images locally** (Settings → Files & links → Attachment folder path = `raw/assets/`; bind hotkey)
- Obsidian Graph View = best way to see wiki shape
- Wiki = just a git repo → free version history & collaboration
- The tedious part = bookkeeping; LLMs don't get bored, can touch 15 files per pass
- Cost of maintenance = near zero with LLMs

---

## 8. Why It Works

> *"Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero."*

Related in spirit to **Vannevar Bush's Memex (1945)** — personal, curated knowledge store with **associative trails between documents**. Bush's vision: private, actively curated, the connections as valuable as the documents.

**What Bush couldn't solve**: who does the maintenance?  
**The LLM does.**

---

## 9. Your Situation vs Karpathy's Pattern

Your vault is **already substantially more sophisticated** than the baseline Karpathy pattern:

| Karpathy Suggests | Your Vault Has |
|-------------------|----------------|
| Three folders (raw / wiki / schema) | PARA + 8 folders (00–07) |
| `index.md` (flat catalog) | `index.md` + 7 MOCs (`05 - MAPS/`) |
| Log.md (chronological) | `log.md` + per-day `04 - DAILY/` |
| Generic entity pages | Typed entities (person/org/concept) in `wiki/` |
| No graph view | Custom 20-color graph system |
| Manual linting | Eigenii's 44 commands offer automation |
| Single LLM-driven flow | `genericagent/` + `Night Shift` autonomous agents |

**Conclusion**: Your vault is already operating as an LLM Wiki pattern, **evolved**. The Eugeniu repo's 44 commands would add automation layers you don't yet have (auto-synthesis, contradiction reconciliation, contextual world-loading) — but they build on a foundation you already have.

---

## 10. Open Questions (For Future Iterations)

1. After 200+ sources, does `index.md` + MOCs scale or do we need qmd search?
2. Should we add **scheduled agents** (nightly lint, weekly review, contradiction sweep)?
3. Can we build **bi-temporal fact tracking** (when a claim was true AND when vault learned it)?
4. Should the LLM have **reading-only access** to some folders (raw sources) and **write access** to others (wiki)?
5. Where do `06 - OUTPUTS/` (finished essays) fit in the wiki pattern — separate or absorbed?

---

## 🔗 Cross-Links

- [[index.md]] — your vault catalog
- [[Research/PKM/Writing-Publication-Pipeline.md]] — output layer
- [[05 - MAPS/Digital Garden MOC.md]] — your garden equivalent
- [[05 - MAPS/Agentic Systems MOC.md]] — autonomous agents you already run
- [[03 - PROJECTS/History-Watchdog.md]] — ingest pattern in action
- [[03 - PROJECTS/Health-Autopilot.md]] — vault-as-state pattern
- [[03 - PROJECTS/Local-AI-Stack.md]] — local LLM infrastructure
- [[03 - PROJECTS/Cross-Domain Idea Synthesis.md]] — synthesis examples
- [[house-rules.md]] — your schema
- [[_CLAUDE.md]] — operating manual

---

*Generated: 2026-07-08 | Source: Karpathy's LLM Wiki pattern document | Status: Reference note for ongoing evolution*