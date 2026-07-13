# History Watchdog — Run Log

## Overview
History Watchdog is an autonomous historiography monitoring agent. It runs weekly research queries across 4 domains, filters for quality, and generates delta-updates to keep your vault's historical notes current.

**Started:** 2026-07-11 (spec from 2026-07-08 Cross-Domain Synthesis)
**Status:** 🟢 Active

---

## Pipeline

| Stage | Schedule | Tool | Status |
|-------|----------|------|--------|
| Scout | Monday 02:00 IST | Elicit + Undermind + DeepSeek + Kimi | 🟢 Active (cron) |
| Refinery | Monday 04:00 IST (auto after Scout) | Venue filter + Scite.ai | ⬜ Pending |
| Editor | Monday 06:00 IST (auto after Refinery) | genericagent SOP | ⬜ Pending |
| Audit | Sunday 22:00 IST weekly | Vault claim check | ⬜ Pending |

---

## Directory Structure

```
03 - PROJECTS/History-Watchdog/
├── queries.yaml          ← All query sets + venue filter + target notes (READY)
├── raw/                  ← Scout JSON outputs
├── processed/            ← Refinery filtered outputs
├── deltas/               ← Editor delta-updates (to apply manually)
├── audit/                ← Audit flags (superseded/disputed claims)
├── logs/                 ← Run logs
└── SPEC.md               ← Full spec (in 03 - PROJECTS/History-Watchdog.md)
```

---

## Query Summary

| Category | Queries | Priority |
|----------|---------|----------|
| Aryan Migration / IVC / Ancient DNA | 8 | 🔴 Critical |
| Dravidian Politics / Tamil Nadu | 8 | 🔴 Critical |
| RSS / Hindutva Funding | 6 | 🟡 High |
| Anti-Caste / Shramana Traditions | 4 | 🟡 High |
| **Total** | **26** | |

---

## Run History

### [2026-07-14] Scout Run — Week 2
- **Run date:** 2026-07-14 | **Source:** OpenAlex API (free, no auth required)
- **Queries run:** 16 (out of 24 in queries.yaml — 2 queries failed due to NoneType in primary_location)
- **Papers found:** 67 total | **Tier1 papers:** 18

#### Category Breakdown
| Category | Queries | Papers | Top Paper |
|----------|---------|--------|-----------|
| aryan_migration | 7 | 35 | AADR 2024 (362 citations, Scientific Data) |
| dravidian_politics | 4 | 16 | Caste Management Review (32 citations, Academy of Management Annals) |
| rss_hindutva | 3 | 12 | Diasporic geopolitics (20 citations, Review of International Studies) |
| anti_caste | 2 | 4 | Buddhism Dalit India (low-citation, non-tier1) |

#### Tool Status
| Tool | Status | Notes |
|------|--------|-------|
| Elicit.org | 🔴 Down | Requires login/signup |
| Undermind.ai | 🔴 Unreachable | Browser connection failed |
| DeepSeek.com | 🔴 Unreachable | Browser connection failed |
| Perplexity.ai | 🔴 Blocked | Cloudflare bot protection |
| Kimi.com | 🔴 Unreachable | Requires login |
| Semantic Scholar | 🔴 Down | 405 errors on all pages |
| **OpenAlex API** | 🟢 Success | Used as primary fallback |

#### Output
- `raw/2026-07-14-scout.json` — 67 papers, 18 tier1
- Tier1 venues found: Nature (×2), Science, Current Biology, Scientific Data

#### Issues
- 2 political queries failed (NoneType in `primary_location` — likely OpenAlex data gaps for Indian political content)
- anti_caste/Shramana query returned 0 results — need different terminology
- 8 queries from original queries.yaml not run (Mitanni treaty, IVC migrationHarappan, Justice Party exact, Periyar, Dravidian ideology, RSSBhutada, Sewa International, BJP South India)

---

### [2026-07-11] Initialization
- `queries.yaml` created with all 26 queries across 4 categories
- Weekly cron job created: Monday 02:00 IST (first run: 2026-07-13)
- Week 1 deliverable (queries.yaml) marked ✅ — was overdue since 2026-07-14

---

## Next Run
**Monday 2026-07-20 02:00 IST** — Week 3 Scout Run

Recommendations for next run:
- Add CrossRef API as secondary source (good for humanities/politics papers)
- Try arXiv q-bio.GN for preprint genetics papers
- Fix NoneType errors in search_oa() with defensive coding
- Run all 24 original queries from queries.yaml (only 16 were run this week)

Expected output:
- 24 queries across 4 tools
- ~80 papers scanned → ~8 high-quality tier1 papers retained
- JSON report at `raw/2026-07-20-scout.json`
- Log entry at `logs/2026-07-20-run-log.md`

---

## Related

- [[History-Watchdog]] — Project hub (spec)
- [[Cross-Domain Idea Synthesis]] — Parent note
- [[05 - MAPS/Indian Political History MOC]] — Politics map (target note)
- [[05 - MAPS/Philosophy & Religion MOC]] — Philosophy map (target note)