# $340/mo AI Stack → $5/mo Local Second Brain

> Source: Community article by Pilli Shreyas — documenting a local-first AI automation setup using Obsidian + NotebookLM + Hermes Agent

## Overview

A self-learning local knowledge system built to run daily B2B pipelines and lead generation at near-zero token cost. Replaced seven cloud subscriptions ($340/month) with a private stack running on Apple Silicon or local hardware.

**Financial math:**
- Was paying: $340/month across Claude Pro, ChatGPT Plus, Cursor, Perplexity, Midjourney, and others
- Cancelled 6 subscriptions, saved $140 immediately — nothing in workflow changed
- Remaining $200 was only justified because a GPU somewhere was running a model that couldn't be run locally. **In 2026 that is no longer true.**
- Local cost: ~$5/month electricity

---

## The Three-Layer Architecture

By linking active execution, semantic synthesis, and durable storage, we build a private second brain that runs pipelines at zero token cost.

### Layer Matrix

| Layer | Primary Software | Input Source | Output Target |
|-------|-----------------|--------------|---------------|
| **Active** | Hermes Agent / Claude Code | Obsidian Vault / User Commands | Local terminal / SQLite State |
| **Passive** | Google NotebookLM / notebooklm-py | Local PDFs, Markdown, web links | Structured summaries / Audio overviews |
| **Memory** | Obsidian Vault | Raw input logs / Agent outputs | PARA-structured notes |
| **Capture** | Omi / SuperWhisper | Ambient audio / Voice inputs | Markdown files in Obsidian inbox |

### Why Both Tools?

- **NotebookLM** excels at digesting external literature but lacks native local storage or linking
- **Obsidian** stores data securely and provides graph visualization, but lacks native reasoning
- **Together** they form a unified brain that neither tool delivers on its own

Traditional vector search systems fail to track global themes and complex relationships in large vaults. This setup divides labor between four specialized layers instead of forcing one model to handle everything.

---

## The 5-Tier Memory Engine

Prevents context bloat and token waste by distributing data based on stability and frequency.

**Context compression formula:**
> C(t) = S_base + Compress(L(t)) + U_profile

Where C(t) is context window size at turn t, S_base is system prompt size, Compress(L(t)) is compressed historical logs using SQLite FTS5, and U_profile is the user profile (capped at 1,300 tokens).

### The Five Levels

| Level | Name | Storage | Purpose |
|-------|------|---------|---------|
| 1 (Hot) | Local memory | `memory.md` + `user.md` in agent profile (1,300 tokens cap) | Instant preferences and active guidelines |
| 2 (Session) | SQLite FTS5 | `state.db` cross-session search | Fast history retrieval, message search |
| 3 (Active) | Dynamic buffers | In-memory retrieval | Task-relevant context on demand |
| 4 (Durable) | Obsidian PARA | Markdown files on disk | Permanent knowledge, skills, guidelines |
| 5 (Ambient) | Omi transcripts | Daily audio logs | Background context refined into summaries |

**Why this matters:** Standard setups suffer context degradation after ~10 turns because history bloats. Compressing logs into SQLite keeps VRAM free and execution fast. Without this, the agent is guessing. With Obsidian, it has a detailed second brain.

---

## Hardware Specifications

Performance is limited by memory bandwidth. Standard PCs copy data between system RAM and discrete GPU VRAM, limiting speed.

**Apple Silicon advantage:** Unified memory architecture lets CPU and GPU share a single pool — no multi-GPU needed.

| Spec | Basic M4 | M4 Pro |
|------|----------|--------|
| Memory bandwidth | 120 GB/s | 273 GB/s |
| System power | 10–30W sustained | 10–30W sustained |
| Electricity cost | <$5/month | <$5/month |

**Minimal to run local agent pipelines:**
- Running models: Llama-cpp lets a 24GB RAM unit run Qwen 2.5 Coder 14B and Gemma 3 27B headlessly
- Local server: Ollama exposes OpenAI-compatible API to the execution layer

### Setup Commands

```bash
# Install base dependencies
brew install ripgrep ffmpeg node python

# Install Ollama and pull a model
curl -fsSL https://ollama.com/install.sh | sh
ollama pull qwen3.5-coder:32b
```

### Hermes Config (`~/.hermes/config.yaml`)

```yaml
provider: ollama
model: qwen3.5-coder:32b
api_base: http://localhost:11434
```

---

## Automation Pathways & Bridges

Two automated pathways connect local tools and remove manual copy-paste:

### 1. Hermes → Obsidian
- Configure `OBSIDIAN_VAULT_PATH` environment variable
- Use the hermes-agent-obsidian-plugin to run sessions from sidebar

### 2. Hermes → NotebookLM
- Use `notebooklm-py` library to upload files automatically
- For complex tasks, use macos-computer-use skill to control Chrome and generate audio overviews

**Note on notebooklm-py authentication:** The package stores session cookies from browser login. On Windows, use Edge (which was already logged in):

```bash
notebooklm login --browser msedge
```

### Python Bridge Example

```python
from notebooklm import NotebookLM

client = NotebookLM(session_cookie="your_cookie_here")
client.upload_source(vault_path="/Agent_Workspace/research.md")
```

---

## Use Case: Huberman Bulk Ingestion

Want to build a deep research vault of 300 Huberman podcast episodes? Manual process = hundreds of hours. Automated pipeline = minutes.

### The Pipeline

1. **Scrape** — Point agent to YouTube playlist URLs using a custom scraper script
2. **Download** — Agent runs ytcli in parallel to download raw text transcripts from all 300 videos, formatted as structured markdown in Obsidian `/inbox`
3. **Ingest** — `notebooklm-py` logs into NotebookLM, creates a new notebook, and uploads all 300 transcripts in batch
4. **Synthesize** — Issue structured queries: compile health experiments, reference studies, return findings with citations
5. **Store** — Agent saves synthesized output to Obsidian as permanent markdown, linked via `[[wiki-brackets]]` to create a visual graph

Result: Videos cluster around topics (sleep protocols, cold exposure, memory retention) — visible in the Obsidian graph view.

---

## Content Generation Loop

Once research is indexed, turn raw insights into production assets.

**NotebookLM can generate up to 12 deliverable types from a single notebook:**
Mind maps, study guides, briefing documents, audio overviews, quizzes, flashcards, infographics, reports, slide decks, data tables, videos, and podcasts.

### The Content Factory

1. Open Obsidian sidebar → launch local Hermes session
2. Prompt: draft a content series on [topic] for your corporate newsletter
3. Hermes reads synthesized notes in PARA vault, matches against `voice-guidelines.md` for brand tone
4. Agent outputs finished drafts directly to your folder — ready for review

This runs entirely locally. Company guidelines and research stay confidential.

---

## Personal Assistant & Ambient Context

Automate daily logs and task planning without manual entry:

- **Omi tracking** — Wearable captures spoken agreements, syncs transcripts to `/Omi_Memories`
- **Morning standup** — Local cron script at 9:00 reads calendar + yesterday's Omi logs
- **SuperWhisper** — Dictate system changes directly to Apple Silicon processor via local speech recognition
- **Converse Mode** — Forces agent to ask clarifying questions before editing files

This loop converts ambient context into actionable schedules.

---

## Vault Maintenance Schedule

| Frequency | Task |
|-----------|------|
| Weekly | Clear orphan notes, trim `MEMORY.md` if >4,000 chars |
| Monthly / on failure | Audit PARA directories, review `issues-fixes-log.md`, write new rules |

**Important:** Running large 32B models on Mac Mini M4 can throttle during parallel transcriptions. Enforce directory limits to keep agent from accessing host files.

---

## ROI Summary

| | Cost |
|---|---|
| Cloud subscriptions (was) | $340/month |
| Local hardware | $5/month electricity |
| Mac Mini M4 ($599) breaks even | ~3.5 months |

**Year 1 savings:** ~$3,421  
**Year 2+ annual savings:** ~$4,020

This won't build a billion-dollar startup overnight.  
But it will run your B2B research pipeline 24/7 without API limits or monthly credit card bills.

**And that is exactly what a real developer builds with.**

---

## Vault Status

- [x] Obsidian vault: `E:\_Knowledge\ObsidianVault`
- [x] OBSIDIAN_VAULT_PATH: set
- [x] notebooklm-py: installed & authenticated
- [ ] Ollama: not installed (optional — use cloud provider)
- [ ] Omi hardware: not applicable
- [ ] PARA structure: non-standard but functional
- [ ] Memory trimming: manual
- [ ] Automated backup: not configured

## Next Steps

- [ ] Configure automated vault backup
- [ ] Set up cron job for memory trimming
- [ ] Create `voice-guidelines.md` for brand tone
- [ ] Test bulk NotebookLM ingestion with a research topic
- [ ] Set up morning standup cron job

---

*Saved: 2026-07-12*
*Source: Self-authored / shared article*