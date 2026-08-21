---
date: 2026-08-13
type: literature
subtype: article
source: https://youtu.be/wvYAuHfJRo0
author: unknown
status: to-process
ai-first: true
tags: [literature, article, second-brain, obsidian, hermes, capture-mode, raw-digest]
---

## For future Claude
This is an article (YouTube companion text) about building a second-brain vault for Hermes Agent using Obsidian. It describes a Raw/Wiki split with a nightly compile job. Captured 2026-08-13 from `https://youtu.be/wvYAuHfJRo0`.

## Source
- Video: https://youtu.be/wvYAuHfJRo0
- Companion article (raw capture): `0-raw/2026-08-13_give-hermes-a-second-brain-with-obsidian_article.md`

## Summary
The article argues that a second brain is "not a bigger memory file" but a different structure: a **Raw folder** of untouched source material and a **Wiki** of compiled knowledge that is disposable and rebuildable. The build steps (as stated in source) are: (1) scaffold the vault with Raw + Wiki + `identity.md`, `projects.md`, `tasks.md` and an `AGENTS.md` ownership rule; (2) fill identity files via an interview prompt; (3) write five read-first context rules — including "name every note you used" and "if the vault has the answer, never answer from training data"; (4) add a routing table to `AGENTS.md` to keep token spend down; (5) enable a "capture mode" that drops voice notes/messages/transcripts into Raw with zero filing overhead, paired with a manual "nightly compile" prompt; (6) turn the compile workflow into a skill called `raw-digest`, scheduled at 3am nightly with a 7am brief of what changed; (7) optional department folders inside the Wiki with their own `AGENTS.md`. Key insight (verbatim from source): "Rule 4 + Rule 5 are the difference between an agent that checks records and one that improvises with confidence."

## Key Claims
- A second brain is a structure (Raw + Wiki), not a larger memory file (as of 2026-08, stated in source).
- Capture mode should have zero filing overhead during the day; nightly compile does the heavy lifting (as of 2026-08, stated in source).
- Context Rule 4: "If the vault has the answer, never answer from training data" — paired with Rule 5: "If the vault does not have it, say so plainly" (as of 2026-08, stated in source).
- The compile workflow should be turned into a reusable skill (`raw-digest`) and scheduled (3am compile + 7am brief) (as of 2026-08, stated in source).
- Wiki is disposable; Raw is the asset. Break/rebuild the wiki freely without losing source (as of 2026-08, stated in source).

## For Refinery
- Candidate atoms (extract only what the source says):
  - **Raw vs Wiki split** — safe experimentation principle (wiki rebuildable, raw immutable)
  - **Capture mode with zero filing overhead** — daytime discipline
  - **Nightly compile job** — 3am cron of the raw-digest skill
  - **Five context rules** — esp. "name every note you used" + "vault-first, never training data" + "say so plainly if missing"
  - **Routing table in AGENTS.md** — per-task file/folder/skill mapping to control token spend
  - **Department folders with their own AGENTS.md** — optional scaling pattern
- Skip: the specific scaffold path (`/path/to/your/vault`) — example only.
- Skip: department-folder idea sketches (listed as "not implemented").
- Source itself does NOT cite empirical studies; claims are prescriptive (how-to), not empirical. Mark all atoms `stated` confidence.
- Possible [FRICTION] candidates (do not create — flag for Editor):
  - This article's "Raw folder, never modified" pattern aligns with house-rules.md Rule 2 (Raw is sacred). Refinery should note this alignment.
  - The article's "nightly compile at 3am + 7am brief" mirrors the Night Shift pipeline in house-rules.md (Scout 11pm, Refinery 3am, Editor 6am). Refinery should note structural overlap, not duplicate content.
