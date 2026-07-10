---
date: 2026-07-09
type: permanent
tags: [concept, second-brain, contrarian-loop, vault-automation, contradiction-detection, steelmanning]
ai-first: true
source: Claude conversation — Contrarian Loop design for Obsidian vault
---

# Contrarian Loop — A Vault That Argues With Itself

## For future Claude
This note captures the design for a "Contrarian Loop" — an automated system that runs against the Obsidian vault to surface contradictions, steelman counterarguments, cross-domain analogies, and ghost-self debates. It is the CONTRA layer beyond the standard DO layer of a second brain. Created 2026-07-09. This is a concept awaiting manual proof before automation.

---

## Core Problem
Every second brain system catches duplicates, surfaces patterns, flags dropped threads. But they don't **argue with you**. Your vault contains multiple versions of you from different time periods — each with different conclusions. The 2023 version thought X. The six-months-ago version thought the opposite. Both are in there. Neither is talking to the other.

## The Two Layers

### DO Layer (Standard)
What every second brain article covers:
- Extract ideas
- Find patterns
- Link related notes
- Surface old work

### CONTRA Layer (New)
What this system adds:
- Steelman the strongest counterargument using your own notes
- Surface contradictions between your own notes
- Cross-pollinate concepts from unrelated domains
- Run the "ghost self" — you from six months ago debating you from today

> **The DO layer finds what fits together. The CONTRA layer finds what does not fit.**

## The Stack
- **The vault:** Obsidian, local markdown files. Every note readable and writable by a script. No API wall.
- **The engine:** Claude, split by role. Sonnet for judgment work (steelmanning, contradiction detection, cross-domain analogies). Haiku for tagging, indexing, and cheap parsing.
- **The trigger:** A cron job or file watcher. No new app, no service, no dashboard.

---

## Loop 1: Ingestion With Argument Tags

**Trigger:** New note added or existing note edited.

**Steps:**
1. Read the note
2. Extract the core claim being made
3. Identify the assumption behind that claim
4. Add three fields to frontmatter:
   ```yaml
   claim: [what the note asserts]
   assumption: [what must be true for the claim to hold]
   ready_for_contra: false
   ```
5. If assumption is unclear, flag the note for manual review

**Why the assumption field is the unlock:** Two notes that seem to disagree usually rest on different assumptions. Once the assumption is explicit, the argument becomes tractable. Contradictions become arguments about premises, not surface disagreements.

---

## Loop 2: The Contrarian Loop

**Trigger:** Every 6 hours.

**Four passes:**

### Pass 1 — Steelman
Pick 5 notes at random from the vault. For each, write the strongest counterargument using material from other notes in the vault. Save as `[note-title]-contra.md`.

### Pass 2 — Contradictions
Compare `assumption` fields across all notes. Find pairs where one note's assumption conflicts with another note's claim. List the collision in `memory/CONTRA.md` with **direct quotes from both notes**.

### Pass 3 — Cross-Domain
Pick one note from a technical domain and one from a personal/philosophical domain. Force an analogy between them. Note the connection in `memory/BRIDGES.md`.

### Pass 4 — Ghost Self
Load all notes older than 6 months on the same topic as any note edited in the last 14 days. Write a short paragraph in the voice of past-you reacting to current-you on that topic. Save to `memory/GHOST.md`.

> **Pass 4 is the one that changes how you use the vault.** Reading a note where you from six months ago is telling you from today that you are rationalizing hits different than reading a bullet list of similar ideas.

---

## Critical Rules

### Never auto-merge contradictions
Two notes that contradict each other are not necessarily wrong. They might be about different contexts, different constraints, different phases. A steelman is a **suggestion, not a verdict**.

### Always keep a human in the loop
The loop surfaces — you decide. Auto-resolving will merge two notes about "quitting a bad client" that were actually about two different clients, and you'll lose the reasoning that made both of them right at the time.

---

## Manual Proof First (Before Automation)

Run this prompt manually against real vault notes:

> Read every note in [folder]. For each note:
> 1. Extract the core claim
> 2. Find one other note where the assumption conflicts with this claim
> 3. Write the steelman of the opposite position, using direct quotes from both notes
>
> Success criteria (strict, no soft passes):
> - Every steelman quotes both notes directly
> - Every contradiction pair identifies the assumption gap
> - No vague "you might reconsider X" style output

Run this a few times against the real vault. If what comes back genuinely makes you rethink something, the loop earns a schedule. If not, don't automate it. **Manual proof first, always.**

---

## Build Order (The Order That Actually Works)

1. **Build Loop 1 first.** Let the vault fill with `claim` and `assumption` metadata for at least three weeks. The loop needs material to argue against.
2. **Add Pass 2 (contradictions) manually** a few times. If the collisions surprise you, schedule it.
3. **Then Pass 4 (ghost self).** This needs three months of history minimum to feel real. Ghost self on a young vault is just guessing.
4. **Add Pass 1 (steelman) and Pass 3 (cross-domain) last.** These are entertaining but only hit something interesting once you have critical mass.

**Do not schedule everything on day one.** A loop that runs against three notes will hallucinate connections and train you to ignore the output. Prove each pass by hand, then automate.

---

## Cost
Loop 1 runs once per note change (Haiku calls, fraction of a cent each). Loop 2 runs four passes every six hours — Pass 1 and Pass 3 on Sonnet (judgment work), Pass 2 and Pass 4 on Haiku (comparison, quote extraction). Sixteen passes a day ≈ cost of a single premium coffee. If the loop catches one contradiction that stops a bad decision, it pays for a year of itself in one afternoon.

---

## The Deeper Point
Your best advisor is not Claude. Your best advisor is you from eight months ago, still writing in your vault, waiting for something to translate what they wrote back into a language you will actually listen to. The loop is that translator.

---

## Related
- [[05 - MAPS/Agentic Systems MOC]]
- [[05 - MAPS/Digital Garden MOC]]
- [[03 - PROJECTS/Cross-Domain Idea Synthesis]]
- [[03 - PROJECTS/InfiniteBrain]]
- [[AI-First-Workflow]]