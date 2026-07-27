---
date: 2026-07-26
type: audit-report
tags: [broken-links, cleanup, weekly-audit]
ai-first: true
audit-week: 2026-W30
---

# Broken Links Report — 2026-07-26

**Source scan:** wiki/concepts/, wiki/entities/, 2-atoms/, 02-PERMANENT/
**Auditor:** Audit Run
**Previous report:** 2026-07-19 (W29) — 3 broken links found, none resolved

---

## Broken Wikilinks Found: 3 🔴 (UNRESOLVED from W29)

### 1. `[[wiki/concepts/Knowledge-Graph-Extraction]]` 🔴 CRITICAL — 7 days old

**Status:** TARGET FILE MISSING

**Referenced by:**
- `wiki/concepts/AI-First-Workflow.md` (line 83)
- `wiki/concepts/Autonomous-Agent-Research.md` (line 61)

**Discovery:** Link to `Knowledge-Graph-Extraction.md` in `wiki/concepts/` — file does not exist in vault.

**W29 stub created:** `3-threads/_stubs/Knowledge-Graph-Extraction.md` (confirmed present)
**Problem:** Stub was created but the actual target file at `wiki/concepts/Knowledge-Graph-Extraction.md` was never written. Broken link has now persisted for 7 days.

**Suggested fix options for morning review:**
- **Option A (preferred):** Write `wiki/concepts/Knowledge-Graph-Extraction.md` with real content — the concept is referenced by 2 notes, suggesting it was intended
- **Option B:** Redirect links to existing related note `[[Autonomous-Agent-Research]]` which covers knowledge graph extraction
- **Option C:** Delete the stub and mark links as intentional but unresolvable

**Action:** [ ] Morning review — choose option and implement

---

### 2. `[[wiki/entities/temp_autoresearch]]` 🟡

**Status:** PATH ISSUE — entity file EXISTS but link format is wrong

**Referenced by:**
- `wiki/concepts/Autonomous-Agent-Research.md` (line 24)

**Discovery:** Entity file exists at `wiki/entities/temp_autoresearch.md` but link uses `[[wiki/entities/temp_autoresearch]]` which adds an extra `wiki/entities/` prefix that Obsidian doesn't resolve.

**Fix:** Change `[[wiki/entities/temp_autoresearch]]` → `[[temp_autoresearch]]`

**Audit's note:** This is a link syntax error, not a missing file. The target exists. Simple fix.

**Action:** [ ] Fix wikilink syntax in Autonomous-Agent-Research.md (line 24)

---

### 3. `[[wiki/entities/genericagent]]` 🟢

**Status:** VERIFY — likely correct path issue

**Referenced by:**
- `wiki/concepts/Autonomous-Agent-Research.md` (line 30)

**Discovery:** Check if `wiki/entities/genericagent.md` exists at the correct path. If it exists with filename `genericagent.md` (not `wiki/entities/genericagent.md`), the link needs the same fix as #2.

**Action:** [ ] Verify entity file exists, [ ] Fix link syntax if needed

---

## Action Items for Morning Review

- [ ] **CRITICAL (7-day-old issue):** Write `wiki/concepts/Knowledge-Graph-Extraction.md` OR approve link redirection
- [ ] Fix `[[wiki/entities/temp_autoresearch]]` → `[[temp_autoresearch]]` in Autonomous-Agent-Research.md
- [ ] Verify `[[wiki/entities/genericagent]]` resolves correctly

---

## Stub Directory Status

| Stub | Created | Status |
|------|---------|--------|
| `3-threads/_stubs/Knowledge-Graph-Extraction.md` | W29 (2026-07-19) | ✅ Created but target never made |

*Per playbook: Broken links flagged, not deleted. Morning review decides.*