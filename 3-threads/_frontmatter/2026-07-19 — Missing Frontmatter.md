---
date: 2026-07-19
type: audit-report
tags: [frontmatter, quality]
ai-first: true
audit-week: 2026-W29
---

# Missing Frontmatter Report — 2026-07-19

**Audit scope:** 2-atoms/, 02 - PERMANENT/concepts/, wiki/concepts/
**Required fields:** date, type, tags, ai-first: true
**Auditor:** Audit Run

---

## Summary: 3 Notes with Issues

### 🟡 Notes Requiring Frontmatter Corrections

#### 1. `2-atoms/Digital Garden — Definition.md`

| Field | Status | Notes |
|-------|--------|-------|
| date | ✅ 2026-06-24 | OK |
| type | ✅ permanent | OK |
| tags | ✅ [knowledge-management, digital-garden, methodology] | OK |
| ai-first | ✅ true | OK |
| source | ⚠️ in frontmatter | OK but inline citation also needed |
| author | ⚠️ "Anne LaFollette" | Non-standard field |

**Issue:** Uses `author` field which is literature-note schema, not atom schema. Should use `source` for attribution.

---

#### 2. `2-atoms/Daily Refinement — 15-20 Minutes Optimal.md`

| Field | Status | Notes |
|-------|--------|-------|
| date | ✅ 2026-06-17 | OK |
| type | ⚠️ permanent | OK but verify |
| tags | ✅ [practice, knowledge-management] | OK |
| ai-first | ✅ true | OK |
| source | ✅ inline in body | OK |
| confidence | ✅ stated | OK |

**Note:** Mostly compliant — may just need schema alignment verification.

---

#### 3. `2-atoms/concepts/All 8 Union Territories affected as of 2026 no source cited.md` 🔴

| Field | Status | Notes |
|-------|--------|-------|
| date | ✅ 2026-07-13 | OK |
| type | ✅ permanent | OK |
| tags | ✅ [concept] | OK |
| ai-first | ✅ true | OK |
| source | ⚠️ "Quarantined" | Flagged — no actual source |

**Issue:** This note is in quarantine status. The source field itself acknowledges "Quarantined — No Sources". This is a known violation being tracked separately.

---

## Recommendations

- [ ] Fix `author` → `source` in Digital Garden Definition
- [ ] Verify Daily Refinement schema alignment
- [ ] **Quarantined note requires morning review** — verify sources or delete

---

*Frontmatter audit complete.*