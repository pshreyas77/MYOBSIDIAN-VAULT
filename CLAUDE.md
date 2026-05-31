---
title: Second Brain — Master Context
created: 2026-05-20
tags: [meta, system]
---

# Second Brain — Master Context

## Identity
Name: Shreyas Pilli (Sunny)
Role: Final-year CSE, MLR Institute of Technology, Hyderabad
Target: Fresher DA/ML/AI roles — actively applying
Stack: Python, SQL, FastAPI, React, LangChain, Ollama, Linux (Feren OS), Windows

## Active Projects
- NeoAttend Agent: autonomous AI attendance, Flask, 14/14 tests passing
- Open Source Agent: multi-agent research platform
- VerifAI: FastAPI + Whisper + spaCy fact-checker
- OmniResearch: ChromaDB + React/Vite
- UCH Research: 3 papers written, enlightenment-as-universal-capacity thesis

## Research Interests
- UCH: universal enlightenment across Advaita, Buddhism, Jainism, Desert Fathers
- Comparative religion: IVC-Vedic-Buddhist-Jain relationships
- Indian philosophy: Nagarjuna (emptiness), Shankara (Advaita), Basavanna
- Ancient history, OSINT, Indian election analysis
- Vigyan Bhairav Tantra, Neti Neti, Vithoba-Buddha connections

## Vault Structure
- /inbox          → unprocessed captures (check first every session)
- /permanent      → atomic Zettelkasten notes, one idea per file
- /wiki           → AI-maintained wiki (Claude writes, I read)
  - /wiki/index.md      → master catalog
  - /wiki/log.md        → append-only history
  - /wiki/hot.md        → recent context cache
  - /wiki/summaries/    → one summary per ingested source
  - /wiki/analyses/     → saved query answers and syntheses
- /raw-sources    → IMMUTABLE inputs (never modify, never delete)
- /projects       → active project folders
- /BOOKS          → book notes
- /BUDDHA         → UCH research nodes
- /Daily Notes    → journal
- /logs/sessions  → session logs YYYY-MM-DD-HH.md
- /Research       → web research outputs (/x-read, /research-deep)

## AI-First Rules (mandatory on every write)
1. Every wiki page: YAML frontmatter (tags, date, source_count, confidence)
2. External claims: recency markers "(as of YYYY-MM, source.com)"
3. Cross-links: [[WikiLink]] for every person/project/concept/decision
4. Sources preserved verbatim — never paraphrase a source URL
5. raw-sources/ is READ-ONLY — Claude reads, never writes

## Session Protocol
### START /resume:
1. Read this CLAUDE.md
2. Run `mempalace wake-up` if available
3. Read /wiki/hot.md for recent context
4. Read /wiki/index.md for vault state
5. Scan /inbox for unprocessed items

### END /save:
1. Update /wiki/hot.md with session summary
2. Append to /wiki/log.md
3. Write session log to /logs/sessions/YYYY-MM-DD-HH.md
4. Suggest 3 new [[wikilinks]] between existing notes
5. Run lint check on wiki/

## Commands
| Command | Purpose |
|---|---|
| /resume | Start session — load all context |
| /save | End session — file everything |
| /ingest [file] | Process source into wiki pages |
| /synthesis | Weekly thesis + contradictions + gaps |
| /brief | Daily brief from recent captures |
| /lint | Wiki health check |
| /query [topic] | Search wiki, answer with citations |
| /autoresearch [topic] | 3-5 round web research → wiki |
| /research-deep [topic] | Vault-first + web gap research |
| /x-read [url] | Read X post → structured vault note |
| /youtube [url] | Transcript + summary → vault |
| /process-inbox | File today's captures to correct locations |
| /process-queue | Process all files in QUEUE\ folder |
| /project-health | Weekly project status assessment |

## What I Want From Claude
- Surface non-obvious connections — cite exact file paths
- Challenge assumptions before agreeing
- Flag contradictions between new and old notes — show both
- Answer from vault first, web second
- Save every valuable analysis to /wiki/analyses/ — never lose insight in chat
- When I ask what to focus on: answer from vault content, not generically