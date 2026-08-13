---
date: 2026-08-13
type: source-article
source: https://youtu.be/wvYAuHfJRo0
tags: [second-brain, obsidian, hermes, capture-mode, raw-digest]
status: unprocessed
captured_by: shrey
---

# Give Hermes A Second Brain With Obsidian

> **Raw capture — DO NOT EDIT.**
> Source: YouTube tutorial transcript / companion article (`https://youtu.be/wvYAuHfJRo0`). Captured for processing by the nightly digest.

## Premise

A second brain is **not** a bigger memory file. It's a different structure:

- **Raw folder** — untouched source material (transcripts, notes, messages, exports).
- **Wiki** — compiled knowledge distilled from Raw.
- Both searchable. Wiki is disposable; Raw is the asset. Break/rebuild the wiki freely without losing source.

## Build Steps (described in article)

### 1. Scaffold the vault

Prompt:
```
Set up my second brain at /path/to/your/vault.

Create this structure:
- A Raw folder (untouched source material)
- A Wiki folder (compiled knowledge)
- identity.md, projects.md and tasks.md at the vault root

Then write an AGENTS.md file at the vault root explaining the ownership rule:
I am the only one who writes to the Raw folder and identity.md.
The nightly compile job is the only thing that writes to the Wiki.
```

### 2. Fill identity files via interview

Prompt:
```
Interview me to populate my second brain. Ask me questions about my business,
my current projects, my open tasks, how I work and what I am trying to build.
Then write my answers into identity.md, projects.md and tasks.md in the vault.
```

### 3. Context Rules (read-first)

Create `context-rules.md` referenced from `AGENTS.md`. Five rules:

1. Read `identity.md` and `projects.md` before answering anything about my work.
2. Pull only the notes that match the question, and follow their links one hop out.
3. Name every note you used by name.
4. If the vault has the answer, never answer from training data.
5. If the vault does not have it, say so plainly.

### 4. Routing Table

In `AGENTS.md`:
```
Add a routing table to AGENTS.md. For each kind of work I do, list which
files and folders to read, what to skip, and which skill to use.
```

Keeps token spend down as vault grows; nothing searches everything.

### 5. Capture mode + Nightly compile

Capture mode:
```
Turn on capture mode. Every voice note, message or transcript I send you
goes straight into the Raw folder of my vault. Do not title it, tag it
or file it. Just save it.
```

Manual compile:
```
Read everything in the Raw folder. File each item where it belongs in the
Wiki, update identity.md, projects.md and tasks.md where relevant, and link
related pages together. Keep the source notes on every wiki page pointing
back to the raw file it came from.
```

### 6. Skill + Cron

```
Turn what you just did, processing the Raw folder into wiki pages, updated
files and linked notes, into a skill called raw-digest, so I can run it
whenever I want.
```

Schedule:
```
Every night at 3am, run the raw-digest skill against my vault's Raw folder.
Then at 7am, write me a short brief of what changed: what was captured,
what was filed, and what the wiki now covers that it did not before.
```

### 7. Department folders (optional, later)

Inside the Wiki: folder per department (finance, marketing, operations, clients, offers), each with its own `AGENTS.md`. Re-run digest to re-categorize.

## Key insights

- Raw vs wiki split = safe experimentation (break wiki, rebuild, Raw never changes).
- Capture mode has zero filing overhead during the day.
- Nightly compile does the heavy lifting while you sleep.
- Rule 4 + Rule 5 are the difference between an agent that checks records and one that improvises with confidence.

## Next ideas (article sketches, not implemented)

- Trigger skill when specific folder updates.
- Call transcripts feeding a queryable wiki for "most common objections last 30 days."

## Source

- YouTube: https://youtu.be/wvYAuHfJRo0
- Companion article (this text)
- Video transcript could be added as a sibling raw file for richer processing.
