---
date: 2026-07-19
type: audit-report
tags: [broken-links, cleanup]
ai-first: true
audit-week: 2026-W29
---

# Broken Links Report — 2026-07-19

**Source scan:** wiki/concepts/, 2-atoms/, 02 - PERMANENT/concepts/
**Auditor:** Audit Run

---

## Broken Wikilinks Found: 3

### 1. `[[wiki/concepts/Knowledge-Graph-Extraction]]` 🔴

**Status:** TARGET FILE MISSING

**Referenced by:**
- `wiki/concepts/AI-First-Workflow.md` (line 83)
- `wiki/concepts/Autonomous-Agent-Research.md` (line 61)

**Discovery:** Link to `Knowledge-Graph-Extraction.md` in `wiki/concepts/` — file does not exist in vault

**Stub created:** `3-threads/_stubs/Knowledge-Graph-Extraction.md`

---

### 2. `[[wiki/entities/temp_autoresearch]]` 🟡

**Status:** PATH ISSUE — entity exists but link format incorrect

**Referenced by:**
- `wiki/concepts/Autonomous-Agent-Research.md` (line 24)

**Discovery:** Entity file exists at `wiki/entities/temp_autoresearch.md` but link format uses `wiki/entities/` prefix unnecessarily

**Suggested fix:** Change `[[wiki/entities/temp_autoresearch]]` to `[[temp_autoresearch]]`

---

### 3. `[[wiki/entities/genericagent]]` 🟢

**Status:** VERIFY — file may exist

**Referenced by:**
- `wiki/concepts/Autonomous-Agent-Research.md` (line 30)

**Discovery:** Check if `wiki/entities/genericagent.md` exists

**Action:** Verify and update link format if needed

---

## Action Items for Morning Review

- [ ] **CRITICAL:** Approve stub creation for `Knowledge-Graph-Extraction.md` OR correct links to point to existing note
- [ ] Fix path format for `temp_autoresearch` link
- [ ] Verify `genericagent` link resolves

---

*Per playbook: Broken links flagged, not deleted. Morning review decides.*