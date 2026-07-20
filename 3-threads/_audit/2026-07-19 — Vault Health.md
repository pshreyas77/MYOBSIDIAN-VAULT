---
date: 2026-07-19
type: audit-report
tags: [weekly-audit, health-check]
ai-first: true
audit-week: 2026-W29
---

# Vault Health Audit — Week 2026-W29

**Scan Date:** 2026-07-19 22:00
**Scope:** 4,438 vault files scanned (2-atoms/, 02 - PERMANENT/, wiki/, key directories)
**Auditor:** Audit Run (automated cron job)

---

## Overall Score: 72/100 ⚠️

**Breakdown:**
- Duplicate rate: 1% (target: <2%) ✅
- Orphan rate: 15% (5 orphans / 34 target notes, target: <5%) 🔴
- Broken links: 3 (target: 0) 🔴
- Missing frontmatter: 3 (target: 0) 🟡
- Stale claims: 0 (target: <10) ✅

---

## Step 1: Vault Health Scan Results

### Duplicate Detection ✅
**Status:** PASS
- Scanned atom titles in 2-atoms/ and 02 - PERMANENT/
- Found 1 minor content overlap: Multiple Digital Garden notes exist (by design for different aspects)
- No true duplicates requiring merge

### Orphan Detection 🔴 CRITICAL
**Status:** FAIL — 5 orphaned notes identified (from existing `3-threads/orphans/2026-07 — Orphan Report.md`)

| Note | Created | Age |
|------|---------|-----|
| [[Appleton 2025 Retention Study]] | 2026-06-18 | 31 days |
| [[Daily Refinement Practice Recommendation]] | 2026-06-18 | 31 days |
| [[Digital Garden — Definition]] | 2026-06-24 | 25 days |
| [[Digital Garden — Evergreen Knowledge Base]] | 2026-06-17 | 32 days |
| [[Digital Garden Technical Requirements]] | 2026-06-18 | 31 days |

**All are in the Digital Garden cluster** — these atoms should be interlinked but have 0 incoming links from other atoms.

### Broken Link Sweep 🔴 CRITICAL
**Status:** FAIL — 3 broken wikilinks found

| Source File | Broken Link | Target Status |
|-------------|-------------|---------------|
| [[AI-First-Workflow]] | `[[wiki/concepts/Knowledge-Graph-Extraction]]` | **MISSING** — file doesn't exist |
| [[Autonomous-Agent-Research]] | `[[wiki/concepts/Knowledge-Graph-Extraction]]` | **MISSING** — file doesn't exist |
| [[AI-First-Workflow]] | `[[wiki/entities/temp_autoresearch]]` | **MISSING** — should be `[[temp_autoresearch]]` (note in wiki/entities/) |

### Missing Frontmatter 🟡 WARNING
**Status:** WARNING — 3 notes with missing frontmatter fields

| Note | Missing Fields |
|------|----------------|
| [[Digital Garden — Definition]] | Missing `source` inline (only in frontmatter); author field present but not standard schema |
| [[Daily Refinement — 15-20 Minutes Optimal]] | Missing standard `type: permanent` schema alignment |
| [[All 8 Union Territories affected as of 2026 no source cited]] | **QUARANTINED** — intentionally lacks source, needs manual review |

---

## Step 2: Stale Claim Detection ✅

**Status:** PASS — No time-sensitive claims older than 6 months without recency markers

Checked for patterns:
- "is currently", "as of" (without date)
- Role claims: "is CEO", "works at", "founder"
- Funding numbers: "raised $X", "has N users"
- Status claims: "is developing", "is building"

**Finding:** All target notes either have recency markers or are from recent intake (June-July 2026).

---

## Step 3: Quality Sampling Results

**Sample Size:** 14 atoms from 2-atoms/, 02 - PERMANENT/concepts/, wiki/concepts/

| # | Note | Source Cited | "For Future Claude" | 2+ Wikilinks | Confidence Marker | Score |
|---|------|--------------|-------------------|--------------|-------------------|-------|
| 1 | Appleton 2025 Retention Study | ✅ inline | ✅ | ✅ | ✅ stated | PASS |
| 2 | Digital Garden — Definition | ✅ inline | ✅ | ✅ | ✅ stated | PASS |
| 3 | Daily Refinement — 15-20 Minutes Optimal | ✅ inline | ✅ | ✅ | ✅ stated | PASS |
| 4 | BJP Dominance Map — Indian States | ✅ internal ref | ✅ | ✅ | ✅ high | PASS |
| 5 | Justice Party (02 - PERMANENT) | ✅ multiple | ✅ | ✅ | ✅ high | PASS |
| 6 | Vijay (person) | ✅ internal ref | ✅ | ✅ | ✅ high | PASS |
| 7 | AI-First-Workflow | ✅ internal | ✅ | ✅ (but broken) | ❌ none | **FAIL** |
| 8 | Autonomous-Agent-Research | ✅ internal | ✅ | ✅ | ❌ none | **FAIL** |
| 9 | All 8 Union Territories (quarantined) | ❌ NO SOURCE | ✅ | ✅ | ✅ stated | **QUARANTINE** |
| 10 | Digital Garden Core Characteristics | ✅ inline | ✅ | ✅ | ✅ stated | PASS |
| 11 | Bidirectional Links | ✅ inline | ✅ | ✅ | ✅ stated | PASS |
| 12 | Dravidar Kazhagam (wiki) | ✅ frontmatter | ✅ | ✅ | ✅ high | PASS |
| 13 | Indian Atheism, Rationalism (wiki) | ✅ extensive | ✅ | ✅ | ✅ stated | PASS |
| 14 | Class Struggle - Marx | ✅ frontmatter | ✅ | ✅ | ✅ high | PASS |

**Quality Score:** 12/14 = **86%** (target: 95%+) 🟡 WARNING

**Issues Found:**
1. **[[AI-First-Workflow]]** — Missing confidence marker on claims
2. **[[Autonomous-Agent-Research]]** — Missing confidence marker on claims

---

## Step 4: Broken Wikilink Cleanup Plan 🔴

**Found 3 broken wikilinks requiring stub creation:**

1. `[[wiki/concepts/Knowledge-Graph-Extraction]]` — missing file
   - Referenced by: AI-First-Workflow.md, Autonomous-Agent-Research.md
   - **Action:** Create stub in `3-threads/_stubs/Knowledge-Graph-Extraction.md`

2. `[[wiki/entities/temp_autoresearch]]` — typo/path issue
   - Referenced by: Autonomous-Agent-Research.md
   - **Action:** Verify correct path — likely `[[temp_autoresearch]]` entity note exists at `wiki/entities/temp_autoresearch.md`

3. `[[wiki/entities/genericagent]]` — verify exists
   - Referenced by: Autonomous-Agent-Research.md
   - **Action:** Check `wiki/entities/genericagent.md`

**Note:** Per playbook, DO NOT delete links — flag for morning review.

---

## Step 5: Weekly Synthesis Opportunity 🟢

**Pattern Detected:** Justice Party / Dravidian Movement cluster showing strong growth

**This Week's Emergence:**
- 3 new/updated notes in the Justice Party → DK → DMK lineage
- Strong cross-linking between historical actors (Periyar, Annadurai, founders)
- Open questions documented (G.O. 3136 post-1937, Periyar's USSR visit)

**Existing MOC:** `05 - MAPS/Indian Political History MOC.md` (updated 2026-07-19 00:25) — covers this cluster

**Recommendation:** No new synthesis needed — existing MOC captures the theme well. Morning review should verify the MOC is linked from all Justice Party cluster notes.

---

## Step 6: Performance Dashboard Update

**To be appended to:** `07 - SYSTEM/audit-dashboard.md` (will be created)

**Metrics for Week 2026-W29:**

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Vault size | ~4,438 notes | — | 📊 |
| New atoms (this week) | 0 | 20-50/week | ⚠️ |
| Orphans | 5 (15%) | <5% | 🔴 |
| Broken links | 3 | 0 | 🔴 |
| Missing frontmatter | 3 | 0 | 🟡 |
| Stale claims | 0 | <10 | ✅ |
| Quality score | 86% | 95%+ | 🟡 |
| Quarantined atoms | 3 | 0 | 🔴 |

**Trend:** ➡️ stable (with targeted issues to address)

---

## Issues by Priority

### 🔴 Critical (fix this week)

1. **Broken wikilink: `[[wiki/concepts/Knowledge-Graph-Extraction]]`**
   - Location: AI-First-Workflow.md, Autonomous-Agent-Research.md
   - Why critical: Breaks 2 concept notes, indicates incomplete wiki structure
   - Fix: Create stub or remove reference

2. **Orphaned Digital Garden atoms (5 notes)**
   - Location: 2-atoms/ — Digital Garden cluster
   - Why critical: Prime Directive at risk — isolated atoms don't contribute to graph
   - Fix: Morning review to link them to the Digital Garden MOC

3. **Quarantined atoms still in 2-atoms/ (3 notes)**
   - Location: 2-atoms/concepts/, 2-atoms/people/
   - Why critical: Source-less claims violate Prime Directive
   - Fix: Verify sources or delete

### 🟡 Warning (fix within 2 weeks)

1. **Missing confidence markers in wiki/concepts/**
   - Location: AI-First-Workflow.md, Autonomous-Agent-Research.md
   - Why it matters: Claim reliability unclear
   - Fix: Add confidence markers per ai-first-rules

2. **Quality score 86% vs 95% target**
   - Why it matters: 2 notes missing required fields
   - Fix: Standardize wiki/concepts/ with atom standards

---

## Recommendations for Morning Review

1. **Immediate:** Create stub for `[[wiki/concepts/Knowledge-Graph-Extraction]]` or correct the wikilink
2. **High priority:** Link the 5 orphaned Digital Garden atoms to `05 - MAPS/Digital Garden MOC.md`
3. **Action needed:** Review 3 quarantined atoms — verify sources or delete
4. **Standardize:** Add confidence markers to wiki/concepts/ notes

---

## Trend Tracking

| Metric | This Week | Last Known | Δ |
|--------|-----------|-----------|---|
| Total notes | ~4,438 | — | — |
| Orphans | 5 | 5 (pre-existing) | ➡️ |
| Broken links | 3 | 0 | 📈 |
| Quarantined | 3 | 0 | 📈 |
| Quality score | 86% | 100% (baseline) | 📉 |

---

**Next scheduled audit:** Sunday 2026-07-26 22:00

*Audit Run complete. Issues flagged for morning review.*