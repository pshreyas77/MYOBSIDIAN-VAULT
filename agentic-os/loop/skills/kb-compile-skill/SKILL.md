---
name: kb-compile-skill
description: Compile raw sources into wiki pages — Agentic OS skill for the loop executor
when: new files in 0-raw/; triage flags "compile" actionable
never:
  - overwrite human-written wiki pages without explicit consent
  - compile without source attribution in frontmatter
  - create pages with confidence >0.8 without citing at least 2 sources
done_when:
  - "every new file in 0-raw/ since last compile has a corresponding wiki page"
  - "wiki/index.md updated with new entries"
  - "wiki/log.md has compilation entry for this run"
---

## Steps

1. Scan `0-raw/` for files modified since last compile (check `wiki/log.md` for last timestamp)
2. For each new raw file:
   - Extract concepts → create/update `wiki/concepts/Concept-Name.md` using the concept page template
   - Extract entities → create/update `wiki/entities/Entity-Name.md` using the entity page template
   - Link concepts to entities and vice versa with `[[wikilinks]]`
3. Update `wiki/index.md` — add new entries under appropriate topic sections
4. Append to `wiki/log.md`:
   ```
   ## YYYY-MM-DD Compilation
   - Processed: 0-raw/file1.md, 0-raw/file2.md
   - Created: wiki/concepts/New-Concept.md, wiki/entities/New-Entity.md
   - Updated: wiki/concepts/Existing-Concept.md
   ```

## Concept Page Template

```markdown
---
concept: "Concept Name"
sources: ["0-raw/source-file.md"]
related: ["Related-Concept"]
tags: ["tag1"]
last_compiled: "YYYY-MM-DD"
confidence: 0.8
---

# Concept Name

**Definition:** 2-3 sentence definition.

**Key Insights:**
- Insight 1
- Insight 2

**Sources:** [[0-raw/source-file.md|Source Title]]

**Related:** [[Related-Concept]], [[Related-Entity]]
```

## Entity Page Template

```markdown
---
entity: "Entity Name"
type: "person | organization | event | work | concept"
sources: ["0-raw/source-file.md"]
related: ["Related-Entity"]
tags: ["tag1"]
last_compiled: "YYYY-MM-DD"
---

# Entity Name

**Type:** Person / Organization / Event / Work / Concept

**Summary:** Brief description.

**Key Details:**
- Detail 1
- Detail 2

**Sources:** [[0-raw/source-file.md|Source Title]]

**Related:** [[Related-Concept]], [[Related-Entity]]
```

## Rules (enforced by verify.sh)

- Never compile without source attribution in frontmatter `sources` field
- Never create pages with confidence >0.8 unless citing ≥2 sources
- Never overwrite a page that has `author: human` in its frontmatter
- All wikilinks must resolve to existing files or new files created in this run