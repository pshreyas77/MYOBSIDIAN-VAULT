---
date: 2026-06-16
type: playbook
tags: [refinery-run, night-shift, autonomous-agents]
ai-first: true
schedule: "0 3 * * *" # 3 AM daily
---

# Refinery Run — Night Shift Playbook

> **Mission:** Extract atomic notes from literature notes. One idea → one file. No interpretation, no drift. You are the alchemist turning raw ore into pure elements.

---

## Operating Parameters

**Time:** 3:00 AM daily (after Scout completes)
**Input:** `1-desk/` (items with `status: to-process`), `house-rules.md`
**Output:** Atomic notes in `2-atoms/`, archived sources in `sources/`

**Read first:**
1. `house-rules.md` — Prime Directive (NO SOURCE, NO NOTE)
2. `07 - SYSTEM/ai-first-rules.md` — Frontmatter schemas
3. Literature notes from Scout Run

---

## The Refinery Pipeline

### Step 1: Source Verification

**For each literature note in `1-desk/`:**

1. **Verify the source exists:**
   - URL is reachable (if online)
   - File exists in `0-raw/` or `sources/`
   - If source is missing: flag `[SOURCE MISSING — cannot refine]` and skip

2. **Check Scout's classification:**
   - `status: to-process` → proceed
   - `status: quarantined` → skip (already flagged)
   - `status: processed` → skip (already refined)

### Step 2: Atomic Extraction

**The Prime Directive in action:**

For each claim/idea in the literature note:

```markdown
## Extraction Rules

1. **One idea per file** — if the title would have "and", split it
2. **Own words only** — paraphrase, don't quote (unless the quote IS the idea)
3. **Source citation mandatory** — inline, verbatim
4. **No additions** — if it's not in the source, it doesn't go in the atom
5. **Confidence marker** — `stated` (direct from source) or `speculation` (inference)
```

**Atomic Note Template:**

```yaml
---
date: YYYY-MM-DD
type: permanent
tags: [concept]
ai-first: true
source: [[YYYY-MM-DD — Source Title]]
related: [["Person Name"]], [["Related Concept"]]
---

## For future Claude
This note explains [concept] extracted on [date] from [source]. It covers [one idea].

## [Concept Name]

[2-4 paragraph explanation in your own words — one idea only]

**Key claim:** [The central assertion] (as of YYYY-MM, stated in [[source]])

## Evidence
> "[Direct quote from source that supports this]" 
> — [[Source Title]], [URL or path]

## Links
- Related: [[Related Concept 1]], [[Related Concept 2]]
- Contrasts with: [[Opposing View]] (if applicable)
- Builds on: [[Foundational Concept]]

## Confidence
stated | high | medium | speculation ← circle one

## Metadata
- Extracted from: [[YYYY-MM-DD — Source Title]]
- Raw source: [URL or file path]
- Extracted by: Refinery Run, YYYY-MM-DD
```

### Step 3: Naming Convention

**Atomic note titles:**
- Concepts: `Concept Name.md` (e.g., `Justice Party.md`)
- People: `Person Name.md` (e.g., `T. M. Nair.md`)
- Events: `Event Name (YYYY).md` (e.g., `Justice Party Founding (1916).md`)
- Questions: `Question?` (e.g., `What caused the Dravidian Movement?.md`)

**NEVER use:**
- `2026-06-16 — Concept Name.md` (that's for literature/daily notes)
- `Notes on Concept.md` (be direct)
- `Concept_Definition.md` (no underscores in titles)

### Step 4: Source Archival

**After extracting atoms:**

1. Move literature note from `1-desk/` to `sources/archived/YYYY-MM-DD — Title.md`
2. Update frontmatter: `status: processed`
3. Add extraction log:

```markdown
## Extraction Log
- **Date:** YYYY-MM-DD
- **Refinery Run:** Extracted N atomic notes
- **Atoms created:**
  1. [[Concept Name 1]]
  2. [[Concept Name 2]]
  3. [[Person Name]]
```

### Step 5: Log & Report

**Append to `log.md`:**

```markdown
## [YYYY-MM-DD 03:XX] Refinery Run | Extracted N atoms
- Processed: M literature notes from `1-desk/`
- Created: N atomic notes in `2-atoms/`
- Archived: M sources to `sources/archived/`
- Skipped: K items (missing source, already processed)
- [FRICTION] flags: F conflicts detected (passed to Editor)
```

---

## [FRICTION] Detection (Refinery Phase)

**Flag a [FRICTION] block when:**

During extraction, you notice:
- The literature note contradicts an existing atomic note
- Two claims in the same source are mutually exclusive
- A "fact" in the source conflicts with vault knowledge

**Create a friction note in `3-threads/_friction/YYYY-MM-DD — [Topic] Conflict.md`:**

```yaml
---
date: YYYY-MM-DD
type: friction
tags: [contradiction, needs-review]
ai-first: true
related: [["Note A"], ["Note B"]]
---

## [FRICTION] — [Topic] Contradiction

**Detection phase:** Refinery Run, YYYY-MM-DD

**Conflict:**
- Existing vault note [[Note A]] says: "X is true" (confidence: high, as of 2025-03)
- New source [[Source Title]] says: "X is false" (stated, as of 2026-06)

**Possible explanations:**
1. X changed between 2025-03 and 2026-06 (temporal update)
2. One source is unreliable (check credentials)
3. Different contexts (X is true in context A, false in context B)

**Resolution needed:**
[What the morning review should check]

**Action:**
- [ ] Compare dates of both claims
- [ ] Assess source credibility
- [ ] Update or archive outdated claim
- [ ] Delete this friction note once resolved
```

---

## Quality Gates

**Before an atom is saved, verify:**

- [ ] **One idea only** — title doesn't have "and" or ","
- [ ] **Source citation** — inline, verbatim, with date marker
- [ ] **Own words** — not a copy-paste (except labeled quotes)
- [ ] **Wikilinks** — 2+ links to existing vault notes
- [ ] **Confidence marker** — `stated | high | medium | speculation`
- [ ] **"For future Claude" preamble** — 2-3 sentences
- [ ] **Frontmatter complete** — type, tags, source, ai-first: true

**If any check fails:**
- Move atom to `1-desk/_needs-work/YYYY-MM-DD — [Name].md`
- Add comment: `# Needs work: [specific issue]`
- Don't create substandard atoms — better to skip than drift

---

## Morning Handoff

**Append to briefings/YYYY-MM-DD — Morning Brief.md:**

```markdown
---
(refinery section — appended by Refinery Run)
---

## Refinery Run Summary — YYYY-MM-DD

**Extraction:**
- Processed: M literature notes
- Created: N atomic notes
- Archived: M sources
- Skipped: K (missing source/already done)
- Needs work: W atoms (check `1-desk/_needs-work/`)

**New Atomic Notes:**
1. [[Concept Name 1]] — [3-5 word summary]
2. [[Concept Name 2]] — [3-5 word summary]
3. [[Person Name]] — [3-5 word summary]
...

**[FRICTION] Flags (needs your review):**
1. `3-threads/_friction/YYYY-MM-DD — X Conflict.md` — [one-line description]
2. ...

**Action Needed:**
- [ ] Skim new atoms for drift (spot-check 2-3)
- [ ] Resolve [FRICTION] conflicts
- [ ] Review `_needs-work/` items
```

---

## Edge Cases

**If source is low-quality (blog, Twitter, unreferenced claim):**
- Extract with `confidence: speculation`
- Tag: `literature, low-confidence`
- Add comment: `# Source quality: low — verify independently`

**If source is a primary document (speech, legal text, original research):**
- Confidence: `stated` (it's their own words)
- Tag: `literature, primary-source`
- Extract more liberally — primary sources are gold

**If literature note is vague or interpretation-heavy:**
- Go back to raw source if available
- If raw source is unavailable: quarantine the whole item
- Don't refine interpretations — only refine facts

**If duplicate atom detected:**
- Search `2-atoms/` for similar concepts
- If 80%+ overlap: update existing atom with new source, don't create duplicate
- Log: "Updated [[Existing Atom]] with new source [[Source Title]]"

---

## Failure Modes

**What NOT to do:**

- Don't add your own interpretation — extract only what's in the source
- Don't create "summary atoms" — atoms are atomic, not summaries
- Don't skip source citation — even if "everyone knows this"
- Don't refine sources Scout didn't verify — garbage in, garbage out

**If uncertain:**

- Skip the item
- Flag with `[UNVERIFIED — needs human review]`
- Let morning review decide

---

## Performance Metrics

**Good Refinery Run:**
- 80%+ of literature notes processed → atoms
- <5% of atoms need rework
- 0 atoms without source citations
- All [FRICTION] conflicts flagged, none ignored

**Track over time:**
- Atoms per literature note (target: 3-7)
- Quarantine rate (target: <10%)
- [FRICTION] detection rate (target: 1-3 per week)

---

*Refinery Run is where knowledge gets purified. Be precise. Be strict. Be traceable.*