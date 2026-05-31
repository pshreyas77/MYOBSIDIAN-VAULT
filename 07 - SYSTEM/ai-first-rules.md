---
date: 2026-05-28
type: system
tags: [ai-first, writing-rules]
ai-first: true
---

# AI-First Rules

> Every note Claude writes in this vault follows these 7 rules. The vault is designed for **future-Claude** to read and reason over, not for human review.

## Rule 1 — Self-Contained Context
Each note explains itself completely. A note pulled in isolation should make sense without requiring backlinks to be read first.

## Rule 2 — "For Future Claude" Preamble
Every note begins with a 2-3 sentence summary under `## For future Claude` immediately after frontmatter:
```markdown
## For future Claude
This note is a [type] about [topic] saved on [date]. It [main purpose].
```

## Rule 3 — Rich, Consistent Frontmatter
```yaml
---
date: YYYY-MM-DD
type: <literature|permanent|project|daily|map|output|system>
tags: [...]
ai-first: true
source: [URL or link]
---
```

## Rule 4 — Recency Markers Per Claim
```markdown
[Claim] (as of YYYY-MM, [source])
```
Example: "Mem0 raised $24M Series A (as of 2026-04, mem0.ai/blog/series-a)"

## Rule 5 — Sources Preserved Verbatim
Every external claim includes its source URL inline in the body text, not just in frontmatter.

## Rule 6 — Cross-Links Are Mandatory
Every person, project, concept, or decision uses `[[wikilinks]]`. Never write a name without linking it.

## Rule 7 — Confidence Levels
Use inline confidence markers on claims:
- `stated` — directly from a cited source
- `high` — well-established fact
- `medium` — likely true, verify when possible
- `speculation` — interpretation, may not hold

---

## Frontmatter Schemas by Note Type

### Literature Note
```yaml
date: YYYY-MM-DD
type: literature
source: [TITLE]
author: [AUTHOR]
date_read: YYYY-MM-DD
status: to-process | processed
tags: [book|article|paper|video]
ai-first: true
```

### Permanent Note
```yaml
date: YYYY-MM-DD
type: permanent
tags: [concept|idea]
created: YYYY-MM-DD
ai-first: true
```

### Project Note
```yaml
date: YYYY-MM-DD
updated: YYYY-MM-DD
type: project
status: active | planning | completed | archived | on-hold
tags: [project, ...]
related-people: [["People/..."]]
related-projects: [["Projects/..."]]
ai-first: true
```

### Daily Note
```yaml
date: YYYY-MM-DD
type: daily
tags: [daily]
mood: ""  # optional
energy: ""  # optional
ai-first: true
```

### Map of Content
```yaml
date: YYYY-MM-DD
type: map
topic: [topic name]
tags: [map, ...]
related_notes: [["02 - PERMANENT/concepts/..."]]
ai-first: true
```

### Output Note
```yaml
date: YYYY-MM-DD
type: output
subtype: essay | analysis | framework
tags: [topic, ...]
ai-first: true
```

### Task Card (on kanban boards)
```markdown
- [ ] 🔴 **Task title** · @{YYYY-MM-DD}
    Description [[Links]]
```

## Migration Note
AI-first rules established 2026-05-28 as part of Karpathy second brain framework migration. Notes written before this date may not yet conform — run `/obsidian-health` to identify them.