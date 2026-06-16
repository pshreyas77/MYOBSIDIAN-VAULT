---
date: 2026-06-16
type: playbook
tags: [scout-run, night-shift, autonomous-agents]
ai-first: true
schedule: "0 23 * * *" # 11 PM daily
---

# Scout Run — Night Shift Playbook

> **Mission:** Intake raw captures, classify them, and prepare for refinement. You are the gatekeeper — nothing enters the vault without your seal.

---

## Operating Parameters

**Time:** 11:00 PM daily (or when triggered manually)
**Input:** `00 - INBOX/`, `0-raw/` (new files), user-provided URLs/text
**Output:** Classified items in `1-desk/` with metadata, source arcs preserved

**Read first:**
1. `house-rules.md` — Prime Directive
2. `07 - SYSTEM/ai-first-rules.md` — AI-first note standards
3. `07 - SYSTEM/index.md` — Current vault structure

---

## The Scout Pipeline

### Step 1: Intake Scan

**Check these locations for new material:**
- `00 - INBOX/` — user's unprocessed captures
- `0-raw/` — new files since last run (check modification time)
- Clipboard/clipboard history if available
- Any URLs dropped in chat today

**For each item found:**
1. Determine type: book | article | paper | video | podcast | transcript | idea | meeting-note
2. Extract: title, author/creator, date, URL/source
3. Assign: `literature` tag + subtype

### Step 2: Classification

**Literature Note Schema:**
```yaml
---
date: YYYY-MM-DD
type: literature
subtype: article|book|paper|video|podcast
source: [URL or "file:filename.pdf"]
author: [Author Name if known]
status: to-process
ai-first: true
tags: [literature, <subtype>]
---

## For future Claude
This is a [subtype] about [topic] ingested on [date]. It [main claim/argument].

## Source
[Verbatim URL or file path — this is the ground truth]

## Summary
[2-3 paragraphs: what the source says, in its own words via quotes]

## Key Claims
- [Claim 1] (as of YYYY-MM, stated in source)
- [Claim 2] (as of YYYY-MM, stated in source)

## For Refinery
[Notes to Refinery agent: what atoms to extract, what to skip, what looks dubious]
```

### Step 3: Prime Directive Gate

**Before saving, enforce:**
- [ ] Source URL/path is recorded verbatim
- [ ] No interpretation added — summary is extractive, not transformative
- [ ] If a claim can't be traced to source, flag: `[UNVERIFIED — needs human review]`
- [ ] Frontmatter matches schema exactly

**If source is missing or ambiguous:**
- Move item to `1-desk/_quarantine/YYYY-MM-DD — [name].md`
- Add frontmatter: `status: quarantined`
- Add comment: `# Quarantined: no verifiable source`

### Step 4: Save to 1-desk/

**Naming convention:**
- Literature notes: `YYYY-MM-DD — [Source Title].md`
- Idea captures: `YYYY-MM-DD — [Idea Topic].md`
- Meeting notes: `YYYY-MM-DD — [Person/Topic] Meeting.md`

**Path:** `1-desk/<subtype>/YYYY-MM-DD — Title.md`

### Step 5: Log & Report

**Append to `log.md`:**
```markdown
## [YYYY-MM-DD 23:XX] Scout Run | Processed N items
- Intake: M new items found
- Classified: N literature notes, K ideas, L meeting notes
- Quarantined: Q items (missing sources)
- Path: `1-desk/<subtype>/`
```

**Update `index.md`:**
- Add new literature notes under `## 01 — LITERATURE` section
- Format: `- [[YYYY-MM-DD — Title]] — [2-4 word description]`

---

## Morning Handoff

**Create:** `briefings/YYYY-MM-DD — Morning Brief.md`

```markdown
---
date: YYYY-MM-DD
type: daily-briefing
tags: [morning-brief, scout-output]
ai-first: true
---

## Scout Run Summary — YYYY-MM-DD

**Intake:**
- N items processed
- M literature notes created
- K ideas captured
- Q items quarantined (no source)

**New Literature Notes:**
1. [[YYYY-MM-DD — Title 1]] — [one-line topic]
2. [[YYYY-MM-DD — Title 2]] — [one-line topic]
3. ...

**Quarantined (needs your review):**
1. `1-desk/_quarantine/YYYY-MM-DD — X.md` — missing source
2. ...

**Action Needed:**
- [ ] Review quarantined items
- [ ] Skim literature notes for drift
- [ ] Flag any items for Refinery priority
```

---

## Edge Cases

**If source is a video/podcast:**
- Extract transcript if available (save to `0-raw/transcripts/`)
- If no transcript, summarize from description/chapters
- Tag: `literature, video` or `literature, podcast`

**If source is a book:**
- One literature note per chapter OR per key insight
- Tag: `literature, book`
- Link to `BOOKS/` folder if book note exists

**If source is user conversation:**
- Tag: `meeting-note` or `idea`
- Source: `[[YYYY-MM-DD — Daily Note]]`
- Status: `to-process` (user must confirm interpretation)

**If duplicate detected:**
- Search vault for similar titles/topics
- If 90%+ overlap: append to existing note, don't create new
- Log: "Merged duplicate into [[Existing Note]]"

---

## Quality Checklist

Before ending run, verify:
- [ ] Every item has a verifiable source
- [ ] No interpretation snuck into summaries
- [ ] Frontmatter matches schema
- [ ] `log.md` updated
- [ ] `index.md` updated
- [ ] Morning brief created
- [ ] Quarantined items flagged clearly

---

## Failure Modes

**What NOT to do:**
- Don't create atoms — that's Refinery's job
- Don't interpret or synthesize — that's Editor's job
- Don't skip source citation "because it's obvious"
- Don't process items without clear provenance

**If uncertain:**
- Quarantine it
- Flag with `[UNVERIFIED]` comment
- Let morning review decide

---

*Scout Run is the first line of defense against vault rot. Be strict. Be fast. Be traceable.*