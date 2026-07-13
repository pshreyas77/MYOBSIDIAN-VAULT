---
name: kb-compile
description: Compile raw source material from 0-raw/ into structured wiki pages in 02 - AREAS/ — Step 2 of the Karpathy method: Let the LLM write your wiki for you.
version: 2.0.0
category: knowledge-management
tags: [obsidian, knowledge-base, compilation, karpathy-method, second-brain, karpathy]
vault_path: "E:/_Knowledge/ObsidianVault"
raw_dir: "0-raw"
output_dir: "02 - AREAS"
state_file: ".kb-compile-state.json"
---

# kb-compile Skill

Reads raw source files from `0-raw/` and produces or updates structured wiki pages in `02 - AREAS/`. This is Step 2 of the Karpathy method: "Let the LLM Write Your Wiki For You."

> The human doesn't organize. The LLM does. You barely touch the output.

## Usage

```
/kb-compile                # Incremental: process raw files newer than last compile
/kb-compile --full         # Full recompilation of every raw file
/kb-compile --limit 5      # Cap at 5 files this run
/kb-compile --since 2026-07-01  # Only raw files modified after date
```

## Prerequisites

- Vault at `E:/_Knowledge/ObsidianVault`
- Raw files in `0-raw/` (`.md` only — `.canvas` files are skipped)

## How It Works

### 1. Scan `0-raw/`

List all `.md` files. Skip `.canvas`. Sort by modification time (newest first).

### 2. Check state file

Read `.kb-compile-state.json` to know what's already processed. Skip already-done files in incremental mode.

### 3. For each raw file

**Extract:**
- Topic/domain (which AREAS folder does it belong to?)
- Key concepts mentioned
- Key entities (people, places, organizations)
- Key claims/facts
- Questions it raises
- Sources/references

**Decide:**
- Does a wiki page for this topic already exist?
- YES → update/add to existing page
- NO → create new page in appropriate `02 - AREAS/` subfolder

### 4. Write/update wiki pages

Each page gets:
- `[[For-Future-Claude]]` preamble
- Concept definition
- Key insights (bullet points)
- Key claims with source links
- Wikilinks to related concepts
- Open questions
- Confidence level

### 5. Update state file

Record processed files + timestamp.

## Concept Page Template

```markdown
---
date: YYYY-MM-DD
type: concept
tags: [domain, sub-topic]
ai-first: true
confidence: 0.8
sources: ["0-raw/source-file.md"]
---

# Concept Name

**For Future Claude:** [Brief note on what this page knows, what's uncertain, what to verify]

## Definition

[Brief 2-3 sentence definition]

## Key Insights

- Insight 1
- Insight 2

## Key Claims

- Claim 1 (source: [[0-raw/source-file]])
- Claim 2 (source: [[0-raw/source-file]])

## Related Concepts

[[Related Concept 1]], [[Related Concept 2]], [[Related Concept 3]]

## Open Questions

- Question 1
- Question 2

---

*Compiled: YYYY-MM-DD | Source: [[0-raw/source-file]]*
```

## Domain Routing

| Raw file topic | Output folder |
|---------------|---------------|
| History, archaeology, ancient civs | `02 - AREAS/03 Ancient Civilizations/` |
| Philosophy, religion, yoga | `02 - AREAS/01 Philosophy & Religion/` |
| AI, tech, tools | `02 - AREAS/02 AI & Technology/` |
| Indian politics, elections | `02 - AREAS/04 Political Analysis/` |
| Career, productivity | `02 - AREAS/06 Personal Development/` |
| Society, caste, Dravidian | `02 - AREAS/06 Society & Culture/` |
| Knowledge management, skills | `02 - AREAS/05 Knowledge Management/` |

## State File Format

```json
{
  "last_full_compile": "2026-07-10T14:30:00Z",
  "last_incremental": "2026-07-13T09:15:00Z",
  "processed_files": {
    "0-raw/article.md": "2026-07-10T14:30:00Z",
    "0-raw/test.md": "2026-07-13T09:00:00Z"
  },
  "pages_created": 12,
  "pages_updated": 8
}
```

## First-Run Checklist

Before running for the first time:
- [ ] `0-raw/` has at least 1 raw source file
- [ ] `02 - AREAS/` folders exist for each domain
- [ ] State file `.kb-compile-state.json` doesn't exist (will be created)

## Vault Directory Reference

```
E:/_Knowledge/ObsidianVault/
├── 0-raw/                          ← RAW CAPTURES (your inbox)
│   ├── 2026-05-27_peopling-raw.md  ← only 1 file! Use this more.
│   └── test-source-article.md
├── 02 - AREAS/                     ← WIKI (1,194 concept pages)
│   ├── 01 Philosophy & Religion/
│   ├── 02 AI & Technology/
│   ├── 03 Ancient Civilizations/
│   ├── 04 Political Analysis/
│   ├── 05 Knowledge Management/
│   └── 06 Personal Development/
├── 02 - PERMANENT/                 ← CANONICAL (concepts + people)
│   ├── concepts/
│   └── people/
├── 05 - OUTPUTS/                   ← GENERATED REPORTS
└── 05 - MEMORY/                    ← 5-TIER MEMORY ENGINE
```

## Current Raw Capture Status

**Problem:** `.raw/` and `0-raw/` have very few files. Capture is not being used.

**Fix:** Every time you encounter an interesting article, immediately clip it to `0-raw/`. Don't organize. Don't rename. Just capture. The compile skill handles the rest.

## Pitfalls

- `.canvas` files are skipped (Obsidian canvas, not markdown)
- Wikilinks must use `[[Page Name]]` syntax for graph view to work
- Confidence: 0.9+ = well-established fact, 0.7-0.9 = probable, <0.7 = speculative
- Always include `[[For-Future-Claude]]` preamble so future sessions know context

---

*Skill version: 2.0.0 | Updated: 2026-07-13*
*Vault: E:\_Knowledge\ObsidianVault*