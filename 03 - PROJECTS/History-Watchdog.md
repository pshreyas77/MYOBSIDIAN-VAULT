---
date: 2026-07-08
type: project
tags: [project, history-watchdog, autonomous-agent, research, indian-history, ai]
status: active
ai-first: true
---

# History Watchdog — Automated Historiography Engine

**For future Claude:** Autonomous agent that continuously monitors new research on Aryan migration, IVC, Dravidian politics, RSS funding — updates your vault with delta-syntheses. Part of Cross-Domain Idea Synthesis Top 3 priority.

---

## Overview

**Problem**: High-value research notes (Aryan migration, Dravidian politics, RSS funding) are static. New papers publish constantly (ancient DNA, linguistics, archaeology, political disclosures). Manual monitoring doesn't scale.

**Solution**: Night Shift autonomous pipeline:
- **Scout** → Weekly: Elicit + Undermind + DeepSeek Deep Research on curated query sets
- **Refinery** → Filter by venue quality, extract claims, cross-ref Scite.ai for support/dispute
- **Editor** → Generate delta-updates with wikilinks to new sources
- **Audit** → Flag superseded/disputed claims in existing notes

---

## Query Sets (Scout Input)

### Aryan Migration / IVC / Ancient DNA
```
"ancient DNA South Asia" 2024..2026
"Rakhigarhi genome" new analysis 2024..2026
"Indus Valley Civilization" ancient DNA 2024..2026
"steppe ancestry South Asia" 2024..2026
"Indo-Aryan migration" linguistics 2024..2026
"Mitanni treaty" Indo-Aryan 2024..2026
```

### Dravidian Politics / Tamil Nadu
```
"Dravidian politics" Tamil Nadu 2024..2026
"DMK AIADMK" election 2024..2026
"Tamil Nadu" reservation policy 2024..2026
"Justice Party" Dravidian movement new research
"Periyar" new scholarship 2024..2026
```

### RSS / Hindutva Funding & Organization
```
"RSS funding" mechanisms 2024..2026
"Sangh Parivar" diaspora funding 2024..2026
"BJP South India" strategy 2024..2026
"Hindutva" organization new research 2024..2026
```

---

## Tool Stack

| Stage | Tool | Purpose | Access |
|-------|------|---------|--------|
| **Scout** | Elicit.org | Systematic paper search, comparison tables | Free tier |
| **Scout** | Undermind.ai | Deep academic search with reasoning chain | Free tier |
| **Scout** | DeepSeek Deep Research | Web search + structured reports (free, no limit) | chat.deepseek.com |
| **Scout** | Kimi | Long paper summarization (1M context) | kimi.com |
| **Refinery** | Scite.ai | Citation context: supported/disputed | Free tier |
| **Refinery** | Consensus.app | Evidence-meter from 200M+ papers | Free tier |
| **Editor** | NotebookLM | Multi-doc synthesis | Free |
| **Editor** | genericagent SOP | Autonomous operation framework | Local |
| **Audit** | Your vault notes | Target notes to update | Local |

---

## Target Notes to Keep Current

| Note | Domain | Last Updated | Priority |
|------|--------|--------------|----------|
| `Research/Deep/2026-06-22 — Aryan Migration Debate Evidence and Pre-Aryan India.md` | Genetics/Linguistics | 2026-06-22 | 🔴 Critical |
| `Research/2026-06-24 — Aryan Migration & Pre-Aryan Substrate — Final Verified Synthesis.md` | Synthesis | 2026-06-24 | 🔴 Critical |
| `05 - MAPS/Indian Political History MOC.md` | Politics | 2026-07-08 | 🟡 High |
| `Research/Articles/2026-06-09 — RSS Funding Mechanisms Analysis.md` | Funding | 2026-06-09 | 🟡 High |
| `Research/Articles/Entities/Bhutada Family Foundation.md` | Entity | 2026-06-09 | 🟡 High |
| `Research/Articles/Entities/Sewa International.md` | Entity | 2026-06-09 | 🟢 Medium |

---

## Agent Configuration (genericagent SOP)

```yaml
# In genericagent/memory/autonomous_operation_sop.md style
agent:
  name: history-watchdog
  schedule: "weekly monday 02:00"
  max_runtime_minutes: 45
  
stages:
  scout:
    queries_file: "E:/_Knowledge/ObsidianVault/03 - PROJECTS/History-Watchdog/queries.yaml"
    tools: [elicit, undermind, deepseek-deep-research, kimi]
    output: "E:/_Knowledge/ObsidianVault/03 - PROJECTS/History-Watchdog/raw/YYYY-MM-DD-scout.json"
    
  refinery:
    venue_filter: ["Science", "Cell", "Nature", "AJHG", "PNAS", "Current Biology", "PLOS Genetics", "Annual Review of Linguistics", "Journal of South Asian Studies"]
    citation_check: scite.ai
    output: "E:/_Knowledge/ObsidianVault/03 - PROJECTS/History-Watchdog/processed/YYYY-MM-DD-refined.json"
    
  editor:
    target_notes: [list above]
    link_format: "[[wikilink]] to new source note in Research/Automated/"
    output: "E:/_Knowledge/ObsidianVault/03 - PROJECTS/History-Watchdog/deltas/YYYY-MM-DD-delta.md"
    
  audit:
    check_claims_in: [target notes above]
    flag_if: "disputed by newer study" OR "superseded by better evidence"
    output: "E:/_Knowledge/ObsidianVault/03 - PROJECTS/History-Watchdog/audit/YYYY-MM-DD-flags.md"
```

---

## First Week Deliverable (2026-07-14)

- [ ] `queries.yaml` created with all query sets
- [ ] Scout pipeline tested: runs all 4 tools, outputs JSON
- [ ] Refinery tested: filters 50 papers → 5 high-quality, checks Scite
- [ ] Editor tested: produces delta for one target note
- [ ] Project hub note created: `03 - PROJECTS/History-Watchdog.md`
- [ ] Added to `05 - MAPS/AI & Technology MOC.md` (done)
- [ ] Night Shift cron configured for weekly Monday runs

---

## Vault Integration

```
03 - PROJECTS/
├── Cross-Domain Idea Synthesis.md          ← Parent idea note
├── History-Watchdog.md                     ← This project hub
└── History-Watchdog/
    ├── queries.yaml                        ← Scout queries
    ├── raw/                                ← Scout outputs
    ├── processed/                          ← Refinery outputs
    ├── deltas/                             ← Editor outputs (to apply)
    ├── audit/                              ← Audit flags
    └── logs/                               ← Run logs
    
Research/Automated/                         ← New source notes created by Editor
├── 2026-07-14 — Ancient DNA South Asia New Finds.md
├── 2026-07-14 — Dravidian Politics TN Update.md
└── ...
```

---

## Success Metrics

| Metric | Target |
|--------|--------|
| Papers scanned/week | 50+ |
| High-quality papers retained | 3-5 |
| Target notes updated/month | 2+ |
| False positive flags | <10% |
| Manual intervention needed | <15 min/week |

---

## Related Notes

- [[Cross-Domain Idea Synthesis]] — Parent idea
- [[05 - MAPS/AI & Technology MOC]] — Tech project map
- [[05 - MAPS/Indian Political History MOC]] — Politics map
- [[05 - MAPS/Philosophy & Religion MOC]] — Philosophy map
- [[genericagent/memory/autonomous_operation_sop.md]] — Agent framework
- [[house-rules.md]] — Night Shift rules
- [[Research/AI Tools/2026-06-19 — AI-Specific Researcher Tools 2026 — Complete Table.md]] — Tool reference

---

**Status:** 🟢 Active — Week 1 deliverables (2026-07-14) completed late (2026-07-11)
**First Scout Run:** Monday 2026-07-13 02:00 IST