---
date: 2026-08-13
type: wiki-reference
tags: [second-brain, workflow, context-rules, capture-mode]
related: ["0-raw/2026-08-13_give-hermes-a-second-brain-with-obsidian_article.md"]
---

# Second Brain — Hermes × Obsidian Reference

> **Compiled wiki page.** Source: `0-raw/2026-08-13_give-hermes-a-second-brain-with-obsidian_article.md`
> (YouTube tutorial + companion article, `https://youtu.be/wvYAuHfJRo0`).

## Core Principle

A second brain is **not** a bigger memory file. It's a two-layer structure:

| Layer | Content | Mutable? |
|-------|---------|----------|
| **Raw** (`0-raw/`) | Untouched source material (transcripts, notes, messages, exports) | Never edited |
| **Wiki** (compiled) | Distilled knowledge, linked pages | Disposable/rebuildable |

Because the wiki is compiled from Raw, you can delete and regenerate the whole wiki anytime. **Raw is the asset; the wiki is disposable.** This makes experimentation safe — break the wiki, rebuild it, restructure it; the source never moves.

## How This Maps To Your Vault

| Article concept | Equivalent in your vault |
|-----------------|--------------------------|
| Raw folder | `0-raw/` (with `0-Inbox/` as the capture inbox) |
| Wiki folder | `02 - AREAS/`, `wiki/`, `05 - MAPS/`, `00 - SYSTEM/MOCs/` |
| identity.md | `ME.MD`, `00 - SYSTEM/01_KNOWLEDGE_HUB.md` |
| projects.md | `01 - PROJECTS/`, `03 - PROJECTS/` |
| tasks.md | `03 - PROJECTS/*/`, `04 - DAILY/` |
| AGENTS.md | `AGENTS.md` (exists, "Jarvis OS") |

## Capture Mode

Fire anything at Hermes all day with zero filing — voice notes, messages, transcripts, exports all go straight into the Raw folder, timestamped, untitled, untagged:

```
Turn on capture mode. Every voice note, message or transcript I send you
goes straight into the Raw folder of my vault. Do not title it, tag it
or file it. Just save it.
```

## Nightly Compile (raw-digest)

Distilled into a reusable skill + cron schedule. Optimized timing for your vault:

| Stage | Time | Action |
|-------|------|--------|
| Digest | 03:00 | `raw-digest` skill: file Raw→wiki, update identity/projects/tasks, link pages, keep source refs |
| Brief | 07:00 | Short brief: what was captured, what was filed, what's new coverage |

Manual compile equivalent:
```
Read everything in the Raw folder. File each item where it belongs in the Wiki,
update identity.md, projects.md and tasks.md where relevant, and link related
pages together. Keep the source notes on every wiki page pointing back to the
raw file it came from.
```

## Context Rules (read-first, in AGENTS.md)

1. Read `identity.md` and `projects.md` before answering anything about my work.
2. Pull only the notes that match the question, and follow their links one hop out.
3. Name every note you used by name.
4. If the vault has the answer, never answer from training data.
5. If the vault does not have it, say so plainly.

→ Rules 4 & 5 are the difference between an agent that **checks its records** and one that **improvises with confidence**.

## Routing Table

Keep token spend down as the vault grows: each task type reads only its own corner of the vault.

| Work type | Read | Skip | Skill |
|-----------|------|------|-------|
| Research / content | `02 - AREAS/`, `wiki/`, `05 - MAPS/` | `04 - DAILY/` | `raw-digest`, `graphify` |
| Code / dev | `03 - PROJECTS/`, `01 - PROJECTS/` | philosophy | terminal/MCP |
| Health / fitness | `02 - AREAS/06`, `wiki/entities` | — | — |
| Philosophy / religion | `02 - AREAS/01`, `00 - SYSTEM/MOCs/` | code | — |

## Department Folders (next step, optional)

Inside the compiled Wiki, create a folder per business area (finance, marketing, operations, clients, offers), each with its own `AGENTS.md`. Re-run `raw-digest` to re-categorize existing pages into the new departments.

---

*Created 2026-08-13 from `0-raw/2026-08-13_give-hermes-a-second-brain-with-obsidian_article.md`.*