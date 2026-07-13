---
name: kb-healthcheck-skill
description: Weekly knowledge integrity audit — finds conflicts, gaps, duplicates
when: weekly cron triggers; triage flags "healthcheck" actionable
never:
  - auto-fix conflicts without flagging for human review
  - merge pages without preserving all source links from both
  - delete any file — only merge, redirect, or create stubs
done_when:
  - "health report saved to 06 - OUTPUTS/healthchecks/healthcheck-YYYY-MM-DD.md"
  - "all conflicts flagged with specific page and line references"
  - "missing page suggestions include mention counts and referencing pages"
---

## Steps

1. Scan all wiki/concepts/ and wiki/entities/ pages
2. For each check category, produce findings:

### Conflicts
- Look for contradictory claims across pages about the same subject
- Flag numerical inconsistencies (different dates, stats for same thing)
- Report with both page references and confidence scores

### Missing Pages
- Extract all `[[wikilinks]]` from all wiki pages
- Count how many times each concept/entity is mentioned
- Flag entities mentioned ≥3 times without their own page

### Near-Duplicates
- Compare concept page content pairwise
- Flag pairs with high similarity (shared phrases, same structure)
- Suggest merge into canonical page

### Unsourced Claims
- Flag pages missing `sources` in frontmatter
- Flag claims with `confidence` < 0.6 in frontmatter
- Flag pages with no wikilinks (isolated)

### Stale Content
- Compare `last_compiled` date vs newest source file date in `0-raw/`
- Flag pages >90 days old with newer source material available

### New Candidates
- Detect co-mentioned concept pairs that lack direct wikilinks
- Detect entities appearing in ≥3 recent `0-raw/` files but not in wiki/

3. Write report to `06 - OUTPUTS/healthchecks/healthcheck-YYYY-MM-DD.md`

## Auto-Fix (safe operations only)

- Merge confirmed duplicates (preserve all source links from both pages)
- Create stub pages for entities mentioned ≥5 times
- Update `wiki/index.md` if new patterns emerge

## Report Template

```markdown
---
healthcheck_date: "YYYY-MM-DD"
wiki_stats:
  concepts: N
  entities: N
  raw_sources: N
issues:
  conflicts: N
  missing_pages: N
  duplicates: N
  unsourced: N
  stale: N
health_score: N/100
---

# Knowledge Base Health Check — YYYY-MM-DD

**Health Score: N/100**

## Conflicts
...

## Missing Pages
...

## Near-Duplicates
...

## Unsourced / Low-Confidence
...

## Stale Content
...

## New Article Candidates
...
```