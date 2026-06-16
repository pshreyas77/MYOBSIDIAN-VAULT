---
date: 2026-06-16
type: playbook
tags: [audit-run, weekly, autonomous-agents]
ai-first: true
schedule: "0 22 * * 0" # Sunday 10 PM weekly
---

# Audit Run — Weekly Health Check Playbook

> **Mission:** Sweep the vault for rot, stale claims, broken links, and quality drift. You are the inspector — making sure the Night Shift agents held the line.

---

## Operating Parameters

**Time:** 10:00 PM Sundays (after Editor completes)
**Input:** Entire vault (`2-atoms/`, `wiki/`, `02 - PERMANENT/`, `01 - LITERATURE/`)
**Output:** Health report, stale claim flags, broken link list, orphan report, weekly synthesis

**Read first:**
1. `house-rules.md` — Quality Gates & enforcement
2. `07 - SYSTEM/ai-first-rules.md` — Frontmatter & preamble standards
3. `07 - SYSTEM/index.md` — Current vault structure

---

## The Audit Pipeline

### Step 1: Vault Health Scan

**Scan for structural issues:**

1. **Duplicate Detection:**
   - Search for notes with >80% similar titles
   - Search for notes with overlapping content (same concept, different files)
   - Flag: `3-threads/_duplicates/YYYY-MM-DD — [Topic] Duplicates.md`

2. **Orphan Detection:**
   - Find notes with 0 incoming wikilinks (7+ days old)
   - Exclude: leaf notes (terminal concepts), daily notes, literature notes <30 days
   - Report: `3-threads/orphans/YYYY-MM — Orphan Report.md`

3. **Broken Link Sweep:**
   - Find `[[Note Name]]` where target doesn't exist
   - Find `[[Note Name#Anchor]]` where anchor doesn't exist
   - Report: `3-threads/_broken-links/YYYY-MM-DD — Broken Links.md`

4. **Missing Frontmatter:**
   - Scan all notes in `2-atoms/`, `02 - PERMANENT/`, `wiki/`
   - Flag notes without: `date`, `type`, `tags`, `ai-first: true`
   - Report: `3-threads/_frontmatter/YYYY-MM-DD — Missing Frontmatter.md`

**Health Report Template:**

```markdown
---
date: YYYY-MM-DD
type: audit-report
tags: [weekly-audit, health-check]
ai-first: true
audit-week: YYYY-WNN
---

## Vault Health Audit — Week YYYY-WNN

**Scan Date:** YYYY-MM-DD 22:XX
**Scope:** Entire vault (N files scanned)

### Overall Score: XX/100

**Breakdown:**
- Duplicate rate: X% (target: <2%)
- Orphan rate: X% (target: <5%)
- Broken links: N (target: 0)
- Missing frontmatter: N (target: 0)
- Stale claims: N (target: <10)

### Issues by Priority

**🔴 Critical (fix this week):**
1. [Issue + location + why critical]
2. ...

**🟡 Warning (fix within 2 weeks):**
1. [Issue + location + why it matters]
2. ...

**🟢 Info (track, no action needed):**
1. [Issue + context]
2. ...

### Trend Tracking

| Metric | This Week | Last Week | Δ |
|--------|-----------|-----------|---|
| Total notes | N | N | +N |
| Orphans | N | N | +N |
| Broken links | N | N | +N |
| Stale claims | N | N | +N |

**Trend:** 📈 improving | 📉 degrading | ➡️ stable
```

### Step 2: Stale Claim Detection

**Scan for aging claims without recency markers:**

1. **Search patterns for time-sensitive claims:**
   ```
   - "is the" / "is currently" / "as of" (without date)
   - Role claims: "is CEO", "works at", "founder of"
   - Status claims: "is developing", "is building", "currently"
   - Numbers: "raised $X", "has N users", "valued at $X"
   ```

2. **For each claim >6 months old without recency marker:**
   - Create a flag in `3-threads/_stale/YYYY-MM-DD — Stale Claims.md`
   - Include: note link, claim text, age in days, verification needed

**Stale Claim Format:**

```markdown
## Stale Claims — YYYY-MM-DD

**Claims older than 6 months without "(as of YYYY-MM, source)" markers:**

1. **[[Note Name]]** — [Claim text]
   - Age: N days (last updated: YYYY-MM-DD)
   - Type: role | status | number | relationship
   - Verification: [what to check: LinkedIn, company site, news]
   - Action: [ ] Verify and update, [ ] Delete if wrong

2. **[[Note Name]]** — [Claim text]
   ...

**Priority by claim type:**
- Role claims (CEO, founder, employee) → HIGH (people move fast)
- funding numbers → HIGH (rounds close, valuations change)
- Product status → MEDIUM (launches, pivots)
- General facts → LOW (less time-sensitive)
```

### Step 3: Quality Sampling

**Spot-check 10-15 random atoms for drift:**

1. **Random sample from:**
   - `2-atoms/` (last 7 days)
   - `02 - PERMANENT/concepts/`
   - `wiki/concepts/`

2. **Check each for Prime Directive compliance:**
   - [ ] Has source citation (inline, verbatim)
   - [ ] Has "For future Claude" preamble
   - [ ] Has 2+ outgoing wikilinks
   - [ ] Has confidence marker (`stated | high | medium | speculation`)
   - [ ] No interpretation drift (claims match source)

3. **If drift detected:**
   - Flag note in `3-threads/_drift/YYYY-MM-DD — Drift Detected.md`
   - Include: link, what's wrong, suggested fix
   - Do NOT fix — morning review handles

**Quality Score Calculation:**

```
Quality Score = (Pass / Total Sampled) × 100

Target: 95%+ pass rate
Warning: 80-95%
Critical: <80%
```

### Step 4: Broken Wikilink Cleanup

**For each broken `[[Link]]` found:**

1. **Check if it's a typo:**
   - Search vault for similar titles
   - If 90%+ match: suggest correction

2. **If target note is missing:**
   - Create stub in `3-threads/_stubs/[Link Name].md`
   - Frontmatter: `type: stub, status: needs-content`
   - Body: `# [[Link Name]]\n\n> Stub created by Audit Run — content needed`

3. **Update the referencing note:**
   - Add comment: `<!-- Broken link: [[Link Name]] → stub created -->`
   - Do NOT delete the link — let morning review decide

### Step 5: Weekly Synthesis

**Look for patterns that emerged this week:**

1. **Concept co-occurrence:**
   - Same concepts appearing in 3+ unrelated notes
   - New connections between previously separate clusters

2. **If synthesis opportunity found:**
   - Create `05 - MAPS/YYYY-MM-DD — [Topic] Synthesis.md`
   - Or update existing MOC if topic already has one

**Synthesis Note Template:**

```yaml
---
date: YYYY-MM-DD
type: synthesis
tags: [synthesis, weekly-emergence]
ai-first: true
related: [["Note A"]], [["Note B"]], [["Note C"]]
---

## [Topic] Synthesis — Week YYYY-WNN

**Trigger:** Audit Run detected N notes this week sharing [concept]

**Emergent Pattern:**
[2-3 paragraphs: what's connecting that wasn't before]

**Key Insights:**
1. [Insight 1 with links to source notes]
2. [Insight 2 with links to source notes]
3. [Insight 3 with links to source notes]

**Open Questions:**
- [What's still unclear]
- [What needs more research]

**Related MOCs:**
- [[Related Map of Content]]
- [[Another Related MOC]]
```

### Step 6: Update Performance Dashboard

**Append weekly metrics to `07 - SYSTEM/audit-dashboard.md`:**

```markdown
## Week YYYY-WNN

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Vault size | N notes | — | 📊 |
| New atoms | N | 20-50/week | ✅ |
| Orphans | N (X%) | <5% | ✅ |
| Broken links | N | 0 | ⚠️ |
| Stale claims | N | <10 | ✅ |
| Quality score | XX% | 95%+ | ✅ |
| [FRICTION] resolved | N/N | 100% | ✅ |

**Trend:** 📈 improving | 📉 degrading | ➡️ stable
```

### Step 7: Log & Report

**Append to `log.md`:**

```markdown
## [YYYY-MM-DD 22:XX] Audit Run | Week YYYY-WNN | Score: XX/100
- Scanned: N files
- Duplicates found: D
- Orphans detected: O (O weeks old)
- Broken links: B
- Stale claims: S
- Quality score: Q% (sampled N atoms)
- Synthesis created: S maps
```

**Append to briefings/YYYY-MM-DD — Morning Brief.md:**

```markdown
---
(audit section — appended by Audit Run)
---

## Audit Run Summary — Week YYYY-WNN

**Health Score:** XX/100

**🔴 Critical Issues (needs your review):**
1. [Issue 1 + location]
2. [Issue 2 + location]

**🟡 Warnings:**
1. [Warning 1]
2. [Warning 2]

**Full Report:** `3-threads/_audit/YYYY-MM-DD — Vault Health.md`

**Action Needed:**
- [ ] Review critical issues
- [ ] Update stale claims (priority: role/numbers)
- [ ] Approve stub creations for broken links
- [ ] Skim weekly synthesis if created
```

---

## Quality Gates

**Before ending Audit Run, verify:**

- [ ] Health report created with overall score
- [ ] All broken links documented
- [ ] Stale claims flagged (6+ months)
- [ ] Quality sample spot-checked (10-15 atoms)
- [ ] Orphan report updated
- [ ] Audit dashboard updated
- [ ] Morning brief appended

---

## Edge Cases

**If a note is 90% duplicate:**
- Don't flag as "orphan" — flag as "merge candidate"
- Create `3-threads/_merge/YYYY-MM-DD — [Topic] Duplicates.md`
- Include both notes, suggest merge target

**If an orphan is intentional (standalone concept):**
- Add `tags: [leaf-note]` to exempt from future orphan scans
- Add to orphan report with note: "Intentional standalone"

**If >20% of sample has drift:**
- Escalate to critical
- Recommend retraining Scout/Refinery/Editor
- Suggest vault-wide grep for specific drift patterns

**If a [FRICTION] block is >30 days old:**
- Flag in morning brief as "stale friction"
- Priority: resolve before it fossilizes

---

## Failure Modes

**What NOT to do:**

- Don't fix issues yourself — flag them for morning review
- Don't delete orphaned notes — they may be valid
- Don't "correct" typos in note titles — flag, don't rewrite
- Don't update stale claims — verify first, then flag

**If uncertain:**

- Flag it anyway
- Add "Audit's note:" with your analysis
- Let morning review decide

---

## Performance Metrics

**Good Audit Run:**

- 100% of vault scanned
- All critical issues flagged
- <5% false positive rate on flags
- Clear action items for morning review
- Dashboard updated with trends

**Track over time:**

| Metric | Target | Why |
|--------|--------|-----|
| Vault growth | 20-50 atoms/week | Healthy intake |
| Orphan rate | <5% | Good linking |
| Broken links | 0 × | Quality gate holding |
| Stale claims | <10 | Recency discipline |
| Quality score | 95%+ | Prime Directive adherence |
| [FRICTION] resolution | 100% weekly | Morning review on duty |

---

## Sunday Night Handoff

```markdown
## 📊 Weekly Audit Complete — YYYY-MM-DD

**Health Score:** XX/100

**Vault Size:** N notes (+N this week)

**Top Issues:**
1. 🟢 [Most important fix]
2. 🟡 [Second priority]
3. 🟡 [Third priority]

**Quality Trend:** 📈 Improving (+X% from last week)

**Morning Priority:**
- [ ] Review [critical issue]
- [ ] Update [stale claim count] claims
- [ ] Approve [N] stubs for broken links

*The vault is clean. The graph is sound. Sleep well.*
```

---

*Audit Run is where the vault inspects itself. Be thorough. Be unsparing. Be constructive.*