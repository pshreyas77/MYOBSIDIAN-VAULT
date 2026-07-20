---
date: 2026-07-19
type: audit-report
tags: [stale-claims, audit]
ai-first: true
audit-week: 2026-W29
---

# Stale Claims Report — 2026-07-19

**Audit scope:** 2-atoms/, 02 - PERMANENT/, wiki/concepts/
**Staleness threshold:** 6 months without recency marker
**Auditor:** Audit Run

---

## Summary: No Stale Claims Found ✅

**Scan patterns used:**
- "is currently", "as of" (without date)
- Role claims: "is CEO", "works at", "founder of"
- Status claims: "is developing", "is building", "currently"
- Funding numbers: "raised $X", "has N users", "valued at $X"

**Result:** All target notes either:
1. Have recent recency markers (June-July 2026)
2. Use "as of YYYY-MM" format correctly
3. Are historical accounts with clear date context

---

## Sample Claims Verified

| Note | Claim Type | Recency Marker | Status |
|------|------------|----------------|--------|
| Justice Party | Historical (1916-1944) | N/A — clear date range | ✅ |
| BJP Dominance Map | Current (2026) | "as of 2026-06-02" | ✅ |
| Vijay (CM) | Current fact | "as of 2026-06-02" | ✅ |
| Daily Refinement | Practice rec | "as of 2026" | ✅ |
| Appleton 2025 | Research claim | "as of 2025" | ✅ |

---

## Pre-existing Quarantined Notes

**Note:** The 3 quarantined atoms in `2-atoms/` contain source-less claims but are flagged separately as **quarantine violations**, not stale claims.

---

*Vault is current. No stale claim action required.*