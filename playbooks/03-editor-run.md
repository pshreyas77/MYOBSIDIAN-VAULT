---
date: 2026-06-16
type: playbook
tags: [editor-run, night-shift, autonomous-agents]
ai-first: true
schedule: "0 6 * * *" # 6 AM daily
---

# Editor Run — Night Shift Playbook

> **Mission:** Link atomic notes into a knowledge graph, detect contradictions, and update the vault's index. You are the cartographer — making sure every note knows its neighbors.

---

## Operating Parameters

**Time:** 6:00 AM daily (after Refinery completes)
**Input:** `2-atoms/` (new atoms from Refinery), existing vault notes
**Output:** Linked notes, [FRICTION] blocks, updated index, morning brief

**Read first:**
1. `house-rules.md` — Prime Directive & [FRICTION] system
2. `07 - SYSTEM/ai-first-rules.md` — Wikilink standards
3. `07 - SYSTEM/index.md` — Current vault structure

---

## The Editor Pipeline

### Step 1: Link New Atoms

**For each new atom from Refinery Run:**

1. **Read the atom fully** — understand the concept
2. **Search the vault for related notes:**
   - Same concept (synonyms, alternative names)
   - Foundational concepts this builds on
   - Opposing viewpoints
   - People mentioned
   - Projects/contexts where this applies

3. **Add wikilinks to the atom:**
   ```markdown
   ## Links
   - Builds on: [[Foundational Concept]]
   - Related: [[Sibling Concept 1]], [[Sibling Concept 2]]
   - Contrasts with: [[Opposing View]]
   - Applied in: [[Project Name]]
   - Person: [[Person Name]]
   ```

4. **Add backlinks from existing notes:**
   - Read 3-5 related notes
   - If the new atom adds context, add a link:
   ```markdown
   See also: [[New Atom]] — [why it's relevant]
   ```

**Minimum linking standard:**
- Every new atom gets 2+ outgoing links
- Every new atom gets 1+ incoming link (backlink)
- Person mentions always linked
- Concept mentions always linked

### Step 2: [FRICTION] Detection

**Scan for contradictions between:**
- New atoms vs. existing vault knowledge
- Two new atoms from the same Refinery Run
- temporal claims (X was true at T1, ¬X at T2)

**Search patterns:**

```
Same concept, opposite claims:
- "X is Y" vs. "X is not Y"
- "X causes Y" vs. "X prevents Y"
- "X happened in year Y" vs. "X happened in year Z"

Temporal conflicts:
- "X is current (as of 2025)" vs. "X changed in 2026"
- Role changes, status updates, location moves

Confidence conflicts:
- "X (confidence: high)" vs. new source casts doubt
- Well-established fact challenged by new evidence
```

**When [FRICTION] is detected:**

Create `3-threads/_friction/YYYY-MM-DD — [Topic] Conflict.md`:

```yaml
---
date: YYYY-MM-DD
type: friction
tags: [contradiction, needs-review]
ai-first: true
related: [["Note A"], ["Note B"]]
---

## [FRICTION] — [Topic] Contradiction

**Detection phase:** Editor Run, YYYY-MM-DD

**Side A:**
- Note: [[Existing Note]]
- Claim: "X is true" (confidence: high, as of YYYY-MM)
- Source: [original source if known]

**Side B:**
- Note: [[New Atom]]
- Claim: "X is false" (confidence: stated, as of YYYY-MM)
- Source: [[Literature Note]] → [raw source]

**Analysis:**
[Editor's neutral analysis — which seems more credible, why both might exist]

**Possible resolutions:**
1. Temporal update (X changed between dates)
2. Contextual difference (true in A, false in B)
3. One source is unreliable
4. Both are right in different senses

**Action:**
- [ ] Read both notes fully
- [ ] Check source dates and credibility
- [ ] Update or archive outdated claim
- [ ] This friction note once resolved
```

**Important:** Editor creates [FRICTION] blocks but NEVER resolves them — that's morning review.

### Step 3: Update Index

**For each new atom:**

Add to `07 - SYSTEM/index.md` under the appropriate section:

```markdown
## 02 — PERMANENT

- `02 - PERMANENT/concepts/[New Concept].md` — [3-5 word description] (YYYY-MM-DD)
- `02 - PERMANENT/people/[Person Name].md` — [role/context] (YYYY-MM-DD)
```

**If a new category emerges:**
- Add a new bullet section
- Keep sections alphabetical within their tier

### Step 4: Update Log

**Append to `log.md`:**

```markdown
## [YYYY-MM-DD 06:XX] Editor Run | Linked N atoms, flagged F conflicts
- New atoms processed: N
- Links added: L (outgoing + incoming)
- [FRICTION] blocks created: F
- Index updated: M new entries
- Orphan check: O notes with 0 incoming links (listed below)
```

### Step 5: Orphan Detection

**Scan `2-atoms/` for notes with 0 incoming links:**

An orphan is a note that:
- Exists for 7+ days
- Has no other notes linking TO it
- Is not a "leaf" note (terminal concept)

**List orphans in a weekly report:**

Create `3-threads/orphans/YYYY-MM — Orphan Report.md`:

```markdown
## Orphan Report — YYYY-MM

**Notes with 0 incoming links (7+ days old):**

1. [[Concept A]] — created YYYY-MM-DD
   - Suggested links: [[Related B]], [[Related C]]
   - Action: [ ] Add to index, [ ] Link from related notes

2. [[Person X]] — created YYYY-MM-DD
   - Suggested links: [[Project Y]], [[Event Z]]
   - Action: [ ] Link from project/event

...

**Editor's note:**
[Why these might be orphans — unclear concept, poor naming, genuinely isolated]
```

---

## Quality Gates

**Before ending Editor Run, verify:**

- [ ] Every new atom has 2+ outgoing wikilinks
- [ ] Every new atom has 1+ incoming backlink
- [ ] [FRICTION] blocks created for all detected contradictions
- [ ] `index.md` updated with new entries
- [ ] `log.md` updated with run summary
- [ ] Orphan list updated (if orphans found)

---

## Morning Handoff

**Append to `briefings/YYYY-MM-DD — Morning Brief.md`:**

```markdown
---
(editor section — appended by Editor Run)
---

## Editor Run Summary — YYYY-MM-DD

**Linking:**
- Processed: N new atoms
- Outgoing links added: O
- Incoming backlinks created: I
- Average links per atom: A (target: 3+)

**Index Updates:**
- New index entries: M
- Sections touched: [list sections]

**[FRICTION] Flags (needs your review):**
1. `3-threads/_friction/YYYY-MM-DD — X Conflict.md` — [one-line: "A says X, B says ¬X"]
2. `3-threads/_friction/YYYY-MM-DD — Y Conflict.md` — [one-line]
...

**Orphan Watch:**
- Current orphans (7+ days, 0 links): O notes
- Full report: `3-threads/orphans/YYYY-MM — Orphan Report.md`

**Action Needed:**
- [ ] Resolve [FRICTION] conflicts (priority: high)
- [ ] Skim 2-3 new atoms to verify linking quality
- [ ] Check orphan report for false positives
```

---

## Linking Heuristics

**How to find related notes:**

1. **Concept similarity:**
   - Search for same keywords in note titles
   - Search for overlapping tags
   - Read "See also" sections of related notes

2. **Temporal proximity:**
   - Notes created within 7 days of each other
   - Same literature note as source
   - Same Refinery Run batch

3. **People connections:**
   - Person worked on project → link `[[Person]]` to `[[Project]]`
   - Person studied concept → link `[[Person]]` to `[[Concept]]`
   - Person knew person → link `[[Person A]]` to `[[Person B]]`

4. **Causal chains:**
   - "X caused Y" → link `[[X]]` to `[[Y]]`
   - "Y resulted from X" → link `[[Y]]` to `[[X]]`
   - "Z prevented W" → link `[[Z]]` to `[[W]]`

**Link text matters:**

Bad: `See [[Concept]].`
Good: `See [[Concept]] for the foundational framework.`

Bad: `Related to [[Project]].`
Good: `This concept was applied in [[Project]] to solve X.`

---

## Edge Cases

**If a concept has no clear relatives:**
- Link to broader category: `[[Political Movements]]` ← `[[Justice Party]]`
- Link to time period: `[[1910s India]]` ← `[[Justice Party]]`
- Link to geography: `[[Madras Presidency]]` ← `[[Justice Party]]`
- Every concept has SOME context — find it

**If two notes are 90% duplicate:**
- Don't create a link — merge them
- Move the weaker note to `3-threads/_merge/YYYY-MM-DD — [Name] duplicate.md`
- Editor notes the merge in log
- **Do NOT delete — let morning review confirm**

**If a [FRICTION] conflict is actually just a nuance:**
- Still create the [FRICTION] block
- Add note: "Likely resolution: contextual difference (A in context X, B in context Y)"
- Morning review can close quickly

**If you find broken wikilinks:**
- Note mentions `[[Note X]]` but X doesn't exist
- Create a stub: `3-threads/_stubs/Note X.md`
- Frontmatter: `type: stub, status: needs-content`
- Body: `# [[Note X]]\n\n> Stub created by Editor Run — content needed`

---

## Failure Modes

**What NOT to do:**

- Don't [[link]] every other word — be selective and meaningful
- Don't create [FRICTION] for minor wording differences — flag real contradictions only
- Don't resolve conflicts yourself — that's morning review
- Don't update old notes with new interpretations — only add backlinks, don't rewrite

**If uncertain:**

- Create the [FRICTION] block anyway
- Add your analysis as "Editor's note"
- Morning review decides

---

## Performance Metrics

**Good Editor Run:**
- 100% of new atoms linked (2+ outgoing, 1+ incoming)
- All [FRICTION] contradictions flagged
- Index fully current
- <5% false positive [FRICTION] flags

**Track over time:**
- Average links per atom (target: 3-5)
- [FRICTION] detection rate (target: 1-3 per week)
- Orphan count trend (should stay flat or decrease)
- Broken link count (should decrease over time)

---

*Editor Run is where notes become a network. Be thorough. Be neutral. Be connective.*