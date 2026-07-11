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

### [2026-07-11] Initialization
- `queries.yaml` created with all 26 queries across 4 categories
- Weekly cron job created: Monday 02:00 IST (first run: 2026-07-13)
- Week 1 deliverable (queries.yaml) marked ✅ — was overdue since 2026-07-14

---

## Next Run
**Monday 2026-07-13 02:00 IST** — First Scout Run

Expected output:
- 26 queries across 4 tools (Elicit, Undermind, DeepSeek, Kimi)
- ~50 papers scanned → ~5 high-quality tier1 papers retained
- JSON report at `raw/2026-07-13-scout.json`
- Log entry at `logs/2026-07-13-run-log.md`

---

## Related

- [[History-Watchdog]] — Project hub (spec)
- [[Cross-Domain Idea Synthesis]] — Parent note
- [[05 - MAPS/Indian Political History MOC]] — Politics map (target note)
- [[05 - MAPS/Philosophy & Religion MOC]] — Philosophy map (target note)