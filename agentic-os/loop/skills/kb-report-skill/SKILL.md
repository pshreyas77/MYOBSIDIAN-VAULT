---
name: kb-report-skill
description: Generate research reports from wiki — answers questions using vault knowledge
when: user asks a research question; triage flags "report" actionable
never:
  - answer without citing wiki sources in the report
  - hallucinate facts not present in wiki pages
  - write reports longer than 3000 words without executive summary
done_when:
  - "report saved to 06 - OUTPUTS/reports/YYYY-MM-DD-topic-slug.md"
  - "all claims cite specific wiki pages or raw sources"
  - "report linked from at least 2 cited wiki pages (Reports section)"
---

## Steps

1. Parse the question — extract keywords and topic domains
2. Search `wiki/concepts/` and `wiki/entities/` for relevant pages (match on title, tags, content)
3. Read all matching pages into context (up to 30 pages, prioritize by relevance + recency)
4. Synthesize answer using ONLY the wiki content — no general LLM knowledge
5. Write report to `06 - OUTPUTS/reports/YYYY-MM-DD-topic-slug.md`

## Report Template

```markdown
---
question: "The research question"
date: "YYYY-MM-DD"
sources_used:
  - wiki/concepts/Concept-1.md
  - wiki/entities/Entity-1.md
tags: ["tag1", "tag2"]
confidence: 0.85
---

# Report: Research Question

**Question:** The original question.

**Executive Summary:** 2-3 paragraph answer.

## Detailed Analysis

### Section 1: Key Concept
Content citing [[Concept-1]] and [[Entity-1]].

### Section 2: Another Angle
Content citing [[Concept-2]].

## Synthesis
Cross-cutting insights.

## Sources Cited

| Source | Type | Key Contribution |
|--------|------|------------------|
| [[Concept-1]] | concept | Definition |
| [[Entity-1]] | entity | Case study |

## Gaps & Open Questions
- Question 1
- Question 2
```

## Link-Back

After writing the report, append to each cited wiki page:

```markdown
## Reports
- [[06 - OUTPUTS/reports/YYYY-MM-DD-topic-slug|Report: Research Question]] (YYYY-MM-DD)
```