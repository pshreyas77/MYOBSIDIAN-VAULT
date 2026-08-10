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
**Monday 2026-08-17 02:00 IST** — Week 6 Scout Run

Recommendations for next run:
- Add CrossRef API as secondary source (humanities/politics papers)
- Add arXiv q-bio.GN call for preprint-tier1 genetics
- Refine or drop the Mitanni query (low yield — surfaces Mesopotamian papers, not IVC)
- Browser-based tools (Elicit/Undermind/DeepSeek/Kimi) require login or paid plan; recommend retiring them from the pipeline unless user adds budget
- Tier1 venue matching is now strict (exact-equality / canonical-prefix); no further false positives expected

---

### [2026-08-10] Scout Run — Week 5
- **Run date:** 2026-08-10 | **Source:** OpenAlex API (free, no auth)
- **Queries run:** 26 (full queries.yaml coverage)
- **Papers found:** 92 (deduped) | **Tier1 papers:** 11 (after fixing tier1 venue-matching)

#### Category Breakdown
| Category | Queries | Papers | Top Paper |
|----------|---------|--------|-----------|
| aryan_migration | 8 | 34 | AADR 2024 (372 citations, Scientific Data) |
| dravidian_politics | 8 | 26 | "Nation at Repair, Women at Work" (SAMAJ, 11 cites) |
| rss_hindutva | 6 | 19 | "Hindutva in the shadow of the Mahatma" (Modern Asian Studies) |
| anti_caste | 4 | 13 | "Truth clashes" (J. Royal Anthropological Institute, 8 cites) |

#### Tool Status
| Tool | Status | Notes |
|------|--------|-------|
| Elicit.com | 🔴 Blocked | Cloudflare bot-detection ("Just a moment...") |
| Undermind.ai | ⬜ Not attempted | Inherits bot-detection; deprioritized |
| DeepSeek.com | ⬜ Not attempted | Login-walled |
| Kimi.com | ⬜ Not attempted | Login-walled |
| **OpenAlex API** | 🟢 Success | Primary source; 92 papers, 11 tier1 |

#### Standout Findings (for user review)
1. **Cell 2025** — "50,000 years of evolutionary history of India" (Kerdoncuff et al., 33 cites) — India-specific 2,762-genome study, supersedes earlier India population-genomics work.
2. **Nature 2025** — "The genetic origin of the Indo-Europeans" (Lazaridis et al., 92 cites) — New anchor reference for Aryan migration debate.
3. **Modern Asian Studies 2024** — "Hindutva in the shadow of the Mahatma: Golwalkar, Gandhi, and the RSS" — directly relevant to RSS funding/ideology research.
4. **Forum for Development Studies 2024** — "Relocations of Hindutva: Hindu Nationalism Under Modi 3.0" — relevant to post-2024 BJP strategy notes.
5. **Contemporary South Asia 2024** — "The BJP's expansionist strategies in Tamil Nadu (2014–present)" — directly relevant to TN politics MOC.

#### Tier1 papers
11 total: AADR (372), Selection landscape Eurasian (145), Neolithic Denmark genomes (117), Indo-European genetic origins (92), Neanderthal ancestry through time (44), Ancient Plasmodium genomes (40), 50k years India (33), M. leprae genome (28), Avar-period reproductive barrier (27), North Pontic Region genomes (16), Eastern Arabian ancient genomes (8).

#### Issues Fixed
- **Tier1 venue matching** was using substring match — false-positives flagged "Frontiers in Political Science" and "International Journal of Emerging Research in Engineering Science and Management" as tier1. Replaced with strict exact-equality / canonical-prefix match. The 2026-07-14 run was affected by this same bug (reported "18 tier1" when the real count was closer to 10).

#### Output
- `raw/2026-08-10-scout.json` — 92 papers, 11 tier1
- `logs/2026-08-10-run-log.md` — full run log
- `scout_run_2026-08-10.py` + `compile_2026-08-10.py` — reusable scripts

---

### [2026-07-14] Scout Run — Week 2

---

## Related

- [[History-Watchdog]] — Project hub (spec)
- [[Cross-Domain Idea Synthesis]] — Parent note
- [[05 - MAPS/Indian Political History MOC]] — Politics map (target note)
- [[05 - MAPS/Philosophy & Religion MOC]] — Philosophy map (target note)