---
date: 2026-07-19
type: system
tags: [audit-dashboard, weekly-metrics]
ai-first: true
---

# Audit Dashboard

> Weekly vault health metrics. Updated every Sunday by Audit Run.

---

## Week 2026-W29 (2026-07-19)

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Vault size | ~4,438 notes | — | 📊 |
| New atoms (this week) | 0 | 20-50/week | ⚠️ Low intake |
| Orphans | 5 (15% of target notes) | <5% | 🔴 |
| Broken links | 3 | 0 | 🔴 |
| Missing frontmatter | 3 | 0 | 🟡 |
| Stale claims | 0 | <10 | ✅ |
| Quality score | 86% | 95%+ | 🟡 |
| Quarantined atoms | 3 | 0 | 🔴 |

**Overall Score:** 72/100 ⚠️

**Trend:** ➡️ stable (with targeted issues to address)

---

## Week 2026-W25 (2026-06-16) — Baseline

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Vault size | ~2,500 notes | — | 📊 |
| New atoms | 2 (test cycle) | 20-50/week | ⚠️ |
| Orphans | 0 | <5% | ✅ |
| Broken links | 0 | 0 | ✅ |
| Missing frontmatter | 0 | 0 | ✅ |
| Stale claims | 0 | <10 | ✅ |
| Quality score | 100% | 95%+ | ✅ |

**Overall Score:** 100/100 ✅

---

## Trend Analysis

| Metric | W25 | W29 | Δ |
|--------|-----|-----|---|
| Vault growth | ~2,500 | ~4,438 | 📈 +1,938 |
| Orphans | 0 | 5 | 📈 (degrading) |
| Broken links | 0 | 3 | 📈 (degrading) |
| Quality score | 100% | 86% | 📈 (degrading) |

**Analysis:** Vault grew significantly but quality infrastructure (linking, frontmatter) didn't scale with it. Night Shift agents reported 0 atoms processed in recent weeks — pipeline may need attention.

---

## Open Issues

### Critical (unresolved)

1. **3 broken wikilinks** — stub created for Knowledge-Graph-Extraction
2. **5 orphaned Digital Garden atoms** — need linking to MOC
3. **3 quarantined atoms** — source verification needed or deletion

### Warning (in progress)

1. **Quality score 86%** — 2 wiki/concepts/ notes missing confidence markers
2. **Frontmatter schema** — `author` field used in atom instead of `source`

---

## Audit Reports Location

All reports in `3-threads/_audit/`:
- `2026-06-16 — Vault Health Report.md` (baseline)
- `2026-07-19 — Vault Health.md` (current)

---

*Dashboard created 2026-07-19 by Audit Run*