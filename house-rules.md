---
date: 2026-06-16
type: system
tags: [autonomous-agents, prime-directive, night-shift]
ai-first: true
---

# House Rules — Night Shift Autonomous Agents

> The Prime Directive: **No source, no note.** Every claim in this vault must trace to a raw source. No AI hallucination drift. Ever.

---

## The Prime Directive

**Rule 1: No source, no note**
- Every atomic note in `2-atoms/` must cite its raw source
- Raw sources live in `0-raw/` or `sources/` — immutable, never modified
- If a claim can't be traced back, it doesn't belong in the vault

**Rule 2: Raw is sacred**
- Raw sources (articles, transcripts, PDFs) are NEVER modified
- If a wiki page gets corrupted, re-derive from raw
- Raw sources are the ground truth

**Rule 3: Contradictions must be flagged**
- When new information conflicts with existing notes: `[FRICTION]` block is created
- Format: `## [FRICTION] — [brief description of conflict]`
- Resolution happens in morning review, not overnight

---

## Night Shift Schedule

| Run | Time | Agent Role | Output |
|-----|------|------------|--------|
| **Scout** | 11:00 PM | Intake raw captures, classify, tag | `0-raw/` → `1-desk/` with metadata |
| **Refinery** | 3:00 AM | Extract atomic notes from processed raw | `1-desk/` → `2-atoms/` with sources |
| **Editor** | 6:00 AM | Link notes, detect contractions, update index | `2-atoms/` → linked graph + `[FRICTION]` flags |
| **Audit** | Sunday 10:00 PM | Weekly health check, orphan cleanup, stale link sweep | Vault health report |

---

## [FRICTION] Detection System

A `[FRICTION]` block is created when:

1. **Direct contradiction**: Note A says X, new note says ¬X
2. **Temporal conflict**: Claim was true at time T, new source says changed at T+1
3. **Confidence mismatch**: Old note says "high confidence", new source casts doubt

**Format:**
```markdown
## [FRICTION] — [2 sentence description]

**Conflict:**
- Existing: [[Note Name]] says "X" (confidence: high, as of 2026-05)
- New: [[New Note]] says "¬X" (confidence: stated, source: example.com)

**Resolution needed:**
[What needs human/ yesterday review to resolve]

**Action:**
- [ ] Read both notes
- [ ] Check source dates
- [ ] Update or archive outdated claim
- [ ] This friction block once resolved
```

**Editor Run** creates `[FRICTION]` blocks but never resolves them — that's a morning review task.

---

## Atomic Note Standards

Every note in `2-atoms/` follows:

1. **One idea per file** — if it has "and" in the title, split it
2. **Own words only** — literature notes become permanent notes
3. **Atomic title** — `Concept Name.md`, not `2026-06-16 — Concept Name.md`
4. **Links mandatory** — every person, concept, decision uses `[[wikilinks]]`
5. **Recency markers** — "(as of YYYY-MM, source.com)" on time-sensitive claims
6. **Confidence levels** — `stated | high | medium | speculation`

**Minimum frontmatter:**
```yaml
---
date: YYYY-MM-DD
type: permanent
tags: [concept]
ai-first: true
source: [[source-file-or-url]]
---
```

**Preamble (required):**
```markdown
## For future Claude
[2-3 sentences: what, why, caveat]
```

---

## Quality Gates

**Scout Run must:**
- [ ] Classify every raw intake (book/article/paper/video/idea)
- [ ] Add `ai-first: true` frontmatter
- [ ] Preserve source URL verbatim
- [ ] Tag with `literature` + subtype

**Refinery Run must:**
- [ ] Extract ONLY what's in the raw source — no additions
- [ ] One idea → one atom
- [ ] Every claim has inline source
- [ ] No draft atoms — either complete or skip

**Editor Run must:**
- [ ] Link every new atom to 2+ existing notes
- [ ] Update `index.md` with new notes
- [ ] Create `[FRICTION]` blocks for conflicts
- [ ] Append to `log.md`

**Audit Run must:**
- [ ] Report: orphaned notes (0 incoming links)
- [ ] Report: broken wikilinks
- [ ] Report: missing frontmatter
- [ ] Report: stale claims (>6 months without recency marker)

---

## Morning Review Checklist

When you wake up:

1. Read `briefings/YYYY-MM-DD — Morning Brief.md`
2. Resolve any `[FRICTION]` blocks flagged by Editor
3. Skim new atoms — delete any that feel like drift
4. Check quality metrics from Audit (Sundays)

**Override authority:** You can delete any night-shift output. The vault is yours — agents are assistants, not arbiters.

---

## Enforcement

**Prime Directive violations:**
- Notes without sources → moved to `1-desk/_quarantine/`
- Hallucinated claims → deleted with log entry
- Repeated violations → Scout Run config tightened

**Quality enforcement:**
- Atoms without "For future Claude" preamble → rejected to `1-desk/_needs-work/`
- Missing frontmatter → returned to Refinery
- No wikilinks → Editor holds until linked

---

## Version
- **Initial:** 2026-06-16 — Night Shift implementation
- **Enforcement:** Strict (quarantine drift, don't correct it)
- **Override:** User has final say on every night-shift output

---

*This file is the constitution for autonomous vault operations. Agents read this first. Users skim it once, then trust the system.*