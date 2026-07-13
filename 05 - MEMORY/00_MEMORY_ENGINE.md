---
date: 2026-07-13
type: system
tags: [memory, second-brain, tiered-memory, hot, session, active, durable, ambient]
status: active
---

# 5-Tier Memory Engine

**For Future Claude:** This is your tiered memory system. Every session starts here. Claude reads Level 1 + Level 2 first, then Level 3 on demand. Level 4 is always available via Obsidian path. Level 5 is ambient audio (if Omi is set up).

## The Math

```
C(t) = S_base + Compress(L(t)) + U_profile
```
- `C(t)` = context window size at turn `t`
- `S_base` = system prompt (~2,000 tokens, fixed)
- `Compress(L(t))` = compressed session log via SQLite FTS5
- `U_profile` = user profile, capped at 1,300 tokens

**Without this system:** context degrades after ~10 turns. History bloats, VRAM fills, model loses focus.
**With this system:** session stays clean, execution stays fast.

---

## Tier 1 — HOT (Immediate, 1,300 token cap)

**File:** `05 - MEMORY/00_HOT_LAYER.md`

Fastest access. Loaded every session automatically. Contains:
- Current active projects and their status
- What Claude should do FIRST in this session
- Known user corrections and preferences
- Any burning issues

**Rules:**
- Max 1,300 tokens. Trim ruthlessly.
- Update at END of every session.
- Only touch during session if user explicitly asks.

---

## Tier 2 — SESSION LOG (SQLite FTS5)

**File:** Hermes session database (`~/.hermes/sessions/`)

Cross-session search. Run:
```
session_search(query="Aryan migration", limit=3)
session_search(session_id="abc123", around_message_id=999)
```
- FTS5 search over ALL past sessions
- Returns matches with highlighted snippets
- Bookend messages (first 3 + last 3) for context

**Use when:** user references "what we discussed about X last week"

---

## Tier 3 — ACTIVE CONTEXT (Dynamic retrieval)

**How:** Claude reads relevant Obsidian pages during task execution.

**Trigger:** When user asks about anything in the vault:
1. Use `search_files` in vault to find relevant notes
2. `read_file` the top matches
3. Inject into context
4. Answer from vault, not training data

**Trigger:** When task requires domain knowledge (history, philosophy, politics):
1. Read the relevant `02 - AREAS/` folder
2. Find the MOC (Master Table of Contents)
3. Follow wikilinks for depth

**Rule:** If the vault has it, USE it. Don't hallucinate.

---

## Tier 4 — DURABLE KNOWLEDGE (Permanent, Obsidian)

**Location:** `E:\_Knowledge\ObsidianVault`

PARA structure:
- `00 INBOX` — unsorted captures (process within 48h)
- `02 - AREAS/` — permanent notes by domain (1,194 files)
- `03 - PROJECTS/` — active projects (24 files)
- `05 - OUTPUTS/` — generated reports (NEW — use this)
- `02 - PERMANENT/concepts/` — canonical concept definitions
- `02 - PERMANENT/people/` — canonical person records

**For-Future-Claude preamble pattern (on every wiki page):**
```markdown
**For Future Claude:** [What this page knows, what's uncertain, what to update]
```

**Key MOCs to know:**
- `02 - AREAS/00 - SYSTEM/index.md` — vault entry point
- `02 - AREAS/05 Knowledge Management/00_MASTER_INDEX.md` — if exists

---

## Tier 5 — AMBIENT CONTEXT (Background capture)

**If Omi wearable is set up:** `E:\_Knowledge\ObsidianVault/Omi_Memories/`

**If NOT set up:** This tier is dormant. Skip.

**Morning standup cron (9 AM daily):**
- Reads yesterday's Omi logs
- Reads calendar events
- Produces morning brief in `04 - DAILY/YYYY-MM-DD.md`

---

## Session Startup Sequence

```
1. Read 05 - MEMORY/00_HOT_LAYER.md          (Tier 1 — hot)
2. Check session_search for recent context    (Tier 2 — session)
3. Ask: "What is the user working on right now?"
4. Read relevant vault pages                   (Tier 3 — active)
5. Proceed with task
```

---

## Memory Hygiene Rules

| When | Action |
|------|--------|
| End of every session | Update 00_HOT_LAYER.md if anything changed |
| Weekly (Sunday) | Run kb-healthcheck, trim hot layer if >1,300 tokens |
| Monthly | Audit PARA directories, review 02 - PERMANENT/ |
| On failure | Write to issues-fixes-log.md in 00 - SYSTEM/ |

---

*Memory engine established: 2026-07-13*
*Vault: E:\_Knowledge\ObsidianVault*