---
date: 2026-07-09
type: literature
source: Karpathy LLM Wiki Pattern — Full Synthesis
author: Andrej Karpathy (original) + synthesis expansion
tags: [article, llm-wiki, second-brain, knowledge-compounding, maintenance, karpathy]
ai-first: true
---

# LLM Wiki Pattern — Full Synthesis: Your Second Brain Is Useless Until AI Maintains It

## For future Claude
This is a full synthesis of Karpathy's LLM wiki pattern — the three-layer architecture (raw sources → compiled wiki → schema), the shift from retrieval to compounding, the health check as product, and why markdown matters. Created 2026-07-09. This is the most complete articulation of the pattern your vault follows.

---

## Core Argument

Most AI document workflows are **retrieval-based**: upload → chunk → embed → search → answer → close tab. Tomorrow, start from zero again. You are not building knowledge. You are renting short bursts of intelligence.

The LLM wiki pattern changes this: knowledge becomes **cumulative**. Every source makes the wiki better. Every question creates an artifact. Every artifact becomes future context. Over time, the system develops a shape that reflects what you actually study, write, build, and decide.

> **"The value is not just faster summaries, cleaner notes, or prettier graphs. The value is accumulated context."**

---

## Why Second Brains Fail Without AI

The old model of PKM quietly assumed the human would do everything:
- Read the source, highlight, summarize
- Choose folders, add tags, create links
- Remember that an older note now needs updating
- Notice that two sources disagree
- Keep indexes clean
- Decide whether orphan notes should be deleted, merged, or connected

This feels productive in week one and unbearable in month three.

> **"The second brain fails because it still needs a first brain to clean up after it."**

LLMs flip this. They don't get tired of repetitive structure. They don't mind updating fifteen files in one pass. They can scan for stale claims, missing backlinks, duplicated concepts, inconsistent naming, and unresolved contradictions. The human stays closer to **judgment** — choosing inputs, asking sharper questions, challenging weak synthesis, deciding what matters. The LLM does the **clerical work of knowledge**.

---

## The Three Layers

### Layer 1: Raw Sources (Immutable)
Original materials: articles, PDFs, notes, transcripts, papers, web clips, images, repos, datasets. The AI can read, cite, and summarize, but should NOT rewrite the evidence. This is the evidence layer.

### Layer 2: Wiki (Compiled)
Directory of markdown files maintained by the LLM: source summaries, concept pages, entity pages, timelines, comparisons, open questions, indexes, research briefs. This is where raw material becomes usable knowledge.

### Layer 3: Schema (Rules)
Instructions that tell the LLM how to behave as a maintainer:
- What folders exist?
- What counts as a source summary?
- How should citations work?
- When should it create a new concept page vs updating an old one?
- How should contradictions be recorded?
- What does a health check look for?

> **"The schema is what turns a chatbot into an operator."**

---

## From Retrieval to Compounding

| Retrieval (RAG) | LLM Wiki |
|:---|:---|
| Waits until query time to synthesize | Compiles knowledge ahead of time |
| Work disappears when conversation ends | Synthesis becomes durable structure |
| Next question starts another cycle | Next question starts from accumulated context |
| Good for one-off questions | Good for learning, research, writing, strategy |

The question changes from *"Can I retrieve the right paragraph?"* to *"Has my knowledge base become smarter because I added this source?"*

---

## The Health Check Is the Product

A normal note system decays silently:
- Links break
- Pages duplicate
- Summaries get stale
- Claims contradict each other
- Important sources remain unprocessed

An LLM-maintained wiki can be **checked**:
- Find orphan pages
- Identify duplicated concepts
- Flag claims that need citations
- Surface where newer sources conflict with older ones
- Assess what pages are too vague, too long, too thin, or missing cross-references

> **"The health check is not a side feature. It is the mechanism that keeps trust alive."**

---

## Why Markdown Matters

Markdown files are:
- Portable (live in a normal folder)
- Openable in Obsidian, any text editor
- Versionable with git
- Searchable with command-line tools
- Renderable into websites, slides
- Processable by scripts

> **"A local markdown wiki is boring in the best possible way. It is inspectable. It is durable. It can be backed up. It can be diffed."**

For serious knowledge work, boring infrastructure wins.

---

## The Real Workflow

1. **Collect** raw sources
2. **Let LLM compile** them into structured markdown wiki
3. **Browse** result in Obsidian
4. **Ask questions** against the wiki
5. **Save substantial answers** back into the wiki
6. **Run periodic health checks**
7. **Repeat**

> **"The flywheel is what matters."**

---

## The Human Role vs AI Role

| Human (Judgment) | AI (Maintenance) |
|:---|:---|
| Choose which sources belong | Summarize, link, revise, cite |
| Decide which claims are important | Update fifteen files in one pass |
| Ask sharper questions | Scan for stale claims, orphans, duplicates |
| Challenge weak synthesis | Flag contradictions, missing backlinks |
| Decide what matters | Lint, maintain, keep indexes current |

> **"The human should do the editorial work of meaning. The LLM should do the clerical work of knowledge."**

---

## Obsidian as the IDE

Karpathy's metaphor: Obsidian is the IDE, the LLM is the programmer, and the wiki is the codebase. Codebases are valuable because files follow conventions, reference each other, can be refactored, can be linted, and can be improved without starting over. A serious knowledge base should work the same way.

---

## The Takeaway

The old second brain was a storage system with a discipline problem. The LLM wiki flips the model:

- Raw sources = evidence layer
- Markdown wiki = compiled layer
- Schema = rules for maintenance
- Health checks = trust mechanism
- Obsidian = inspection/query/reuse interface

RAG can help you answer a question from a pile of documents. An LLM-maintained wiki changes the **starting point for every future question**.

> **"Your second brain does not need more folders. It needs someone to maintain it. And for the first time, that someone does not have to be you."**

---

## Related
- [[01 - LITERATURE/2026-07-08 — LLM Wiki Pattern — Karpathy]] — original Karpathy post analysis
- [[02 - PERMANENT/concepts/Contrarian Loop — Vault That Argues With Itself]] — CONTRA layer for contradiction detection
- [[05 - MAPS/Digital Garden MOC]] — PKM methodology
- [[05 - MAPS/Agentic Systems MOC]] — automation patterns
- [[03 - PROJECTS/InfiniteBrain]] — this vault as PKM system