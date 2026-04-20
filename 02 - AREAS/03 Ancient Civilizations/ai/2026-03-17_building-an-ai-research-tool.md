---
title: "Building an AI research tool"
date: 2026-03-17
tags:
  - python
  - sql
  - machine-learning
  - llm-ai
  - data-analysis
  - linux
  - obsidian
  - job-search
  - philosophy
  - geopolitics
  - stock-market
  - osint
  - research
  - projects
  - creative
  - finance
  - web-dev
  - game-design
source: claude-export
---

# Building an AI research tool

> **Conversation Overview**

The person, who goes by Sunny (referenced in file paths as "sunny77"), is building a local multi-agent AI research platform called OmniResearch on an HP ProBook 640 G4 with 8GB RAM, Intel integrated graphics, and CPU-only processing. The conversation focused on generating a detailed OpenCode prompt to build the full platform, then guiding the person through setup, debugging, and optimization. The person uses OpenCode (a terminal-based AI coding agent) with locally running Ollama models rather than cloud APIs, and has a GitHub account at github.com/pshreyas77.

The full 19-file OmniResearch platform was successfully built using a single paste-ready OpenCode prompt, covering a FastAPI backend with five specialized agents (Coordinator, Searcher, Summarizer, Critic, Synthesizer, Debate), ChromaDB vector storage, aiosqlite session management, and a React/Vite frontend with a dark terminal aesthetic. The backend health check confirmed successful connection between FastAPI and Ollama. The person pushed the project to github.com/pshreyas77/omniresearch.git using a Personal Access Token workflow. Key model decisions settled on qwen2.5:0.5b or qwen2.5:1.5b as the sweet spot for the hardware constraints, replacing the originally planned mistral:7b-instruct which caused 100% CPU usage.

Two persistent issues remain unresolved at the end of the conversation: the frontend at localhost:3000 is not loading despite the backend running correctly, and the canvas-based 3D globe animation was causing excessive CPU usage. Fixes were provided for both — removing the animation loop and throttling Ollama via OLLAMA_NUM_THREADS=2 — but the frontend loading issue was still being diagnosed, with Claude requesting output from five diagnostic commands (ss -tlnp, npm run dev, wc -l on App.jsx, vite.config.js, and package.json) that the person had not yet provided. The person indicated they would continue debugging the next day.

**Date:** 2026-03-17  
**Topics:** [[Python]] · [[SQL]] · [[Machine-Learning]] · [[LLM-AI]] · [[Data-Analysis]] · [[Linux]] · [[Obsidian]] · [[Job-Search]] · [[Philosophy]] · [[Geopolitics]] · [[Stock-Market]] · [[OSINT]] · [[Research]] · [[Projects]] · [[Creative]] · [[Finance]] · [[Web-Dev]] · [[Game-Design]]

---

### 🤖 Claude

{'type': 'text', 'text': '     1\t---\n     2\tname: frontend-design\n     3\tdescription: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.\n     4\tlicense: Complete terms in LICENSE.txt\n     5\t---\n     6\t\n     7\tThis skill guides creation of distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. Implement real working code with exceptional attention to aesthetic details and creative choices.\n     8\t\n     9\tThe user provides frontend requirements: a component, page, application, or interface to build. They may include context about the purpose, audience, or technical constraints.\n    10\t\n    11\t## Design Thinking\n    12\t\n    13\tBefore coding, understand the context and commit to a BOLD aesthetic direction:\n    14\t- **Purpose**: What problem does this interface solve? Who uses it?\n    15\t- **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, etc. There are so many flavors to choose from. Use these for inspiration but design one that is true to the aesthetic direction.\n    16\t- **Constraints**: Technical requirements (framework, performance, accessibility).\n    17\t- **Differentiation**: What makes this UNFORGETTABLE? What\'s the one thing someone will remember?\n    18\t\n    19\t**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work - the key is intentionality, not intensity.\n    20\t\n    21\tThen implement working code (HTML/CSS/JS, React, Vue, etc.) that is:\n    22\t- Production-grade and functional\n    23\t- Visually striking and memorable\n    24\t- Cohesive with a clear aesthetic point-of-view\n    25\t- Meticulously refined in every detail\n    26\t\n    27\t## Frontend Aesthetics Guidelines\n    28\t\n    29\tFocus on:\n    30\t- **Typography**: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend\'s aesthetics; unexpected, characterful font choices. Pair a distinctive display font with a refined body font.\n    31\t- **Color & Theme**: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes.\n    32\t- **Motion**: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Use Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions. Use scroll-triggering and hover states that surprise.\n    33\t- **Spatial Composition**: Unexpected layouts. Asymmetry. Overlap. Diagonal flow. Grid-breaking elements. Generous negative space OR controlled density.\n    34\t- **Backgrounds & Visual Details**: Create atmosphere and depth rather than defaulting to solid colors. Add contextual effects and textures that match the overall aesthetic. Apply creative forms like gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, and grain overlays.\n    35\t\n    36\tNEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character.\n    37\t\n    38\tInterpret creatively and make unexpected choices that feel genuinely designed for the context. No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices (Space Grotesk, for example) across generations.\n    39\t\n    40\t**IMPORTANT**: Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate code with extensive animations and effects. Minimalist or refined designs need restraint, precision, and careful attention to spacing, typography, and subtle details. Elegance comes from executing the vision well.\n    41\t\n    42\tRemember: Claude is capable of extraordinary creative work. Don\'t hold back, show what can truly be created when thinking outside the box and committing fully to a distinctive vision.\n    43\t', 'uuid': '105177e7-62ec-4cd8-9d72-7b0cf247755d'}
What would you like me to build? Looking at this document, I can see a few directions:

{'type': 'text', 'text': '{\n  "questions": [\n    {\n      "question": "What do you want me to build from this OmniResearch spec?",\n      "type": "single_select",\n      "options": [\n        "Full interactive landing/demo page for OmniResearch",\n        "Phase 1 backend (FastAPI research engine)",\n        "React frontend UI (dark, hacker aesthetic)",\n        "The complete Claude-powered artifact version of the research tool"\n      ]\n    }\n  ]\n}', 'uuid': '7b97209d-4ce2-416a-8a2c-18921d29fdcd'}
Pick your poison, Sunny — each direction is a solid build. The **Claude-powered artifact** version would be the most immediately usable (a working AI research tool right in the browser using the Anthropic API), while the **FastAPI backend** sets up the actual local stack you'd deploy on your machine.

---

### 🧑 You

[User denied question request]

---

### 🤖 Claude

What do you want me to build? Just tell me directly — no need for a menu.

---

### 🧑 You

generate me an prompt to make it in  an open source deep research platform which has like multiple AI agents working together ti find information for doing research . it should world completly on my system by using ollama or llama.cpp local models . generate me prompt

---

### 🤖 Claude

Here's your OpenCode/Claude Code prompt:

---

```
# Project: DeepResearch Local — Open-Source Multi-Agent Research Platform

## Goal
Build a fully local, open-source deep research platform where multiple specialized AI agents collaborate to research any topic. Zero cloud dependencies. Runs entirely on Ollama or llama.cpp. Designed for 8GB RAM, CPU-only systems (Intel integrated graphics).

---

## System Architecture

### LLM Backend
- Primary: Ollama (http://localhost:11434)
- Fallback: llama.cpp server (http://localhost:8080)
- Default models:
  - Fast/cheap tasks: llama3.2:3b or phi3:mini
  - Smart/synthesis tasks: mistral:7b-instruct or llama3.1:8b
  - Embeddings: nomic-embed-text
- Model selection is configurable via .env

### Backend
- Python 3.10+
- FastAPI with async/await throughout
- SQLite for persistence (research sessions, agent logs, reports)
- ChromaDB for vector storage and semantic search
- asyncio for concurrency (no Redis/Celery dependency)
- WebSockets for real-time agent status streaming to frontend

### Frontend
- React (Vite) — dark, terminal-inspired UI
- Real-time agent activity feed via WebSocket
- Research tree visualization (D3.js)
- Markdown report viewer with citation highlights
- Single-page app, no auth required for local use

### Deployment
- Docker Compose (one command: `docker-compose up`)
- Or bare-metal: `pip install -r requirements.txt && uvicorn main:app`
- Ollama must be running separately on host

---

## Multi-Agent System — Core Feature

Implement a coordinator + specialist agent architecture:

### Agent Roles (all powered by local LLM)
1. **Coordinator Agent** — Breaks query into sub-questions, assigns tasks, merges results
2. **Web Search Agent** — Searches DuckDuckGo/SearXNG, scrapes and reads pages
3. **Summarizer Agent** — Condenses long documents into key facts with source attribution
4. **Critic Agent** — Reviews summaries, flags contradictions, identifies gaps
5. **Synthesizer Agent** — Combines all findings into a coherent final report
6. **Fact-Check Agent** (optional, depth=deep) — Cross-references claims across sources

### Agent Communication Protocol
- Agents communicate via an internal message bus (Python asyncio Queue)
- Each agent has: role, system prompt, input queue, output queue, state (idle/working/done)
- Coordinator orchestrates execution order
- All agent reasoning steps are logged and streamed to frontend in real-time
- Configurable: run agents sequentially (low RAM) or in parallel (more RAM)

### Research Loop
```
User Query
    ↓
Coordinator: decompose into N sub-questions
    ↓
For each sub-question:
    Web Search Agent → fetch URLs → raw content
    Summarizer Agent → extract key facts + citations
    Critic Agent → validate, flag issues
    ↓
Synthesizer Agent → merge all findings
    ↓
Final Report (Markdown + PDF)
```

### Depth Levels
- `quick`: 1 loop, 3 sources, Coordinator + Summarizer only
- `standard`: 3 loops, 10 sources, all agents except Fact-Check
- `deep`: 5+ loops, 20+ sources, all agents including Fact-Check + re-research on gaps

---

## Search & Data Sources

- **Web**: DuckDuckGo (no API key), SearXNG (self-hosted option)
- **Local files**: PDF, DOCX, TXT, CSV ingestion via drag-and-drop or folder watch
- **ArXiv**: Direct API for academic papers
- **Wikipedia**: Direct API for factual grounding
- All fetched content is chunked, embedded (nomic-embed-text), and stored in ChromaDB
- Deduplication: cosine similarity check before storing new chunks

---

## Report Generation

- Output formats: Markdown (default), PDF (via WeasyPrint), DOCX (via python-docx)
- Every claim in the report is linked to its source URL + agent that found it
- Confidence score per claim (based on source count + critic agent rating)
- Reports saved to `/reports/` directory, browsable in UI
- Research sessions are resumable — save state, continue later

---

## API Endpoints (FastAPI)

```
POST   /api/research          — Start new research session
GET    /api/research/{id}     — Get session status + results
GET    /api/research/{id}/report — Download final report
GET    /api/sessions          — List all past sessions
POST   /api/ingest            — Upload local files for research
WS     /ws/research/{id}      — Real-time agent activity stream
GET    /api/models            — List available Ollama models
POST   /api/models/pull       — Pull a new Ollama model
```

---

## Project Structure

```
deepresearch/
├── backend/
│   ├── main.py                  # FastAPI app entry point
│   ├── agents/
│   │   ├── base.py              # BaseAgent class
│   │   ├── coordinator.py
│   │   ├── searcher.py
│   │   ├── summarizer.py
│   │   ├── critic.py
│   │   ├── synthesizer.py
│   │   └── factcheck.py
│   ├── core/
│   │   ├── research_engine.py   # Orchestrates the full loop
│   │   ├── llm_client.py        # Ollama/llama.cpp abstraction
│   │   ├── search.py            # DuckDuckGo + SearXNG
│   │   ├── scraper.py           # Web page fetch + clean
│   │   └── embeddings.py        # ChromaDB + nomic-embed-text
│   ├── models/
│   │   └── schemas.py           # Pydantic models
│   ├── services/
│   │   ├── report_gen.py        # MD/PDF/DOCX export
│   │   └── session_store.py     # SQLite session management
│   └── config.py                # Settings from .env
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/
│   │   │   ├── ResearchForm.jsx
│   │   │   ├── AgentFeed.jsx      # Real-time agent log
│   │   │   ├── ResearchTree.jsx   # D3 visualization
│   │   │   └── ReportViewer.jsx
│   │   └── hooks/
│   │       └── useWebSocket.js
│   └── vite.config.js
├── reports/                     # Generated reports saved here
├── data/                        # Ingested local files
├── .env.example
├── docker-compose.yml
└── requirements.txt
```

---

## .env Configuration

```bash
# LLM
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
FAST_MODEL=llama3.2:3b
SMART_MODEL=mistral:7b-instruct
EMBEDDING_MODEL=nomic-embed-text

# Search
SEARCH_ENGINE=duckduckgo
SEARXNG_URL=
MAX_SEARCH_RESULTS=10

# Research
DEFAULT_DEPTH=standard
MAX_LOOPS=5
MAX_SOURCES=20
REQUEST_TIMEOUT=30

# Storage
DATABASE_URL=sqlite:///./deepresearch.db
VECTOR_DB_PATH=./chroma_db
REPORTS_DIR=./reports

# Performance (tune for 8GB RAM)
PARALLEL_AGENTS=false
MAX_CHUNK_SIZE=1000
EMBEDDING_BATCH_SIZE=8
```

---

## Hardware Constraints & Optimizations

Target: HP ProBook 640 G4, 8GB RAM, Intel integrated graphics, CPU-only

- Always use quantized models (Q4_K_M minimum) via Ollama
- Sequential agent execution by default (PARALLEL_AGENTS=false)
- Streaming LLM responses — never load full response into memory
- Chunk documents to 1000 tokens max before embedding
- Limit concurrent web requests to 3
- Use llama3.2:3b for search/summarize agents, mistral:7b only for synthesis
- SQLite WAL mode for concurrent reads without locking
- Generator patterns for large document processing

---

## Implementation Order

**Phase 1** (build first):
- `llm_client.py` — Ollama API wrapper with streaming
- `base.py` — BaseAgent with message queue
- `coordinator.py` + `summarizer.py` — minimal 2-agent loop
- FastAPI with `/api/research` POST + WebSocket
- Basic React UI: input form + agent log feed

**Phase 2**:
- `searcher.py` (DuckDuckGo) + `scraper.py`
- `critic.py` + `synthesizer.py`
- ChromaDB embeddings + semantic dedup
- Report generation (Markdown + PDF)

**Phase 3**:
- Local file ingestion
- Research tree D3 visualization
- Session resume
- Docker Compose

---

## Constraints

- 100% local inference — no OpenAI, Anthropic, or any cloud LLM API
- No paid services anywhere in the stack
- MIT License
- Must work offline after initial model pull
- Peak RAM usage must stay under 6GB to leave headroom for OS
```

---

**How to use this:** Paste it directly into Claude Code (`claude` CLI), Aider (`aider --model ollama/mistral`), or Cursor. Start with Phase 1 only — say *"implement Phase 1 only"* after the prompt so it doesn't try to build everything at once.

The key design decision here is **sequential agents + 3b model for cheap tasks** — that's what makes it survive on your ProBook without swapping to disk.

---

### 🧑 You

provide me steps to build it in claude code but make sure it is completed using less tokens because i am using ollama cloud models and less tokens so provide me minimal steps to build it faster without completing my tokens in middle of the project

---

### 🤖 Claude

# Claude Code Build Strategy — DeepResearch (Token-Efficient)

---

## Setup First (do this before opening Claude Code)

```bash
mkdir deepresearch && cd deepresearch
git init
```

Create this file structure manually — **don't ask Claude Code to create empty folders:**

```bash
mkdir -p backend/agents backend/core backend/models backend/services frontend/src/components
touch backend/main.py backend/config.py backend/agents/base.py
touch .env docker-compose.yml requirements.txt
```

---

## Rule: How to Talk to Claude Code (Save Tokens)

- ❌ `"Build me the entire research engine with all agents and frontend"`
- ✅ `"Write backend/core/llm_client.py only"` — one file per prompt
- Always say **"no comments, no docstrings"** — saves 20-30% tokens
- Always say **"no explanations, just code"**
- If it starts explaining, type: `"code only"`

---

## Phase 1 — 5 Prompts, Core Working App

---

### Prompt 1 — Config + LLM Client
```
Write backend/config.py and backend/core/llm_client.py.

config.py: pydantic Settings from .env — OLLAMA_BASE_URL, FAST_MODEL, SMART_MODEL, EMBEDDING_MODEL, DATABASE_URL, MAX_SEARCH_RESULTS, REQUEST_TIMEOUT

llm_client.py: OllamaClient class with:
- chat(model, messages, stream=True) → async generator of text chunks
- embed(text) → list[float]
- Uses httpx async, reads from config

No comments. No docstrings. No explanations.
```

---

### Prompt 2 — Base Agent + Coordinator
```
Write backend/agents/base.py and backend/agents/coordinator.py.

base.py: BaseAgent(name, role, llm_client) with:
- async run(input: str) → str
- self.log list for storing steps

coordinator.py: CoordinatorAgent extends BaseAgent:
- decompose(query, depth) → list[str] of sub-questions (calls SMART_MODEL)
- depth "quick"=3, "standard"=5, "deep"=8 sub-questions

No comments. No docstrings. No explanations.
```

---

### Prompt 3 — Searcher + Summarizer
```
Write backend/core/search.py, backend/core/scraper.py, backend/agents/summarizer.py.

search.py: async duckduckgo_search(query, max_results) → list[{title, url, snippet}] using duckduckgo_search pip package

scraper.py: async fetch_page(url) → str (clean text, strip HTML, max 3000 chars) using httpx + BeautifulSoup

summarizer.py: SummarizerAgent extends BaseAgent:
- summarize(query, url, content) → {facts: list[str], source: url}
- Uses FAST_MODEL, prompt: extract key facts relevant to query

No comments. No docstrings. No explanations.
```

---

### Prompt 4 — Research Engine + FastAPI
```
Write backend/core/research_engine.py and backend/main.py.

research_engine.py: ResearchEngine class:
- async research(query, depth) → {report: str, sources: list, logs: list}
- Flow: coordinator.decompose → for each sub-question: search(3 results) → scrape → summarize → collect all facts → final synthesis prompt to SMART_MODEL → return markdown report
- Emit logs via asyncio.Queue passed in constructor

main.py: FastAPI app:
- POST /api/research {query, depth} → {session_id}
- GET /api/research/{id} → {status, report, sources, logs}
- WS /ws/{id} → stream logs from queue
- Store sessions in dict (in-memory, no DB needed for now)

No comments. No docstrings. No explanations.
```

---

### Prompt 5 — Frontend (single file)
```
Write frontend/src/App.jsx as a single-file React app (no component splits).

Features:
- Dark background #0a0a0a, monospace font
- Input: query text + depth select (quick/standard/deep) + submit button
- On submit: POST /api/research, then open WebSocket /ws/{id}
- Left panel: real-time log feed (agent messages scrolling)
- Right panel: markdown report display when done (use marked.js from CDN)
- Minimal CSS inline or in same file

No comments. No explanations. Vite project, index.html imports App.jsx.
```

---

## Phase 2 — 3 Prompts (add after Phase 1 works)

### Prompt 6 — Critic + Synthesizer agents
```
Write backend/agents/critic.py and backend/agents/synthesizer.py.

critic.py: CriticAgent — review(facts: list[str]) → list[str] filtered, removes duplicates/contradictions, uses FAST_MODEL

synthesizer.py: SynthesizerAgent — synthesize(query, all_facts: list, sources: list) → markdown report string, uses SMART_MODEL, structured as: Summary, Key Findings, Sources

Update research_engine.py to use critic before synthesizer.
No comments. No explanations.
```

### Prompt 7 — SQLite sessions
```
Write backend/services/session_store.py.

SQLite via aiosqlite. Table: sessions(id, query, depth, status, report, logs_json, created_at).
Methods: create(query, depth)→id, update(id, status, report, logs), get(id)→dict, list_all()→list

Update main.py to use session_store instead of in-memory dict.
No comments. No explanations.
```

### Prompt 8 — Docker + requirements
```
Write requirements.txt, docker-compose.yml, .env.example, and frontend/index.html.

requirements.txt: fastapi, uvicorn, httpx, beautifulsoup4, duckduckgo-search, aiosqlite, pydantic-settings, python-multipart

docker-compose.yml: two services — backend (port 8000) and frontend (port 3000, node:18, vite dev server). Backend env_file: .env

.env.example: all config keys with defaults

frontend/index.html: standard Vite HTML entry, loads App.jsx, imports marked.js from CDN

No comments. No explanations.
```

---

## Token-Saving Rules (follow always)

| Do | Don't |
|---|---|
| One file per prompt | Ask for "the whole project" |
| "no comments, no docstrings" | Let it write verbose code |
| "code only" if it starts explaining | Ask it to explain what it built |
| Paste errors directly, say "fix only this" | Describe the error in words |
| `"update X to add Y only"` | Re-explain the whole context |

---

## Total: 8 prompts → complete working app

Phase 1 (5 prompts) = working research tool  
Phase 2 (3 prompts) = production-ready  

Start with Prompt 1, test each phase before moving on.

---

### 🧑 You

i will use opencode istead of claude code guide me

---

### 🤖 Claude

# OpenCode Setup & Build Guide — DeepResearch

---

## What is OpenCode
OpenCode is a terminal-based AI coding agent (like Claude Code but runs in your terminal, supports any LLM including Ollama).

---

## Step 1 — Install OpenCode

```bash
# Install via npm
npm install -g opencode-ai

# OR via curl (check latest at github.com/sst/opencode)
curl -fsSL https://opencode.ai/install | bash
```

Verify:
```bash
opencode --version
```

---

## Step 2 — Configure OpenCode to use Ollama

Create config file:
```bash
mkdir -p ~/.config/opencode
nano ~/.config/opencode/config.json
```

Paste this:
```json
{
  "model": "ollama/mistral:7b-instruct",
  "providers": {
    "ollama": {
      "baseURL": "http://localhost:11434"
    }
  }
}
```

Make sure Ollama is running:
```bash
ollama serve
ollama pull mistral:7b-instruct
ollama pull llama3.2:3b
ollama pull nomic-embed-text
```

---

## Step 3 — Create Project Folder

```bash
mkdir deepresearch && cd deepresearch
git init

# Create structure manually (saves tokens — don't ask AI to do this)
mkdir -p backend/agents backend/core backend/models backend/services
mkdir -p frontend/src/components
touch backend/main.py backend/config.py
touch backend/agents/base.py
touch backend/core/llm_client.py
touch .env.example requirements.txt docker-compose.yml
```

---

## Step 4 — Launch OpenCode in Project

```bash
cd deepresearch
opencode
```

You'll see an interactive terminal UI. This is where you paste prompts.

---

## Step 5 — OpenCode-Specific Tips

OpenCode works slightly differently from Claude Code:

| Setting | What to do |
|---|---|
| **Model for coding** | Use `mistral:7b-instruct` (best for code on 8GB) |
| **Context limit** | Keep prompts under 500 words |
| **File targeting** | Say `"write to backend/core/llm_client.py"` explicitly |
| **Auto-apply** | OpenCode will show diff and ask to apply — press `y` |
| **Switch model mid-session** | Type `/model ollama/llama3.2:3b` for cheaper prompts |

---

## Step 6 — Build Order (same 8 prompts, OpenCode style)

### How to enter prompts in OpenCode
Just type or paste in the terminal UI. After each response, press `y` to apply file changes.

---

### Prompt 1 — Config + LLM Client
```
Write backend/config.py and backend/core/llm_client.py.

config.py: pydantic Settings from .env — OLLAMA_BASE_URL, FAST_MODEL, 
SMART_MODEL, EMBEDDING_MODEL, DATABASE_URL, MAX_SEARCH_RESULTS, REQUEST_TIMEOUT

llm_client.py: OllamaClient class:
- async chat(model, messages, stream=True) → async generator of text chunks
- async embed(text) → list[float]
- Uses httpx async, reads from config

No comments. No docstrings. No explanations. Code only.
```

Apply changes → `y`

---

### Prompt 2 — Agents Base + Coordinator
```
Write backend/agents/base.py and backend/agents/coordinator.py.

base.py: BaseAgent(name, role, llm_client) — async run(input) → str, self.log list

coordinator.py: CoordinatorAgent extends BaseAgent:
- async decompose(query, depth) → list[str] sub-questions
- quick=3, standard=5, deep=8 sub-questions, calls SMART_MODEL

No comments. No docstrings. Code only.
```

Apply → `y`

---

### Prompt 3 — Search + Scraper + Summarizer
```
Write backend/core/search.py, backend/core/scraper.py, backend/agents/summarizer.py.

search.py: async duckduckgo_search(query, max_results) → list[{title,url,snippet}]
using duckduckgo_search package

scraper.py: async fetch_page(url) → str clean text max 3000 chars, httpx + BeautifulSoup

summarizer.py: SummarizerAgent — async summarize(query, url, content) → {facts: list[str], source: url}
uses FAST_MODEL

No comments. No docstrings. Code only.
```

Apply → `y`

---

### Prompt 4 — Research Engine + FastAPI
```
Write backend/core/research_engine.py and backend/main.py.

research_engine.py: ResearchEngine:
- async research(query, depth, log_queue) → {report, sources, logs}
- Flow: decompose → search 3 results → scrape → summarize → synthesize with SMART_MODEL → markdown report

main.py: FastAPI:
- POST /api/research {query, depth} → {session_id}
- GET /api/research/{id} → {status, report, sources, logs}
- WS /ws/{id} → stream from asyncio.Queue
- In-memory session dict

No comments. No docstrings. Code only.
```

Apply → `y`

---

### Prompt 5 — Frontend
```
Write frontend/src/App.jsx single file React app.

- Dark #0a0a0a background, monospace font, no component splits
- Query input + depth select + submit button
- POST /api/research on submit, open WebSocket /ws/{id}
- Left: scrolling agent log feed
- Right: markdown report (use marked.js from CDN)
- Inline CSS only

Also write frontend/index.html standard Vite entry importing App.jsx and marked.js CDN.
No comments. Code only.
```

Apply → `y`

---

### Test Phase 1 before continuing

```bash
# Terminal 1
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# Terminal 2
cd frontend
npm create vite@latest . -- --template react
npm install
npm run dev
```

Open `http://localhost:5173` — test a query.

---

### Prompt 6 — Critic + Synthesizer
```
Write backend/agents/critic.py and backend/agents/synthesizer.py.
Then update backend/core/research_engine.py to use them.

critic.py: CriticAgent — async review(facts: list[str]) → list[str], removes duplicates, uses FAST_MODEL
synthesizer.py: SynthesizerAgent — async synthesize(query, facts, sources) → markdown str, uses SMART_MODEL
research_engine.py: insert critic after summarizer, synthesizer at end

No comments. Code only.
```

---

### Prompt 7 — SQLite Sessions
```
Write backend/services/session_store.py using aiosqlite.
Table: sessions(id TEXT, query, depth, status, report, logs_json, created_at)
Methods: create(query,depth)→id, update(id,**kwargs), get(id)→dict, list_all()→list

Update backend/main.py to replace in-memory dict with session_store.
No comments. Code only.
```

---

### Prompt 8 — Docker + Config Files
```
Write requirements.txt, docker-compose.yml, .env.example.

requirements.txt: fastapi uvicorn httpx beautifulsoup4 duckduckgo-search aiosqlite pydantic-settings

docker-compose.yml: backend service port 8000, frontend service port 3000 node:18 vite dev

.env.example:
OLLAMA_BASE_URL=http://localhost:11434
FAST_MODEL=llama3.2:3b
SMART_MODEL=mistral:7b-instruct
EMBEDDING_MODEL=nomic-embed-text
DATABASE_URL=sqlite:///./deepresearch.db
MAX_SEARCH_RESULTS=10
REQUEST_TIMEOUT=30

No comments. Code only.
```

---

## OpenCode Slash Commands (useful)

```
/model ollama/llama3.2:3b     ← switch to cheap model for simple fixes
/model ollama/mistral:7b      ← switch back for complex prompts
/clear                         ← clear context (saves tokens between phases)
/help                          ← list all commands
```

---

## Fix Errors Fast (token-efficient)

When something breaks, paste **only the error**, not the whole file:
```
Fix this error only, no explanations:

ModuleNotFoundError: No module named 'backend.core.llm_client'
File: backend/main.py line 3
```

---

## Total Token Budget Estimate

| Phase | Prompts | Approx Tokens |
|---|---|---|
| Phase 1 (working app) | 5 prompts | ~15k tokens |
| Phase 2 (production) | 3 prompts | ~8k tokens |
| Bug fixes | ~5 fixes | ~5k tokens |
| **Total** | | **~28k tokens** |

Fits comfortably in most Ollama model context windows with room to spare.

---

### 🧑 You

provide me prompt  to paste in opencode

---

### 🤖 Claude

Here's your single paste-ready prompt for OpenCode:

---

```
You are building "DeepResearch" — a local multi-agent research platform using Ollama.

RULES:
- No comments. No docstrings. No explanations. Code only.
- One file at a time, apply immediately.
- Use async/await throughout.
- Target: 8GB RAM, CPU-only, Ollama on localhost:11434

STACK:
- Backend: Python 3.10+, FastAPI, httpx, aiosqlite, BeautifulSoup4, duckduckgo-search, pydantic-settings
- Frontend: React + Vite, single App.jsx file, marked.js from CDN
- Models: FAST=llama3.2:3b, SMART=mistral:7b-instruct

BUILD IN THIS EXACT ORDER:

--- FILE 1: .env ---
OLLAMA_BASE_URL=http://localhost:11434
FAST_MODEL=llama3.2:3b
SMART_MODEL=mistral:7b-instruct
EMBEDDING_MODEL=nomic-embed-text
DATABASE_URL=sqlite:///./deepresearch.db
MAX_SEARCH_RESULTS=8
REQUEST_TIMEOUT=30

--- FILE 2: requirements.txt ---
fastapi uvicorn httpx beautifulsoup4 duckduckgo-search aiosqlite pydantic-settings python-multipart

--- FILE 3: backend/config.py ---
Pydantic BaseSettings loading all keys from .env

--- FILE 4: backend/core/llm_client.py ---
OllamaClient class:
- async chat(model, messages) → str  (calls /api/chat, non-streaming for simplicity)
- async embed(text) → list[float]  (calls /api/embeddings)
- reads baseURL from config

--- FILE 5: backend/agents/base.py ---
BaseAgent(name, role, llm_client):
- async run(input: str) → str
- self.logs: list[str]
- self.log(msg) appends to logs and prints

--- FILE 6: backend/agents/coordinator.py ---
CoordinatorAgent(BaseAgent):
- async decompose(query: str, depth: str) → list[str]
- prompt: "Break this research query into sub-questions. quick=3, standard=5, deep=7. Return only a numbered list."
- parse numbered list from LLM response → return list[str]
- uses SMART_MODEL

--- FILE 7: backend/core/search.py ---
async duckduckgo_search(query: str, max_results: int) → list[dict]
each dict: {title, url, snippet}
uses duckduckgo_search package DDGS

--- FILE 8: backend/core/scraper.py ---
async fetch_page(url: str) → str
httpx GET with 10s timeout, BeautifulSoup extract text from p tags only, return max 2500 chars, handle exceptions → return empty string

--- FILE 9: backend/agents/summarizer.py ---
SummarizerAgent(BaseAgent):
- async summarize(query: str, content: str, url: str) → dict
- returns {facts: list[str], source: url}
- prompt: "Given this content, extract 3-5 key facts relevant to: {query}. Return as numbered list."
- parse numbered list → facts
- uses FAST_MODEL

--- FILE 10: backend/agents/critic.py ---
CriticAgent(BaseAgent):
- async review(facts: list[str]) → list[str]
- prompt: "Remove duplicate or irrelevant facts. Return cleaned numbered list."
- parse and return
- uses FAST_MODEL

--- FILE 11: backend/agents/synthesizer.py ---
SynthesizerAgent(BaseAgent):
- async synthesize(query: str, facts: list[str], sources: list[str]) → str
- returns markdown report with sections: ## Summary, ## Key Findings (bullet list), ## Sources
- uses SMART_MODEL

--- FILE 12: backend/services/session_store.py ---
aiosqlite session store:
- table: sessions(id TEXT PRIMARY KEY, query, depth, status, report, logs_json, created_at)
- async init_db()
- async create_session(query, depth) → id  (use uuid4)
- async update_session(id, **kwargs)
- async get_session(id) → dict
- async list_sessions() → list[dict]

--- FILE 13: backend/core/research_engine.py ---
ResearchEngine(coordinator, summarizer, critic, synthesizer, llm_client):
- async research(query: str, depth: str, on_log: callable) → dict
- Flow:
  1. coordinator.decompose(query, depth) → sub_questions
  2. for each sub_question:
     a. duckduckgo_search(sub_question, max_results=3) → results
     b. for each result: fetch_page(url) → content
     c. summarizer.summarize(query, content, url) → {facts, source}
  3. collect all facts + sources
  4. critic.review(all_facts) → cleaned_facts
  5. synthesizer.synthesize(query, cleaned_facts, sources) → report
  6. call on_log(msg) at each major step
  7. return {report, sources, logs}

--- FILE 14: backend/main.py ---
FastAPI app:
- on startup: init_db()
- POST /api/research body={query: str, depth: str} → {session_id: str}
  - create session, run research_engine in background (asyncio.create_task)
  - update session status to "running" then "done" when complete
- GET /api/research/{id} → session dict
- GET /api/sessions → list all sessions

Instantiate all agents and engine at module level using lifespan.

--- FILE 15: frontend/index.html ---
Standard Vite HTML, import App.jsx as module, load marked.js from CDN: https://cdn.jsdelivr.net/npm/marked/marked.min.js

--- FILE 16: frontend/src/App.jsx ---
Single file React app, no imports except React hooks.
Layout: full dark page #0a0a0a, font: 'Courier New' monospace
- Top: title "DeepResearch" in green #00ff88
- Form: text input (query), select (quick/standard/deep), Submit button
- On submit: POST /api/research → get session_id
- Poll GET /api/research/{id} every 3 seconds until status=done
- Left panel (40%): show logs as they appear, green text on black, scrollable
- Right panel (60%): when done, render report markdown using marked.parse()
- Show loading spinner (ASCII: rotating | / - \) while running
- All CSS inline as style objects

--- FILE 17: docker-compose.yml ---
services:
  backend: python:3.11-slim, workdir /app, copy backend/, pip install, uvicorn main:app --host 0.0.0.0 --port 8000, env_file .env
  frontend: node:18-slim, workdir /app, copy frontend/, npm install, npm run dev -- --host, port 3000

Build all 17 files now in order. After all files are written, show me how to run it with 3 commands.
```

---

Paste this entire block into OpenCode and let it run. It will build all 17 files in sequence. At the end it'll give you the 3 run commands.

---

### 🤖 Claude

Here's your single paste-ready OpenCode prompt for OmniResearch:

---

```
You are building "OmniResearch" — a local-first multi-agent deep research platform.

RULES:
- No comments. No docstrings. No explanations. Code only.
- Build files in exact order listed.
- Use async/await throughout.
- Target: 8GB RAM, CPU-only, Ollama on localhost:11434

STACK:
- Backend: Python 3.10+, FastAPI, httpx, aiosqlite, BeautifulSoup4, duckduckgo-search, pydantic-settings
- Frontend: React + Vite, single App.jsx, marked.js + d3 from CDN
- Models: FAST=llama3.2:3b, SMART=mistral:7b-instruct, EMBED=nomic-embed-text

BUILD ALL FILES IN ORDER:

--- FILE 1: .env ---
OLLAMA_BASE_URL=http://localhost:11434
FAST_MODEL=llama3.2:3b
SMART_MODEL=mistral:7b-instruct
EMBEDDING_MODEL=nomic-embed-text
DATABASE_URL=sqlite:///./omniresearch.db
MAX_SEARCH_RESULTS=8
REQUEST_TIMEOUT=30
ENABLE_OSINT=false
ENABLE_MULTI_AGENT=true

--- FILE 2: requirements.txt ---
fastapi
uvicorn
httpx
beautifulsoup4
duckduckgo-search
aiosqlite
pydantic-settings
python-multipart
chromadb
sentence-transformers

--- FILE 3: backend/config.py ---
Pydantic BaseSettings loading all .env keys above.

--- FILE 4: backend/core/llm_client.py ---
OllamaClient:
- async chat(model, messages) → str  POST /api/chat non-streaming
- async embed(text) → list[float]  POST /api/embeddings
- reads from config

--- FILE 5: backend/agents/base.py ---
BaseAgent(name, role, llm_client):
- async run(input: str) → str
- self.logs: list[str]
- log(msg): append + print with [AgentName] prefix

--- FILE 6: backend/agents/coordinator.py ---
CoordinatorAgent(BaseAgent):
- async decompose(query, depth) → list[str]
- depth: quick=3, standard=5, deep=8 sub-questions
- prompt: "Break this into sub-questions for deep research. Return numbered list only."
- parse numbered list → list[str]
- uses SMART_MODEL

--- FILE 7: backend/agents/searcher.py ---
SearcherAgent(BaseAgent):
- async search(query, max_results) → list[{title,url,snippet}]
- uses duckduckgo_search DDGS
- handles exceptions, returns empty list on failure

--- FILE 8: backend/core/scraper.py ---
async fetch_page(url) → str
httpx GET 10s timeout, BeautifulSoup p-tags only, max 2500 chars, return "" on error

--- FILE 9: backend/agents/summarizer.py ---
SummarizerAgent(BaseAgent):
- async summarize(query, content, url) → {facts: list[str], source: str}
- prompt: "Extract 3-5 key facts relevant to: {query}. Numbered list only."
- parse list → facts
- uses FAST_MODEL

--- FILE 10: backend/agents/critic.py ---
CriticAgent(BaseAgent):
- async review(facts: list[str]) → list[str]
- prompt: "Remove duplicates and irrelevant items. Return cleaned numbered list only."
- uses FAST_MODEL

--- FILE 11: backend/agents/synthesizer.py ---
SynthesizerAgent(BaseAgent):
- async synthesize(query, facts, sources) → str
- returns markdown: ## Summary, ## Key Findings (bullets), ## Sources (numbered)
- uses SMART_MODEL

--- FILE 12: backend/agents/debate.py ---
DebateAgent(BaseAgent):
- personas = ["Economist", "Skeptic", "Optimist", "Historian", "Technical Expert"]
- async debate(query, report) → list[{persona, opinion}]
- for each persona: prompt "As a {persona}, give 2-sentence critique of this research: {report}"
- uses FAST_MODEL
- returns list of persona opinions

--- FILE 13: backend/services/vector_store.py ---
ChromaDB vector store:
- VectorStore class
- async init(collection_name="omniresearch")
- async add(texts: list[str], ids: list[str], metadatas: list[dict])
- async search(query_text, n_results=5) → list[dict]
- uses OllamaClient.embed for embeddings

--- FILE 14: backend/services/session_store.py ---
aiosqlite:
- table: sessions(id TEXT PRIMARY KEY, query, depth, status, report, logs_json, sources_json, debate_json, created_at)
- async init_db()
- async create_session(query, depth) → id (uuid4)
- async update_session(id, **kwargs)
- async get_session(id) → dict
- async list_sessions() → list[dict]

--- FILE 15: backend/core/research_engine.py ---
ResearchEngine(coordinator, searcher, summarizer, critic, synthesizer, debate_agent, vector_store, llm_client):
- async research(query, depth, on_log: callable) → dict
- Flow:
  1. on_log("Decomposing query...")
  2. sub_questions = coordinator.decompose(query, depth)
  3. all_facts, all_sources = [], []
  4. for each sub_question:
     a. on_log(f"Searching: {sub_question}")
     b. results = searcher.search(sub_question, max_results=3)
     c. for each result: content = fetch_page(url) → summarizer.summarize() → collect facts+source
  5. on_log("Reviewing facts...")
  6. cleaned = critic.review(all_facts)
  7. on_log("Synthesizing report...")
  8. report = synthesizer.synthesize(query, cleaned, all_sources)
  9. if ENABLE_MULTI_AGENT:
       on_log("Running agent debate...")
       debate = debate_agent.debate(query, report)
  10. vector_store.add(cleaned, ids, metadatas)
  11. return {report, sources: all_sources, debate, logs}

--- FILE 16: backend/main.py ---
FastAPI app:
- lifespan: init_db(), instantiate all agents + engine
- POST /api/research {query: str, depth: str} → {session_id}
  background task: run engine, update session status running→done
- GET /api/research/{id} → session dict
- GET /api/sessions → list all
- GET /api/health → {"status":"ok","ollama": ping result}

--- FILE 17: frontend/index.html ---
Vite HTML entry. Load from CDN:
- marked.js: https://cdn.jsdelivr.net/npm/marked/marked.min.js
- d3: https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js
Import src/App.jsx as module.

--- FILE 18: frontend/src/App.jsx ---
Single-file React app. No external imports except React hooks.
All CSS as inline style objects.

Design: dark #090909 background, green #00ff88 accent, monospace 'Courier New'

Layout (3 panels):

TOP BAR:
- Title "⬡ OmniResearch" left, green
- Model indicator right: "mistral:7b | llama3.2:3b"

LEFT PANEL (25%):
- "Sessions" heading
- Poll GET /api/sessions every 5s
- List sessions as clickable rows showing query + status badge (green=done, yellow=running)
- Click → load that session into right panels

CENTER PANEL (40%):
- Research form: textarea (query), select depth, Submit button
- On submit: POST /api/research → session_id
- Poll GET /api/research/{id} every 2s until status=done
- Scrollable log feed below form: each log line prefixed with ▸, green text
- ASCII spinner next to status when running: cycle | / - \

RIGHT PANEL (35%):
- Tabs: "Report" | "Debate" | "Sources"
- Report tab: render markdown via marked.parse(), white text
- Debate tab: show list of {persona, opinion} cards, each with colored left border
- Sources tab: numbered list of URLs as links

Show error banner in red if fetch fails.

--- FILE 19: docker-compose.yml ---
services:
  backend:
    image: python:3.11-slim
    working_dir: /app
    volumes: [".:/app"]
    command: bash -c "pip install -r requirements.txt -q && cd backend && uvicorn main:app --host 0.0.0.0 --port 8000 --reload"
    ports: ["8000:8000"]
    env_file: .env
    extra_hosts: ["host.docker.internal:host-gateway"]

  frontend:
    image: node:18-slim
    working_dir: /app
    volumes: ["./frontend:/app"]
    command: bash -c "npm install -q && npm run dev -- --host"
    ports: ["3000:3000"]

Build all 19 files now in order. After completion show exactly 3 commands to run the project.
```

---

**One tip:** After pasting, if OpenCode asks which model to use mid-way, type `/model ollama/llama3.2:3b` to switch to the cheaper model for simple files, then `/model ollama/mistral:7b-instruct` for the engine and main files. Saves tokens on boilerplate.

---

### 🧑 You

qwen-tiny.gguf  model ?

---

### 🤖 Claude

That's a very small model — likely **Qwen2.5-0.5B or 1.5B** quantized as a GGUF file.

**The problem:** Models that small struggle to follow multi-file coding prompts reliably. They'll hallucinate, forget context, and produce broken code halfway through.

**Your options:**

---

{'type': 'text', 'text': '{\n  "questions": [\n    {\n      "question": "How are you running qwen-tiny.gguf?",\n      "type": "single_select",\n      "options": [\n        "llama.cpp server locally",\n        "Ollama (ollama run)",\n        "OpenCode direct GGUF path",\n        "Not sure"\n      ]\n    },\n    {\n      "question": "What do you want to do?",\n      "type": "single_select",\n      "options": [\n        "Use qwen-tiny anyway (simplified prompt)",\n        "Use OpenRouter free models instead (better quality)",\n        "Use Ollama with a proper small model like qwen2.5:3b"\n      ]\n    }\n  ]\n}', 'uuid': '8a663fca-8f9d-494e-94dd-827d59f18e68'}
Tell me how you're running it and what you want to do — I'll give you the exact config and a trimmed prompt that fits within qwen-tiny's limitations.

---

### 🧑 You

Q: How are you running qwen-tiny.gguf?
A: llama.cpp server locally

Q: What do you want to do?
A: which will run best in my system that i will run

---

### 🤖 Claude

Given your HP ProBook 640 G4 — 8GB RAM, Intel integrated graphics, CPU-only — here's the honest recommendation:

---

## Best Model for Your System

**`qwen2.5-coder:3b`** via Ollama

```bash
ollama pull qwen2.5-coder:3b
```

**Why this beats qwen-tiny:**
- Specifically trained for code generation (not general chat)
- 3B params fits easily in 8GB RAM (~2GB loaded, leaves 6GB free)
- Follows multi-file instructions reliably
- Quantized Q4 by default in Ollama
- Faster than mistral:7b on your CPU

---

## If you want to keep llama.cpp instead of Ollama

Download this GGUF and run it:

```bash
# Download
wget https://huggingface.co/Qwen/Qwen2.5-Coder-3B-Instruct-GGUF/resolve/main/qwen2.5-coder-3b-instruct-q4_k_m.gguf

# Run llama.cpp server
./llama-server -m qwen2.5-coder-3b-instruct-q4_k_m.gguf \
  --host 0.0.0.0 \
  --port 8080 \
  --ctx-size 4096 \
  --threads 4 \
  --n-predict 2048
```

Then configure OpenCode:
```json
{
  "model": "openai/qwen2.5-coder",
  "providers": {
    "openai": {
      "baseURL": "http://localhost:8080/v1",
      "apiKey": "none"
    }
  }
}
```

---

## RAM Usage Comparison on Your Machine

| Model | RAM Used | Code Quality | Speed |
|---|---|---|---|
| qwen-tiny (0.5B) | ~0.5GB | ❌ Poor | Fast |
| qwen2.5-coder:3b | ~2GB | ✅ Good | Medium |
| mistral:7b | ~5GB | ✅ Good | Slow |
| llama3.1:8b | ~6GB | ✅ Best | Very slow |

---

**My recommendation:** Use `qwen2.5-coder:3b` via Ollama. It's the sweet spot for your hardware — good enough to follow the 19-file prompt without hallucinating, won't slow your system to a crawl, and zero config needed beyond `ollama pull`.

Want me to update the OpenCode prompt to use `qwen2.5-coder:3b` as both FAST and SMART model?

---

### 🧑 You

not for coding for doing research

---

### 🤖 Claude

Got it — you want to run **research/reasoning tasks** on your system, not coding. Different requirement entirely.

---

## Best Models for Research/Reasoning on Your Hardware

**Top pick: `qwen2.5:3b`** via Ollama

```bash
ollama pull qwen2.5:3b
```

**Why:**
- General purpose, strong reasoning and summarization
- Follows instructions well (numbered lists, structured output)
- Fits in 8GB RAM comfortably
- Better than qwen2.5-coder for research tasks

---

## Full Comparison for Research Use

| Model | RAM | Summarization | Reasoning | Instruction Following |
|---|---|---|---|---|
| qwen-tiny (0.5B) | 0.5GB | ❌ Weak | ❌ Poor | ❌ Unreliable |
| qwen2.5:3b | 2GB | ✅ Good | ✅ Good | ✅ Reliable |
| qwen2.5:7b | 5GB | ✅ Great | ✅ Great | ✅ Very reliable |
| mistral:7b | 5GB | ✅ Great | ✅ Good | ✅ Reliable |
| llama3.2:3b | 2GB | ✅ Good | ✅ Good | ✅ Reliable |

---

## My Recommendation for Your 8GB System

**Use two models together:**

```bash
ollama pull qwen2.5:3b        # FAST model — search, summarize, critic
ollama pull qwen2.5:7b        # SMART model — synthesis, coordinator, final report
```

`qwen2.5:7b` uses ~5GB and `qwen2.5:3b` uses ~2GB — but since they run **sequentially** (not simultaneously) in the research engine, you'll never exceed 5GB at once. Leaves 3GB free for your OS.

---

## Update Your .env

```bash
FAST_MODEL=qwen2.5:3b
SMART_MODEL=qwen2.5:7b
EMBEDDING_MODEL=nomic-embed-text
```

---

**Bottom line:** Ditch qwen-tiny for research. It's too small to summarize paragraphs or follow structured prompts reliably. `qwen2.5:3b` alone will do the job, and adding `qwen2.5:7b` for final synthesis gives you noticeably better reports. Both run fine on your ProBook.

Want me to regenerate the full OpenCode prompt with these two models?

---

### 🧑 You

next ?

---

### 🤖 Claude

It worked! All 19 files built successfully. I can see all the modified files on the right panel.

Now run it:

---

## Step 1 — Install Python dependencies

```bash
cd /home/sunny77/deepresearch/backend
pip install -r ../requirements.txt
```

## Step 2 — Start Ollama + pull models

```bash
# Terminal 1
ollama serve

# Terminal 2 - pull models
ollama pull qwen2.5:3b
ollama pull nomic-embed-text
```

## Step 3 — Start Backend

```bash
cd /home/sunny77/deepresearch/backend
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Step 4 — Start Frontend

```bash
cd /home/sunny77/deepresearch/frontend
npm run dev
```

## Step 5 — Open browser

```
http://localhost:3000
```

---

## If you get errors, paste them here

Most likely errors and quick fixes:

| Error | Fix |
|---|---|
| `ModuleNotFoundError` | `pip install <module>` |
| `Connection refused 11434` | Run `ollama serve` first |
| `CORS error` in browser | Add `origins=["*"]` to FastAPI CORS middleware in main.py |
| `chromadb` crash | `pip install chromadb --upgrade` |

---

Paste any error you see and I'll give you a one-line fix.

---

### 🧑 You

now

---

### 🤖 Claude

**It's fully running!** Health check shows `{"status":"ok","ollama":"ok"}` — both backend and Ollama are connected.

One quick fix needed first:

## Fix the duckduckgo package (1 command)

```bash
pip install ddgs
```

The warning says `duckduckgo_search` was renamed to `ddgs`. Fix it in OpenCode:

```
In backend/agents/searcher.py replace:
from duckduckgo_search import DDGS
with:
from ddgs import DDGS
No explanations.
```

---

## Then open the app

```
http://localhost:3000
```

Try your first research query:

**Query:** `India defence sector investment outlook 2025`
**Depth:** `standard`
**Click Research**

---

You should see:
- Agent logs streaming on the left
- Final markdown report on the right
- Debate panel with Economist/Skeptic/Optimist opinions

That's it — your local multi-agent research platform is live. Let me know what happens when you run the first query.

---

### 🧑 You

not working still in localhost 3000

---

### 🤖 Claude

Share a screenshot of what you see at localhost:3000 — blank page, error, or something else?

Also run this and paste the output:

```bash
curl http://localhost:8000/api/health
```

And check if frontend is actually running:

```bash
curl http://localhost:3000
```

That'll tell me exactly where it's broken.

---

### 🧑 You

still not lodaing

---

### 🤖 Claude

Frontend is running fine — the HTML is being served correctly. It's a **browser cache or React mount issue**.

Try these in order:

## 1. Hard refresh
```
Ctrl + Shift + R
```

## 2. If still blank — open browser console
Press `F12` → Console tab → paste any red errors here

## 3. If you see a white/black blank page, try direct:
```
http://127.0.0.1:3000
```

## 4. Check if App.jsx is being loaded — run this:
```bash
cat /home/sunny77/deepresearch/frontend/src/App.jsx | head -20
```

Paste the output here — I need to see if App.jsx was actually written correctly or if it's empty/broken.

Most likely cause: **App.jsx is empty or has a syntax error** that silently kills React rendering. The HTML loads fine but the React component crashes before mounting.

---

### 🧑 You

once check it is ok or not becaude it is showing "questions"

---

### 🤖 Claude

**It's working!** OmniResearch is live and running your first query. 🎉

I can see:
- ✅ UI loaded perfectly — dark theme, green accents
- ✅ Session created on the left — "running" badge
- ✅ Query submitted: "hi do research about coming AI problem faced in future"
- ✅ Depth: Deep (8 questions)
- ✅ Status: `▸ | Running` — agents are working

---

## The "questions" thing is normal

That's the **Coordinator Agent** decomposing your query into 8 sub-questions before searching. It's working correctly — Deep mode takes **5-15 minutes on your CPU** because it:

1. Breaks into 8 sub-questions
2. Searches web for each
3. Scrapes + summarizes each result
4. Critic reviews all facts
5. Synthesizer writes final report
6. Debate agents give opinions

---

## Just wait

Keep the browser open. The left panel will show logs as each agent finishes. When done, the **Report tab** on the right will fill with your markdown research report.

**Tip for next time:** Use `quick` or `standard` depth first to test — it finishes in 1-3 minutes instead of 15. Use `deep` only for serious research queries.

Your local AI research platform is fully operational. 🚀

---

### 🧑 You

change UI to this but in more unique and better colors combinations to make it look more good

---

### 🤖 Claude

That's a gorgeous UI — agent swarm panel, knowledge graph globe, live OSINT, consensus meter. Let me build that.

{'type': 'text', 'text': '# Imagine — Visual Creation Suite\n\n## Modules\nCall read_me again with the modules parameter to load detailed guidance:\n- `diagram` — SVG flowcharts, structural diagrams, illustrative diagrams\n- `mockup` — UI mockups, forms, cards, dashboards\n- `interactive` — interactive explainers with controls\n- `chart` — charts, data analysis, geographic maps (Chart.js, D3 choropleth)\n- `art` — illustration and generative art\nPick the closest fit. The module includes all relevant design guidance.\n\n**Complexity budget — hard limits:**\n- Box subtitles: ≤5 words. Detail goes in click-through (`sendPrompt`) or the prose below — not the box.\n- Colors: ≤2 ramps per diagram. If colors encode meaning (states, tiers), add a 1-line legend. Otherwise use one neutral ramp.\n- Horizontal tier: ≤4 boxes at full width (~140px each). 5+ boxes → shrink to ≤110px OR wrap to 2 rows OR split into overview + detail diagrams.\n\nIf you catch yourself writing "click to learn more" in prose, the diagram itself must ACTUALLY be sparse. Don\'t promise brevity then front-load everything.\n\nYou create rich visual content — SVG diagrams/illustrations and HTML interactive widgets — that renders inline in conversation. The best output feels like a natural extension of the chat.\n\n## Core Design System\n\nThese rules apply to ALL use cases.\n\n### Philosophy\n- **Seamless**: Users shouldn\'t notice where claude.ai ends and your widget begins.\n- **Flat**: No gradients, mesh backgrounds, noise textures, or decorative effects. Clean flat surfaces.\n- **Compact**: Show the essential inline. Explain the rest in text.\n- **Text goes in your response, visuals go in the tool** — All explanatory text, descriptions, introductions, and summaries must be written as normal response text OUTSIDE the tool call. The tool output should contain ONLY the visual element (diagram, chart, interactive widget). Never put paragraphs of explanation, section headings, or descriptive prose inside the HTML/SVG. If the user asks "explain X", write the explanation in your response and use the tool only for the visual that accompanies it. The user\'s font settings only apply to your response text, not to text inside the widget.\n\n### Streaming\nOutput streams token-by-token. Structure code so useful content appears early.\n- **HTML**: `<style>` (short) → content HTML → `<script>` last.\n- **SVG**: `<defs>` (markers) → visual elements immediately.\n- Prefer inline `style="..."` over `<style>` blocks — inputs/controls must look correct mid-stream.\n- Keep `<style>` under ~15 lines. Interactive widgets with inputs and sliders need more style rules — that\'s fine, but don\'t bloat with decorative CSS.\n- Gradients, shadows, and blur flash during streaming DOM diffs. Use solid flat fills instead.\n\n### Rules\n- No `<!-- comments -->` or `/* comments */` (waste tokens, break streaming)\n- No font-size below 11px\n- No emoji — use CSS shapes or SVG paths\n- No gradients, drop shadows, blur, glow, or neon effects\n- No dark/colored backgrounds on outer containers (transparent only — host provides the bg)\n- **Typography**: The default font is Anthropic Sans. For the rare editorial/blockquote moment, use `font-family: var(--font-serif)`.\n- **Headings**: h1 = 22px, h2 = 18px, h3 = 16px — all `font-weight: 500`. Heading color is pre-set to `var(--color-text-primary)` — don\'t override it. Body text = 16px, weight 400, `line-height: 1.7`. **Two weights only: 400 regular, 500 bold.** Never use 600 or 700 — they look heavy against the host UI.\n- **Sentence case** always. Never Title Case, never ALL CAPS. This applies everywhere including SVG text labels and diagram headings.\n- **No mid-sentence bolding**, including in your response text around the tool call. Entity names, class names, function names go in `code style` not **bold**. Bold is for headings and labels only.\n- The widget container is `display: block; width: 100%`. Your HTML fills it naturally — no wrapper div needed. Just start with your content directly. If you want vertical breathing room, add `padding: 1rem 0` on your first element.\n- Never use `position: fixed` — the iframe viewport sizes itself to your in-flow content height, so fixed-positioned elements (modals, overlays, tooltips) collapse it to `min-height: 100px`. For modal/overlay mockups: wrap everything in a normal-flow `<div style="min-height: 400px; background: rgba(0,0,0,0.45); display: flex; align-items: center; justify-content: center;">` and put the modal inside — it\'s a faux viewport that actually contributes layout height.\n- No DOCTYPE, `<html>`, `<head>`, or `<body>` — just content fragments.\n- When placing text on a colored background (badges, pills, cards, tags), use the darkest shade from that same color family for the text — never plain black or generic gray.\n- **Corners**: use `border-radius: var(--border-radius-md)` (or `-lg` for cards) in HTML. In SVG, `rx="4"` is the default — larger values make pills, use only when you mean a pill.\n- **No rounded corners on single-sided borders** — if using `border-left` or `border-top` accents, set `border-radius: 0`. Rounded corners only work with full borders on all sides.\n- **No titles or prose inside the tool output** — see Philosophy above.\n- **Icon sizing**: When using emoji or inline SVG icons, explicitly set `font-size: 16px` for emoji or `width: 16px; height: 16px` for SVG icons. Never let icons inherit the container\'s font size — they will render too large. For larger decorative icons, use 24px max.\n- No tabs, carousels, or `display: none` sections during streaming — hidden content streams invisibly. Show all content stacked vertically. (Post-streaming JS-driven steppers are fine — see Illustrative/Interactive sections.)\n- No nested scrolling — auto-fit height.\n- Scripts execute after streaming — load libraries via `<script src="https://cdnjs.cloudflare.com/ajax/libs/...">` (UMD globals), then use the global in a plain `<script>` that follows.\n- **CDN allowlist (CSP-enforced)**: external resources may ONLY load from `cdnjs.cloudflare.com`, `esm.sh`, `cdn.jsdelivr.net`, `unpkg.com`. All other origins are blocked by the sandbox — the request silently fails.\n\n### CSS Variables\n**Backgrounds**: `--color-background-primary` (white), `-secondary` (surfaces), `-tertiary` (page bg), `-info`, `-danger`, `-success`, `-warning`\n**Text**: `--color-text-primary` (black), `-secondary` (muted), `-tertiary` (hints), `-info`, `-danger`, `-success`, `-warning`\n**Borders**: `--color-border-tertiary` (0.15α, default), `-secondary` (0.3α, hover), `-primary` (0.4α), semantic `-info/-danger/-success/-warning`\n**Typography**: `--font-sans`, `--font-serif`, `--font-mono`\n**Layout**: `--border-radius-md` (8px), `--border-radius-lg` (12px — preferred for most components), `--border-radius-xl` (16px)\nAll auto-adapt to light/dark mode. For custom colors in HTML, use CSS variables.\n\n**Dark mode is mandatory** — every color must work in both modes:\n- In SVG: use the pre-built color classes (`c-blue`, `c-teal`, `c-amber`, etc.) for colored nodes — they handle light/dark mode automatically. Never write `<style>` blocks for colors.\n- In SVG: every `<text>` element needs a class (`t`, `ts`, `th`) — never omit fill or use `fill="inherit"`. Inside a `c-{color}` parent, text classes auto-adjust to the ramp.\n- In HTML: always use CSS variables (--color-text-primary, --color-text-secondary) for text. Never hardcode colors like color: #333 — invisible in dark mode.\n- Mental test: if the background were near-black, would every text element still be readable?\n\n### sendPrompt(text)\nA global function that sends a message to chat as if the user typed it. Use it when the user\'s next step benefits from Claude thinking. Handle filtering, sorting, toggling, and calculations in JS instead.\n\n### Links\n`<a href="https://...">` just works — clicks are intercepted and open the host\'s link-confirmation dialog. Or call `openLink(url)` directly.\n\n## When nothing fits\nPick the closest use case below and adapt. When nothing fits cleanly:\n- Default to editorial layout if the content is explanatory\n- Default to card layout if the content is a bounded object\n- All core design system rules still apply\n- Use `sendPrompt()` for any action that benefits from Claude thinking\n\n\n## Color palette\n\n9 color ramps, each with 7 stops from lightest to darkest. 50 = lightest fill, 100-200 = light fills, 400 = mid tones, 600 = strong/border, 800-900 = text on light fills.\n\n| Class | Ramp | 50 (lightest) | 100 | 200 | 400 | 600 | 800 | 900 (darkest) |\n|-------|------|------|-----|-----|-----|-----|-----|------|\n| `c-purple` | Purple | #EEEDFE | #CECBF6 | #AFA9EC | #7F77DD | #534AB7 | #3C3489 | #26215C |\n| `c-teal` | Teal | #E1F5EE | #9FE1CB | #5DCAA5 | #1D9E75 | #0F6E56 | #085041 | #04342C |\n| `c-coral` | Coral | #FAECE7 | #F5C4B3 | #F0997B | #D85A30 | #993C1D | #712B13 | #4A1B0C |\n| `c-pink` | Pink | #FBEAF0 | #F4C0D1 | #ED93B1 | #D4537E | #993556 | #72243E | #4B1528 |\n| `c-gray` | Gray | #F1EFE8 | #D3D1C7 | #B4B2A9 | #888780 | #5F5E5A | #444441 | #2C2C2A |\n| `c-blue` | Blue | #E6F1FB | #B5D4F4 | #85B7EB | #378ADD | #185FA5 | #0C447C | #042C53 |\n| `c-green` | Green | #EAF3DE | #C0DD97 | #97C459 | #639922 | #3B6D11 | #27500A | #173404 |\n| `c-amber` | Amber | #FAEEDA | #FAC775 | #EF9F27 | #BA7517 | #854F0B | #633806 | #412402 |\n| `c-red` | Red | #FCEBEB | #F7C1C1 | #F09595 | #E24B4A | #A32D2D | #791F1F | #501313 |\n\n**How to assign colors**: Color should encode meaning, not sequence. Don\'t cycle through colors like a rainbow (step 1 = blue, step 2 = amber, step 3 = red...). Instead:\n- Group nodes by **category** — all nodes of the same type share one color. E.g. in a vaccine diagram: all immune cells = purple, all pathogens = coral, all outcomes = teal.\n- For illustrative diagrams, map colors to **physical properties** — warm ramps for heat/energy, cool for cold/calm, green for organic, gray for structural/inert.\n- Use **gray for neutral/structural** nodes (start, end, generic steps).\n- Use **2-3 colors per diagram**, not 6+. More colors = more visual noise. A diagram with gray + purple + teal is cleaner than one using every ramp.\n- **Prefer purple, teal, coral, pink** for general diagram categories. Reserve blue, green, amber, and red for cases where the node genuinely represents an informational, success, warning, or error concept — those colors carry strong semantic connotations from UI conventions. (Exception: illustrative diagrams may use blue/amber/red freely when they map to physical properties like temperature or pressure.)\n\n**Text on colored backgrounds:** Always use the 800 or 900 stop from the same ramp as the fill. Never use black, gray, or --color-text-primary on colored fills. **When a box has both a title and a subtitle, they must be two different stops** — title darker (800 in light mode, 100 in dark), subtitle lighter (600 in light, 200 in dark). Same stop for both reads flat; the weight difference alone isn\'t enough. For example, text on Blue 50 (#E6F1FB) must use Blue 800 (#0C447C) or 900 (#042C53), not black. This applies to SVG text elements inside colored rects, and to HTML badges, pills, and labels with colored backgrounds.\n\n**Light/dark mode quick pick** — use only stops from the table, never off-table hex values:\n- **Light mode**: 50 fill + 600 stroke + **800 title / 600 subtitle**\n- **Dark mode**: 800 fill + 200 stroke + **100 title / 200 subtitle**\n- Apply `c-{ramp}` to a `<g>` wrapping shape+text, or directly to a `<rect>`/`<circle>`/`<ellipse>`. Never to `<path>` — paths don\'t get ramp fill. For colored connector strokes use inline `stroke="#..."` (any mid-ramp hex works in both modes). Dark mode is automatic for ramp classes. Available: c-gray, c-blue, c-red, c-amber, c-green, c-teal, c-purple, c-coral, c-pink.\n\nFor status/semantic meaning in UI (success, warning, danger) use CSS variables. For categorical coloring in both diagrams and UI, use these ramps.\n\n\n## SVG setup\n\n**ViewBox safety checklist** — before finalizing any SVG, verify:\n1. Find your lowest element: max(y + height) across all rects, max(y) across all text baselines.\n2. Set viewBox height = that value + 40px buffer.\n3. Find your rightmost element: max(x + width) across all rects. All content must stay within x=0 to x=680.\n4. For text with text-anchor="end", the text extends LEFT from x. If x=118 and text is 200px wide, it starts at x=-82 — outside the viewBox. Increase x or use text-anchor="start".\n5. Never use negative x or y coordinates. The viewBox starts at 0,0.\n6. Flowcharts/structural only: for every pair of boxes in the same row, check that the left box\'s (x + width) is less than the right box\'s x by at least 20px. If four 160px boxes plus three 20px gaps sum to more than 640px, the row doesn\'t fit — shrink the boxes or cut the subtitles, don\'t let them overlap.\n\n**SVG setup**: `<svg width="100%" viewBox="0 0 680 H">` — 680px wide, flexible height. Set H to fit content tightly — the last element\'s bottom edge + 40px padding. Don\'t leave excess empty space below the content. Safe area: x=40 to x=640, y=40 to y=(H-40). Background transparent. **Do not wrap the SVG in a container `<div>` with a background color** — the widget host already provides the card container and background. Output the raw `<svg>` element directly.\n\n**The 680 in viewBox is load-bearing — do not change it.** It matches the widget container width so SVG coordinate units render 1:1 with CSS pixels. With `width="100%"`, the browser scales the entire coordinate space to fit the container: `viewBox="0 0 480 H"` in a 680px container scales everything by 680/480 = 1.42×, so your `class="th"` 14px text renders at ~20px. The font calibration table below and all "text fits in box" math assume 1:1. If your diagram content is naturally narrow, **keep viewBox width at 680 and center the content** (e.g. content spans x=180..500) — do not shrink the viewBox to hug the content. This applies equally to inline SVGs inside `imagine_html` steppers and widgets: same `viewBox="0 0 680 H"`, same 1:1 guarantee.\n\n**viewBox height:** After layout, find max_y (bottom-most point of any shape, including text baselines + 4px descent). Set viewBox height = max_y + 20. Don\'t guess.\n\n**text-anchor=\'end\' at x<60 is risky** — the longest label will extend left past x=0. Use text-anchor=\'start\' and right-align the column instead, or check: label_chars × 8 < anchor_x.\n\n**One SVG per tool call** — each call must contain exactly one <svg> element. Never leave an abandoned or partial SVG in the output. If your first attempt has problems, replace it entirely — do not append a corrected version after the broken one.\n\n**Style rules for all diagrams**:\n- Every `<text>` element must carry one of the pre-built classes (`t`, `ts`, `th`). An unclassed `<text>` inherits the default sans font, which is the tell that you forgot the class.\n- Use only two font sizes: 14px for node/region labels (class="t" or "th"), 12px for subtitles, descriptions, and arrow labels (class="ts"). No other sizes.\n- No decorative step numbers, large numbering, or oversized headings outside boxes.\n- No icons or illustrations inside boxes — text only. (Exception: illustrative diagrams may use simple shape-based indicators inside drawn objects — see below.)\n- Sentence case on all labels.\n\n**Font size calibration for diagram text labels** - Here\'s csv table to give you better sense of the Anthropic Sans font rendering width:\n```csv\ntext, chars length, font-weight, font-size, rendered width\nAuthentication Service, chars: 22, font-weight: 500, font-size: 14px, width: 167px\nBackground Job Processor, chars: 24, font-weight: 500, font-size: 14px, width: 201px\nDetects and validates incoming tokens, chars: 37, font-weight: 400, font-size: 14px, width: 279px\nforwards request to, chars: 19, font-weight: 400, font-size: 12px, width: 123px\nデータベースサーバー接続, chars: 12, font-weight: 400, font-size: 14px, width: 181px\n```\n\nBefore placing text in a box, check: does (text width + 2×padding) fit the container?\n\n**SVG `<text>` never auto-wraps.** Every line break needs an explicit `<tspan x="..." dy="1.2em">`. If your subtitle is long enough to need wrapping, it\'s too long — shorten it (see complexity budget).\n\n**Example check**: You want to put "Glucose (C₆H₁₂O₆)" in a rounded rect. The text is 20 characters at 14px ≈ 180px wide. Add 2×24px padding = 228px minimum box width. If your rect is only 160px wide, the text WILL overflow — either shorten the label (e.g. just "Glucose") or widen the box. Subscript characters like ₆ and ₁₂ still take horizontal space — count them.\n\n**Pre-built classes** (already loaded in SVG widget):\n- `class="t"` = sans 14px primary, `class="ts"` = sans 12px secondary, `class="th"` = sans 14px medium (500)\n- `class="box"` = neutral rect (bg-secondary fill, border stroke)\n- `class="node"` = clickable group with hover effect (cursor pointer, slight dim on hover)\n- `class="arr"` = arrow line (1.5px, open chevron head)\n- `class="leader"` = dashed leader line (tertiary stroke, 0.5px, dashed)\n- `class="c-{ramp}"` = colored node (c-blue, c-teal, c-amber, c-green, c-red, c-purple, c-coral, c-pink, c-gray). Apply to `<g>` or shape element (rect/circle/ellipse), NOT to paths. Sets fill+stroke on shapes, auto-adjusts child `t`/`ts`/`th`, dark mode automatic.\n\n**c-{ramp} nesting:** These classes use direct-child selectors (`>`). Nest a `<g>` inside a `<g class="c-blue">` and the inner shapes become grandchildren — they lose the fill and render BLACK (SVG default). Put `c-*` on the innermost group holding the shapes, or on the shapes directly. If you need click handlers, put `onclick` on the `c-*` group itself, not a wrapper.\n\n- Short aliases: `var(--p)`, `var(--s)`, `var(--t)`, `var(--bg2)`, `var(--b)`\n- Arrow marker: always include this `<defs>` at the start of every SVG:\n  `<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>`\n  Then use `marker-end="url(#arrow)"` on lines. The head uses `context-stroke`, so it inherits the colour of whichever line it sits on — a dashed green line gets a green head, a grey line gets a grey head. Never a colour mismatch. Do not add filters, patterns, or extra markers to `<defs>`. Illustrative diagrams may add a single `<clipPath>` or `<linearGradient>` (see Illustrative section).\n\n**Minimize standalone labels.** Every `<text>` element must be inside a box (title or ≤5-word subtitle) or in the legend. Arrow labels are usually unnecessary — if the arrow\'s meaning isn\'t obvious from its source + target, put it in the box subtitle or in prose below. Labels floating in space collide with things and are ambiguous.\n\n**Stroke width:** Use 0.5px strokes for diagram borders and edges — not 1px or 2px. Thin strokes feel more refined.\n\n**Connector paths need `fill="none"`.** SVG defaults to `fill: black` — a curved connector without `fill="none"` renders as a huge black shape instead of a clean line. Every `<path>` or `<polyline>` used as a connector/arrow MUST have `fill="none"`. Only set fill on shapes meant to be filled (rects, circles, polygons).\n\n**Rect rounding:** `rx="4"` for subtle corners. `rx="8"` max for emphasized rounding. `rx` ≥ half the height = pill shape — deliberate only.\n\n**Schematic containers use dashed rects with a label.** Don\'t draw literal shapes (organelle ovals, cloud outlines, server tower icons) — the diagram is a schema, not an illustration. A dashed `<rect>` labeled "Reactor vessel" reads cleaner than an `<ellipse>` that clips content.\n\n**Lines stop at component edges.** When a line meets a component (wire into a bulb, edge into a node), draw it as segments that stop at the boundary — never draw through and rely on a fill to hide the line. The background color is not guaranteed; any occluding fill is a coupling. Compute the stop/start coordinates from the component\'s position and size.\n\n**Physical-color scenes (sky, water, grass, skin, materials):** Use ALL hardcoded hex — never mix with `c-*` theme classes. The scene should not invert in dark mode. If you need a dark variant, provide it explicitly with `@media (prefers-color-scheme: dark)` — this is the one place that\'s allowed. Mixing hardcoded backgrounds with theme-responsive `c-*` foreground breaks: half inverts, half doesn\'t.\n\n**No rotated text**. `<defs>` may contain the arrow marker, a `<clipPath>`, and — in illustrative diagrams only — a single `<linearGradient>`. Nothing else: no filters, no patterns, no extra markers.\n\n\n## Diagram types\n*"Explain how compound interest works" / "How does a process scheduler work"*\n\n**Two rules that cause most diagram failures — check these before writing each arrow and each box:**\n1. **Arrow intersection check**: before writing any `<line>` or `<path>`, trace its coordinates against every box you\'ve already placed. If the line crosses any rect\'s interior (not just its source/target), it will visibly slash through that box — use an L-shaped `<path>` detour instead. This applies to arrows crossing labels too.\n2. **Box width from longest label**: before writing a `<rect>`, find its longest child text (usually the subtitle). `rect_width = max(title_chars × 8, subtitle_chars × 7) + 24`. A 100px-wide box holds at most a 10-char subtitle. If your subtitle is "Files, APIs, streams" (20 chars), the box needs 164px minimum — 100px will visibly overflow.\n\n**Tier packing:** Compute total width BEFORE placing. Example — 4 pub/sub consumer boxes:\n- WRONG: x=40,160,260,360 w=160 → 40-60px overlaps (4×160=640 > 480 available)\n- RIGHT: x=50,200,350,500 w=130 gap=20 → fits (4×130 + 3×20 = 580 ≤ 590 safe width; right edge at 630 ≤ 640)\nWork bottom-up for trees: size leaf tier first, parent width ≥ sum of children.\n\n**Diagrams are the hardest use case** — they have the highest failure rate due to precise coordinate math. Common mistakes: viewBox too small (content clipped), arrows through unrelated boxes, labels on arrow lines, text past viewBox edges. For illustrative diagrams, also watch for: shapes extending outside the viewBox, overlapping labels that obscure the drawing, and color choices that don\'t map intuitively to the physical properties being shown. Double-check coordinates before finalizing.\n\nUse `imagine_svg` for diagrams. The widget automatically wraps SVG output in a card.\n\n**Pick the right diagram type.** The decision is about *intent*, not subject matter. Ask: is the user trying to *document* this, or *understand* it?\n\n**Reference diagrams** — the user wants a map they can point at. Precision matters more than feeling. Boxes, labels, arrows, containment. These are the diagrams you\'d find in documentation.\n- **Flowchart** — steps in sequence, decisions branching, data transforming. Good for: approval workflows, request lifecycles, build pipelines, "what happens when I click submit". Trigger phrases: *"walk me through the process"*, *"what are the steps"*, *"what\'s the flow"*.\n- **Structural diagram** — things inside other things. Good for: file systems (blocks in inodes in partitions), VPC/subnet/instance, "what\'s inside a cell". Trigger phrases: *"what\'s the architecture"*, *"how is this organised"*, *"where does X live"*.\n\n**Intuition diagrams** — the user wants to *feel* how something works. The goal isn\'t a correct map, it\'s the right mental model. These should look nothing like a flowchart. The subject doesn\'t need a physical form — it needs a *visual metaphor*.\n- **Illustrative diagram** — draw the mechanism. Physical things get cross-sections (water heaters, engines, lungs). Abstract things get spatial metaphors: an LLM is a stack of layers with tokens lighting up as attention weights, gradient descent is a ball rolling down a loss surface, a hash table is a row of buckets with items falling into them, TCP is two people passing numbered envelopes. Good for: ML concepts (transformers, attention, backprop, embeddings), physics intuition, CS fundamentals (pointers, recursion, the call stack), anything where the breakthrough is *seeing* it rather than *reading* it. Trigger phrases: *"how does X actually work"*, *"explain X"*, *"I don\'t get X"*, *"give me an intuition for X"*.\n\n**Route on the verb, not the noun.** Same subject, different diagram depending on what was asked:\n\n| User says | Type | What to draw |\n|---|---|---|\n| "how do LLMs work" | **Illustrative** | Token row, stacked layer slabs, attention threads glowing warm between tokens. Go interactive if you can. |\n| "transformer architecture" | Structural | Labelled boxes: embedding, attention heads, FFN, layer norm. |\n| "how does attention work" | **Illustrative** | One query token, a fan of lines to every key, line opacity = weight. |\n| "how does gradient descent work" | **Illustrative** | Contour surface, a ball, a trail of steps. Slider for learning rate. |\n| "what are the training steps" | Flowchart | Forward → loss → backward → update. Boxes and arrows. |\n| "how does TCP work" | **Illustrative** | Two endpoints, numbered packets in flight, an ACK returning. |\n| "TCP handshake sequence" | Flowchart | SYN → SYN-ACK → ACK. Three boxes. |\n| "explain the Krebs cycle" / "how does the event loop work" | **HTML stepper** | Click through stages. Never a ring. |\n| "how does a hash map work" | **Illustrative** | Key falling through a funnel into one of N buckets. |\n| "draw the database schema" / "show me the ERD" | **mermaid.js** | `erDiagram` syntax. Not SVG. |\n\nThe illustrative route is the default for *"how does X work"* with no further qualification. It is the more ambitious choice — don\'t chicken out into a flowchart because it feels safer. Claude draws these well.\n\nDon\'t mix families in one diagram. If you need both, draw the intuition version first (build the mental model), then the reference version (fill in the precise labels) as a second tool call with prose between.\n\n**For complex topics, use multiple SVG calls** — break the explanation into a series of smaller diagrams rather than one dense diagram. Each SVG streams in with its own animation and card, creating a visual narrative the user can follow step by step.\n\n**Always add prose between diagrams** — never stack multiple SVG calls back-to-back without text. Between each SVG, write a short paragraph (in your normal response text, outside the tool call) that explains what the next diagram shows and connects it to the previous one.\n\n**Promise only what you deliver** — if your response text says "here are three diagrams", you must include all three tool calls. Never promise a follow-up diagram and omit it. If you can only fit one diagram, adjust your text to match. One complete diagram is better than three promised and one delivered.\n\n#### Flowchart\n\nFor sequential processes, cause-and-effect, decision trees.\n\n**Planning**: Size boxes to fit their text generously. At 14px sans-serif, each character is ~8px wide — a label like "Load Balancer" (13 chars) needs a rect at least 140px wide. When in doubt, make boxes wider and leave more space between them. Cramped diagrams are the most common failure mode.\n\n**Special characters are wider**: Chemical formulas (C₆H₁₂O₆), math notation (∑, ∫, √), subscripts/superscripts via <tspan> with dy/baseline-shift, and Unicode symbols all render wider than plain Latin characters. For labels containing formulas or special notation, add 30-50% extra width to your estimate. When in doubt, make the box wider — overflow looks worse than extra padding.\n\n**Spacing**: 60px minimum between boxes, 24px padding inside boxes, 12px between text and edges. Leave 10px gap between arrowheads and box edges. Two-line boxes (title + subtitle) need at least 56px height with 22px between the lines.\n\n**Vertical text placement**: Every `<text>` inside a box needs `dominant-baseline="central"`, with y set to the *centre* of the slot it sits in. Without it SVG treats y as the baseline, the glyph body sits ~4px higher than you intended, and the descenders land on the line below. Formula: for text centred in a rect at (x, y, w, h), use `<text x={x+w/2} y={y+h/2} text-anchor="middle" dominant-baseline="central">`. For a row inside a multi-row box, y is the centre of *that row*, not of the whole box.\n\n**Layout**: Prefer single-direction flows (all top-down or all left-right). Keep diagrams simple — max 4-5 nodes per diagram. The widget is narrow (~680px) so complex layouts break.\n\n**When the prompt itself is over budget**: if the user lists 6+ components ("draw me auth, products, orders, payments, gateway, queue"), don\'t draw all of them in one pass — you\'ll get overlapping boxes and arrows through text, every time. Decompose: (1) a stripped overview with the boxes only and at most one or two arrows showing the main flow — no fan-outs, no N-to-N meshes; (2) then one diagram per interesting sub-flow ("here\'s what happens when an order is placed", "here\'s the auth handshake"), each with 3-4 nodes and room to breathe. Count the nouns before you draw. The user asked for completeness — give it to them across several diagrams, not crammed into one.\n\n**Cycles don\'t get drawn as rings.** If the last stage feeds back into the first (Krebs cycle, event loop, GC mark-and-sweep, TCP retransmit), your instinct is to place the stages around a circle. Don\'t. Every spacing rule in this spec is Cartesian — there is no collision check for "input box orbits outside stage box on a ring". You will get satellite boxes overlapping the stages they feed, labels sitting on the dashed circle, and tangential arrows that point nowhere. The ring is decoration; the loop is conveyed by the return arrow.\n\nBuild a stepper in `imagine_html`. One panel per stage, dots or pills showing position (● ○ ○), Next wraps from the last stage back to the first — that\'s the loop. Each panel owns its inputs and products: an event loop\'s pending callbacks live *inside* the Poll panel, not floating next to a box on a ring. Nothing collides because nothing shares the canvas. Only fall back to a linear SVG (stages in a row, curved `<path>` return arrow) when there\'s one input and one output total and no per-stage detail to show.\n\n**Feedback loops in linear flows:** Don\'t draw a physical arrow traversing the layout (it fights the flow direction and clips edges). Instead:\n- Small `↻` glyph + text near the cycle point: `<text>↻ returns to start</text>`\n- Or restructure the whole diagram as a circle if the cycle IS the point\n\n**Arrows:** A line from A to B must not cross any other box or label. If the direct path crosses something, route around with an L-bend: `<path d="M x1 y1 L x1 ymid L x2 ymid L x2 y2"/>`. Place arrow labels in clear space, not on the midpoint.\n\nKeep all nodes the same height when they have the same content type (e.g. all single-line boxes = 44px, all two-line boxes = 56px).\n\n**Flowchart components** — use these patterns consistently:\n\n*Single-line node* (44px tall): title only. The `c-blue` class sets fill, stroke, and text colors for both light and dark mode automatically — no `<style>` block needed.\n```svg\n<g class="node c-blue" onclick="sendPrompt(\'Tell me more about T-cells\')">\n  <rect x="100" y="20" width="180" height="44" rx="8" stroke-width="0.5"/>\n  <text class="th" x="190" y="42" text-anchor="middle" dominant-baseline="central">T-cells</text>\n</g>\n```\n\n*Two-line node* (56px tall): bold title + muted subtitle.\n```svg\n<g class="node c-blue" onclick="sendPrompt(\'Tell me more about dendritic cells\')">\n  <rect x="100" y="20" width="200" height="56" rx="8" stroke-width="0.5"/>\n  <text class="th" x="200" y="38" text-anchor="middle" dominant-baseline="central">Dendritic cells</text>\n  <text class="ts" x="200" y="56" text-anchor="middle" dominant-baseline="central">Detect foreign antigens</text>\n</g>\n```\n\n*Connector* (no label — meaning is clear from source + target):\n```svg\n<line x1="200" y1="76" x2="200" y2="120" class="arr" marker-end="url(#arrow)"/>\n```\n\n*Neutral node* (gray, for start/end/generic steps): use `class="box"` for auto-themed fill/stroke, and default text classes.\n\nMake all nodes clickable by default — wrap in `<g class="node" onclick="sendPrompt(\'...\')">`. The hover effect is built in.\n\n#### Structural diagram\n\nFor concepts where physical or logical containment matters — things inside other things.\n\n**When to use**: The explanation depends on *where* processes happen. Examples: how a cell works (organelles inside a cell), how a file system works (blocks inside inodes inside partitions), how a building\'s HVAC works (ducts inside floors inside a building), how a CPU cache hierarchy works (L1 inside core, L2 shared).\n\n**Core idea**: Large rounded rects are containers. Smaller rects inside them are regions or sub-structures. Text labels describe what happens in each region. Arrows show flow between regions or from external inputs/outputs.\n\n**Container rules**:\n- Outermost container: large rounded rect, rx=20-24, lightest fill (50 stop), 0.5px stroke (600 stop). Label at top-left inside, 14px bold.\n- Inner regions: medium rounded rects, rx=8-12, next shade fill (100-200 stop). Use a different color ramp if the region is semantically different from its parent.\n- 20px minimum padding inside every container — text and inner regions must not touch the container edges.\n- Max 2-3 nesting levels. Deeper nesting gets unreadable at 680px width.\n\n**Layout**:\n- Place inner regions side by side within the container, with 16px+ gap between them.\n- External inputs (sunlight, water, data, requests) sit outside the container with arrows pointing in.\n- External outputs sit outside with arrows pointing out.\n- Keep external labels short — one word or a short phrase. Details go in the prose between diagrams.\n\n**What goes inside regions**: Text only — the region name (14px bold) and a short description of what happens there (12px). Don\'t put flowchart-style boxes inside regions. Don\'t draw illustrations or icons inside.\n\n**Structural container example** (library branch with two side-by-side regions, an internal labeled arrow, and an external input). ViewBox 700x320, horizontal layout, color classes handle both light and dark mode — no `<style>` block:\n```svg\n<defs>\n  <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">\n    <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>\n  </marker>\n</defs>\n<!-- Outer container -->\n<g class="c-green">\n  <rect x="120" y="30" width="560" height="260" rx="20" stroke-width="0.5"/>\n  <text class="th" x="400" y="62" text-anchor="middle">Library branch</text>\n  <text class="ts" x="400" y="80" text-anchor="middle">Main floor</text>\n</g>\n<!-- Inner: Circulation desk -->\n<g class="c-teal">\n  <rect x="150" y="100" width="220" height="160" rx="12" stroke-width="0.5"/>\n  <text class="th" x="260" y="130" text-anchor="middle">Circulation desk</text>\n  <text class="ts" x="260" y="148" text-anchor="middle">Checkouts, returns</text>\n</g>\n<!-- Inner: Reading room -->\n<g class="c-amber">\n  <rect x="450" y="100" width="210" height="160" rx="12" stroke-width="0.5"/>\n  <text class="th" x="555" y="130" text-anchor="middle">Reading room</text>\n  <text class="ts" x="555" y="148" text-anchor="middle">Seating, reference</text>\n</g>\n<!-- Arrow between inner boxes with label -->\n<text class="ts" x="410" y="175" text-anchor="middle">Books</text>\n<line x1="370" y1="185" x2="448" y2="185" class="arr" marker-end="url(#arrow)"/>\n<!-- External input: New acq. — text vertically aligned with arrow -->\n<text class="ts" x="40" y="185" text-anchor="middle">New acq.</text>\n<line x1="75" y1="185" x2="118" y2="185" class="arr" marker-end="url(#arrow)"/>\n```\n\n**Color in structural diagrams**: Nested regions need distinct ramps — `c-{ramp}` classes resolve to fixed fill/stroke stops, so the same class on parent and child gives identical fills and flattens the hierarchy. Pick a *related* ramp for inner structures (e.g. Green for the library envelope, Teal for the circulation desk inside it) and a *contrasting* ramp for a region that does something functionally different (e.g. Amber for the reading room). This keeps the diagram scannable — you can see at a glance which parts are related.\n\n**Database schemas / ERDs — use mermaid.js, not SVG.** A schema table is a header plus N field rows plus typed columns plus crow\'s-foot connectors. That is a text-layout problem and hand-placing it in SVG fails the same way every time. mermaid.js `erDiagram` does layout, cardinality, and connector routing for free. ERDs only; everything else stays in SVG.\n\n```\nerDiagram\n  USERS ||--o{ POSTS : writes\n  POSTS ||--o{ COMMENTS : has\n  USERS {\n    uuid id PK\n    string email\n    timestamp created_at\n  }\n  POSTS {\n    uuid id PK\n    uuid user_id FK\n    string title\n  }\n```\n\nUse `imagine_html` for ERDs. Import and initialize in a `<script type="module">`. The host CSS re-styles mermaid\'s output to match the design system — keep the init block exactly as shown (fontFamily + fontSize are used for layout measurement; deviate and text clips). After rendering, replace sharp-cornered entity `<path>` elements with rounded `<rect rx="8">` to match the design system, and strip borders from attribute rows (only the outer container and header row keep visible borders — alternating fill colors separate the rows):\n```html\n<style>\n#erd svg.erDiagram .divider path { stroke-opacity: 0.5; }\n#erd svg.erDiagram .row-rect-odd path,\n#erd svg.erDiagram .row-rect-odd rect,\n#erd svg.erDiagram .row-rect-even path,\n#erd svg.erDiagram .row-rect-even rect { stroke: none !important; }\n</style>\n<div id="erd"></div>\n<script type="module">\nimport mermaid from \'https://esm.sh/mermaid@11/dist/mermaid.esm.min.mjs\';\nconst dark = matchMedia(\'(prefers-color-scheme: dark)\').matches;\nawait document.fonts.ready;\nmermaid.initialize({\n  startOnLoad: false,\n  theme: \'base\',\n  fontFamily: \'"Anthropic Sans", sans-serif\',\n  themeVariables: {\n    darkMode: dark,\n    fontSize: \'13px\',\n    fontFamily: \'"Anthropic Sans", sans-serif\',\n    lineColor: dark ? \'#9c9a92\' : \'#73726c\',\n    textColor: dark ? \'#c2c0b6\' : \'#3d3d3a\',\n  },\n});\nconst { svg } = await mermaid.render(\'erd-svg\', `erDiagram\n  USERS ||--o{ POSTS : writes\n  POSTS ||--o{ COMMENTS : has`);\ndocument.getElementById(\'erd\').innerHTML = svg;\n\n// Round only the outermost entity box corners (not internal row stripes)\ndocument.querySelectorAll(\'#erd svg.erDiagram .node\').forEach(node => {\n  const firstPath = node.querySelector(\'path[d]\');\n  if (!firstPath) return;\n  const d = firstPath.getAttribute(\'d\');\n  const nums = d.match(/-?[\\d.]+/g)?.map(Number);\n  if (!nums || nums.length < 8) return;\n  const xs = [nums[0], nums[2], nums[4], nums[6]];\n  const ys = [nums[1], nums[3], nums[5], nums[7]];\n  const x = Math.min(...xs), y = Math.min(...ys);\n  const w = Math.max(...xs) - x, h = Math.max(...ys) - y;\n  const rect = document.createElementNS(\'http://www.w3.org/2000/svg\', \'rect\');\n  rect.setAttribute(\'x\', x); rect.setAttribute(\'y\', y);\n  rect.setAttribute(\'width\', w); rect.setAttribute(\'height\', h);\n  rect.setAttribute(\'rx\', \'8\');\n  for (const a of [\'fill\', \'stroke\', \'stroke-width\', \'class\', \'style\']) {\n    if (firstPath.hasAttribute(a)) rect.setAttribute(a, firstPath.getAttribute(a));\n  }\n  firstPath.replaceWith(rect);\n});\n\n// Strip borders from attribute rows (mermaid v11: .row-rect-odd / .row-rect-even)\ndocument.querySelectorAll(\'#erd svg.erDiagram .row-rect-odd path, #erd svg.erDiagram .row-rect-even path\').forEach(p => {\n  p.setAttribute(\'stroke\', \'none\');\n});\n</script>\n```\n\nWorks identically for `classDiagram` — swap the diagram source; init stays the same.\n\n#### Illustrative diagram\n\nFor building *intuition*. The subject might be physical (an engine, a lung) or completely abstract (attention, recursion, gradient descent) — what matters is that a spatial drawing conveys the mechanism better than labelled boxes would. These are the diagrams that make someone go "oh, *that\'s* what it\'s doing."\n\n**Two flavours, same rules:**\n- **Physical subjects** get drawn as simplified versions of themselves. Cross-sections, cutaways, schematics. A water heater is a tank with a burner underneath. A lung is a branching tree in a cavity. You\'re drawing *the thing*, stylised.\n- **Abstract subjects** get drawn as *spatial metaphors*. You\'re inventing a shape for something that doesn\'t have one — but the shape should make the mechanism obvious. A transformer is a stack of horizontal slabs with a bright thread of attention connecting tokens across layers. A hash function is a funnel scattering items into a row of buckets. The call stack is literally a stack of frames growing and shrinking. Embeddings are dots clustering in space. The metaphor *is* the explanation.\n\nThis is the most ambitious diagram type and the one Claude is best at. Lean into it. Use colour for intensity (a hot attention weight glows amber, a cold one stays gray). Use repetition for scale (many small circles = many parameters).\n\n**Prefer interactive over static.** A static cross-section is a good answer; a cross-section you can *operate* is a great one. The decision rule: if the real-world system has a control, give the diagram that control. A water heater has a thermostat — so give the user a slider that shifts the hot/cold boundary, a toggle that fires the burner and animates convection currents. An LLM has input tokens — let the user click one and watch the attention weights re-fan. A cache has a hit rate — let them drag it and watch latency change. Reach for `imagine_html` with inline SVG first; only fall back to static `imagine_svg` when there\'s genuinely nothing to twiddle.\n\n**When NOT to use**: The user is asking for a *reference*, not an *intuition*. "What are the components of a transformer" wants labelled boxes — that\'s a structural diagram. "Walk me through our CI pipeline" wants sequential steps — that\'s a flowchart. Also skip this when the metaphor would be arbitrary rather than revealing: drawing "the cloud" as a cloud shape or "microservices" as little houses doesn\'t teach anything about how they work. If the drawing doesn\'t make the *mechanism* clearer, don\'t draw it.\n\n**Fidelity ceiling**: These are schematics, not illustrations. Every shape should read at a glance. If a `<path>` needs more than ~6 segments to draw, simplify it. A tank is a rounded rect, not a Bézier portrait of a tank. A flame is three triangles, not a fire. Recognisable silhouette beats accurate contour every time — if you find yourself carefully tracing an outline, you\'re overshooting.\n\n**Core principle**: Draw the mechanism, not a diagram *about* the mechanism. Spatial arrangement carries the meaning; labels annotate. A good illustrative diagram works with the labels removed.\n\n**What changes from flowchart/structural rules**:\n\n- **Shapes are freeform.** Use `<path>`, `<ellipse>`, `<circle>`, `<polygon>`, and curved lines to represent real forms. A water tank is a tall rect with rounded bottom. A heart valve is a pair of curved paths. A circuit trace is a thin polyline. You are not limited to rounded rects.\n- **Layout follows the subject\'s geometry**, not a grid. If the thing is tall and narrow (a water heater, a thermometer), the diagram is tall and narrow. If it\'s wide and flat (a PCB, a geological cross-section), the diagram is wide. Let the subject dictate proportions within the 680px viewBox width.\n- **Color encodes intensity**, not category. For physical subjects: warm ramps (amber, coral, red) = heat/energy/pressure, cool ramps (blue, teal) = cold/calm, gray = inert structure. For abstract subjects: warm = active/high-weight/attended-to, cool or gray = dormant/low-weight/ignored. A user should be able to glance at the diagram and see *where the action is* without reading a single label.\n- **Layering and overlap are encouraged — for shapes.** Unlike flowcharts where boxes must never overlap, illustrative diagrams can layer shapes for depth — a pipe entering a tank, attention lines fanning through layers, insulation wrapping a chamber. Use z-ordering (later in source = on top) deliberately.\n- **Text is the exception — never let a stroke cross it.** The overlap permission is for shapes only. Every label needs 8px of clear air between its baseline/cap-height and the nearest stroke. Don\'t solve this with a background rect — solve it by *placing the text somewhere else*. Labels go in the quiet regions: above the drawing, below it, in the margin with a leader line, or in the gap between two fans of lines. If there is no quiet region, the drawing is too dense — remove something or split into two diagrams.\n- **Small shape-based indicators are allowed** when they communicate physical state. Triangles for flames. Circles for bubbles or particles. Wavy lines for steam or heat radiation. Parallel lines for vibration. These aren\'t decoration — they tell the user what\'s happening physically. Keep them simple: basic SVG primitives, not detailed illustrations.\n- **One gradient per diagram is permitted** — the only exception to the global no-gradients rule — and only to show a *continuous* physical property across a region (temperature stratification in a tank, pressure drop along a pipe, concentration in a solution). It must be a single `<linearGradient>` between exactly two stops from the same colour ramp. No radial gradients, no multi-stop fades, no gradient-as-aesthetic. If two stacked flat-fill rects communicate the same thing, do that instead.\n- **Animation is permitted for interactive HTML versions.** Use CSS `@keyframes` animating only `transform` and `opacity`. Keep loops under ~2s, and wrap every animation in `@media (prefers-reduced-motion: no-preference)` so it\'s opt-out by default. Animations should show how the system *behaves* — convection current, rotation, flow — not just move for the sake of moving. No physics engines or heavy libraries.\n\nAll core rules still apply (viewBox 680px, dark mode mandatory, 14/12px text, pre-built classes, arrow marker, clickable nodes).\n\n**Label placement**:\n- Place labels *outside* the drawn object when possible, with a thin leader line (0.5px dashed, `var(--t)` stroke) pointing to the relevant part. This keeps the illustration uncluttered.\n- For large internal zones (like temperature regions in a tank), labels can sit inside if there\'s ample clear space — minimum 20px from any edge.\n- External labels sit in the margin area or above/below the object. **Pick one side for labels and put them all there** — at 680px wide you don\'t have room for a drawing *and* label columns on both sides. Reserve at least 140px of horizontal margin on the label side. Labels on the left are the ones that clip: `text-anchor="end"` extends leftward from x, and with multi-line callouts it\'s very easy to blow past x=0 without noticing. Default to right-side labels with `text-anchor="start"` unless the subject\'s geometry forces otherwise. Use `class="ts"` (12px) for callouts, `class="th"` (14px medium) for major component names.\n\n**Composition approach**:\n1. Start with the main object\'s silhouette — the largest shape, centered in the viewBox.\n2. Add internal structure: chambers, pipes, membranes, mechanical parts.\n3. Add external connections: pipes entering/exiting, arrows showing flow direction, labels for inputs and outputs.\n4. Add state indicators last: color fills showing temperature/pressure/concentration, small animated elements showing movement or energy.\n5. Leave generous whitespace around the object for labels — don\'t crowd annotations against the viewBox edges.\n\n**Static vs interactive**: Static cutaways and cross-sections work best as pure `imagine_svg`. If the diagram benefits from controls — a slider that changes a temperature zone, buttons toggling between operating states, live readouts — use `imagine_html` with inline SVG for the drawing and HTML controls around it.\n\n**Illustrative diagram example** — interactive water heater cross-section with vivid physical-realism colors, animated convection currents, and controls. Uses `imagine_html` with inline SVG: a thermostat slider shifts the hot/cold gradient boundary, a heating toggle animates flames on/off and transitions convection to paused. viewBox is 680x560; tank occupies x=180..440, leaving 140px+ of right margin for labels. Smooth convection paths use `stroke-dasharray:5 5` at ~1.6s for a gentle flow feel. A warm-glow overlay on the hot zone pulses subtly when heating is on. Flame shapes use warm gradient fills and clean opacity transitions. Labels sit along the right margin with leader lines.\n```html\n<style>\n  @keyframes conv { to { stroke-dashoffset: -20; } }\n  @keyframes flicker { 0%,100%{opacity:1} 50%{opacity:.82} }\n  @keyframes glow { 0%,100%{opacity:.3} 50%{opacity:.6} }\n  .conv { stroke-dasharray:5 5; animation: conv var(--dur,1.6s) linear infinite; transition: opacity .5s; }\n  .conv.off { opacity:0; animation-play-state:paused; }\n  #flames path { transition: opacity .5s; }\n  #flames.off path { opacity:0; animation:none; }\n  #flames path:nth-child(odd)  { animation: flicker .6s ease-in-out infinite; }\n  #flames path:nth-child(even) { animation: flicker .8s ease-in-out infinite .15s; }\n  #warm-glow { animation: glow 3s ease-in-out infinite; transition: opacity .5s; }\n  #warm-glow.off { opacity:0; animation:none; }\n  .toggle-track { position:relative;width:32px;height:18px;background:var(--color-border-secondary);border-radius:9px;transition:background .2s;display:inline-block; }\n  .toggle-track:has(input:checked) { background:var(--color-text-info); }\n  #heat-toggle:checked + span { transform:translateX(14px); }\n</style>\n<svg width="100%" viewBox="0 0 680 560">\n  <defs>\n    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker>\n    <linearGradient id="tg" x1="0" y1="0" x2="0" y2="1">\n      <stop id="gh" offset="40%" stop-color="#E8593C" stop-opacity="0.45"/>\n      <stop id="gc" offset="40%" stop-color="#3B8BD4" stop-opacity="0.4"/>\n    </linearGradient>\n    <linearGradient id="fg1" x1="0" y1="1" x2="0" y2="0"><stop offset="0%" stop-color="#E85D24"/><stop offset="60%" stop-color="#F2A623"/><stop offset="100%" stop-color="#FCDE5A"/></linearGradient>\n    <linearGradient id="fg2" x1="0" y1="1" x2="0" y2="0"><stop offset="0%" stop-color="#D14520"/><stop offset="50%" stop-color="#EF8B2C"/><stop offset="100%" stop-color="#F9CB42"/></linearGradient>\n    <linearGradient id="pipe-h" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#D05538" stop-opacity=".25"/><stop offset="100%" stop-color="#D05538" stop-opacity=".08"/></linearGradient>\n    <linearGradient id="pipe-c" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#3B8BD4" stop-opacity=".25"/><stop offset="100%" stop-color="#3B8BD4" stop-opacity=".08"/></linearGradient>\n    <clipPath id="tc"><rect x="180" y="55" width="260" height="390" rx="14"/></clipPath>\n  </defs>\n  <!-- Tank fill -->\n  <g clip-path="url(#tc)"><rect x="180" y="55" width="260" height="390" fill="url(#tg)"/></g>\n  <!-- Warm glow overlay (pulses when heating) -->\n  <g clip-path="url(#tc)"><rect id="warm-glow" x="180" y="55" width="260" height="160" fill="#E8593C" opacity=".3"/></g>\n  <!-- Tank shell (double stroke for solidity) -->\n  <rect x="180" y="55" width="260" height="390" rx="14" fill="none" stroke="var(--t)" stroke-width="2.5" opacity=".25"/>\n  <rect x="180" y="55" width="260" height="390" rx="14" fill="none" stroke="var(--t)" stroke-width="1"/>\n  <!-- Hot pipe out (top right) -->\n  <rect x="370" y="14" width="16" height="50" rx="4" fill="url(#pipe-h)"/>\n  <path d="M378 14V55" stroke="var(--t)" stroke-width="3" stroke-linecap="round" fill="none"/>\n  <!-- Cold pipe in + dip tube (top left) -->\n  <rect x="234" y="14" width="16" height="50" rx="4" fill="url(#pipe-c)"/>\n  <path d="M242 14V55" stroke="var(--t)" stroke-width="3" stroke-linecap="round" fill="none"/>\n  <path d="M242 55V395" stroke="var(--t)" stroke-width="2.5" stroke-linecap="round" fill="none" opacity=".5"/>\n  <!-- Convection currents (curved paths at different speeds) -->\n  <path class="conv" style="--dur:1.6s" fill="none" stroke="#D05538" stroke-width="1" opacity=".5" d="M350 380C355 320,365 240,358 140Q355 110,340 100"/>\n  <path class="conv" style="--dur:2.1s" fill="none" stroke="#C04828" stroke-width=".8" opacity=".35" d="M300 390C308 340,320 260,315 170Q312 130,298 115"/>\n  <path class="conv" style="--dur:2.6s" fill="none" stroke="#B05535" stroke-width=".7" opacity=".3" d="M380 370C382 310,388 230,382 150Q378 120,365 110"/>\n  <!-- Burner bar -->\n  <rect x="188" y="454" width="244" height="5" rx="2" fill="var(--t)" opacity=".6"/>\n  <rect x="220" y="462" width="180" height="6" rx="3" fill="var(--t)" opacity=".3"/>\n  <!-- Flames (gradient-filled organic shapes) -->\n  <g id="flames">\n    <path d="M240,454Q248,430 252,438Q256,424 260,454Z" fill="url(#fg1)"/>\n    <path d="M278,454Q285,426 290,434Q295,418 300,454Z" fill="url(#fg2)"/>\n    <path d="M320,454Q328,428 333,436Q338,420 342,454Z" fill="url(#fg1)"/>\n    <path d="M360,454Q367,430 371,438Q375,422 380,454Z" fill="url(#fg2)"/>\n    <path d="M398,454Q404,434 408,440Q412,428 416,454Z" fill="url(#fg1)"/>\n  </g>\n  <!-- Labels (right margin) -->\n  <g class="node" onclick="sendPrompt(\'How does hot water exit the tank?\')">\n    <line class="leader" x1="386" y1="34" x2="468" y2="70"/><circle cx="386" cy="34" r="2" fill="var(--t)"/>\n    <text class="ts" x="474" y="74">Hot water outlet</text></g>\n  <g class="node" onclick="sendPrompt(\'How does the cold water inlet work?\')">\n    <line class="leader" x1="250" y1="34" x2="468" y2="140"/><circle cx="250" cy="34" r="2" fill="var(--t)"/>\n    <text class="ts" x="474" y="144">Cold water inlet</text></g>\n  <g class="node" onclick="sendPrompt(\'What does the dip tube do?\')">\n    <line class="leader" x1="250" y1="260" x2="468" y2="220"/><circle cx="250" cy="260" r="2" fill="var(--t)"/>\n    <text class="ts" x="474" y="224">Dip tube</text></g>\n  <g class="node" onclick="sendPrompt(\'What does the thermostat control?\')">\n    <line class="leader" x1="440" y1="250" x2="468" y2="300"/><circle cx="440" cy="250" r="2" fill="var(--t)"/>\n    <text class="ts" x="474" y="304">Thermostat</text></g>\n  <g class="node" onclick="sendPrompt(\'What material is the tank made of?\')">\n    <line class="leader" x1="440" y1="380" x2="468" y2="380"/><circle cx="440" cy="380" r="2" fill="var(--t)"/>\n    <text class="ts" x="474" y="384">Tank wall</text></g>\n  <g class="node" onclick="sendPrompt(\'How does the gas burner heat water?\')">\n    <line class="leader" x1="432" y1="454" x2="468" y2="454"/><circle cx="432" cy="454" r="2" fill="var(--t)"/>\n    <text class="ts" x="474" y="458">Heating element</text></g>\n</svg>\n<div style="display:flex;align-items:center;gap:16px;margin:12px 0 0;font-size:13px;color:var(--color-text-secondary)">\n  <label style="display:flex;align-items:center;gap:6px;cursor:pointer;user-select:none">\n    <span class="toggle-track">\n      <input type="checkbox" id="heat-toggle" checked onchange="toggleHeat(this.checked)" style="position:absolute;opacity:0;width:100%;height:100%;cursor:pointer;margin:0">\n      <span style="position:absolute;top:2px;left:2px;width:14px;height:14px;background:#fff;border-radius:50%;transition:transform .2s;pointer-events:none"></span>\n    </span>\n    Heating\n  </label>\n  <span>Thermostat</span>\n  <input type="range" id="temp-slider" min="10" max="90" value="40" style="flex:1" oninput="setTemp(this.value)">\n  <span id="temp-label" style="min-width:36px;text-align:right">40%</span>\n</div>\n<script>\nfunction setTemp(v) {\n  document.getElementById(\'gh\').setAttribute(\'offset\', v+\'%\');\n  document.getElementById(\'gc\').setAttribute(\'offset\', v+\'%\');\n  document.getElementById(\'temp-label\').textContent = v+\'%\';\n}\nfunction toggleHeat(on) {\n  document.getElementById(\'flames\').classList.toggle(\'off\', !on);\n  document.getElementById(\'warm-glow\').classList.toggle(\'off\', !on);\n  document.querySelectorAll(\'.conv\').forEach(p => p.classList.toggle(\'off\', !on));\n}\n</script>\n```\n\n**Illustrative example — abstract subject** (attention in a transformer). Same rules, no physical object. A row of tokens at the bottom, one query token highlighted, weight-scaled lines fanning to every other token. Caption sits below the fan — clear of every stroke — not inside it.\n```svg\n<rect class="c-purple" x="60" y="40"  width="560" height="26" rx="6" stroke-width="0.5"/>\n<rect class="c-purple" x="60" y="80"  width="560" height="26" rx="6" stroke-width="0.5"/>\n<rect class="c-purple" x="60" y="120" width="560" height="26" rx="6" stroke-width="0.5"/>\n<text class="ts" x="72" y="57" >Layer 3</text>\n<text class="ts" x="72" y="97" >Layer 2</text>\n<text class="ts" x="72" y="137">Layer 1</text>\n\n<line stroke="#EF9F27" stroke-linecap="round" x1="340" y1="230" x2="116" y2="146" stroke-width="1"   opacity="0.25"/>\n<line stroke="#EF9F27" stroke-linecap="round" x1="340" y1="230" x2="228" y2="146" stroke-width="1.5" opacity="0.4"/>\n<line stroke="#EF9F27" stroke-linecap="round" x1="340" y1="230" x2="340" y2="146" stroke-width="4"   opacity="1.0"/>\n<line stroke="#EF9F27" stroke-linecap="round" x1="340" y1="230" x2="452" y2="146" stroke-width="2.5" opacity="0.7"/>\n<line stroke="#EF9F27" stroke-linecap="round" x1="340" y1="230" x2="564" y2="146" stroke-width="1"   opacity="0.2"/>\n\n<g class="node" onclick="sendPrompt(\'What do the attention weights mean?\')">\n  <rect class="c-gray"  x="80"  y="230" width="72" height="36" rx="6" stroke-width="0.5"/>\n  <rect class="c-gray"  x="192" y="230" width="72" height="36" rx="6" stroke-width="0.5"/>\n  <rect class="c-amber" x="304" y="230" width="72" height="36" rx="6" stroke-width="1"/>\n  <rect class="c-gray"  x="416" y="230" width="72" height="36" rx="6" stroke-width="0.5"/>\n  <rect class="c-gray"  x="528" y="230" width="72" height="36" rx="6" stroke-width="0.5"/>\n  <text class="ts" x="116" y="252" text-anchor="middle">the</text>\n  <text class="ts" x="228" y="252" text-anchor="middle">cat</text>\n  <text class="th" x="340" y="252" text-anchor="middle">sat</text>\n  <text class="ts" x="452" y="252" text-anchor="middle">on</text>\n  <text class="ts" x="564" y="252" text-anchor="middle">the</text>\n</g>\n\n<text class="ts" x="340" y="300" text-anchor="middle">Line thickness = attention weight from "sat" to each token</text>\n```\n\nNote what\'s *not* here: no boxes labelled "multi-head attention", no arrows labelled "Q/K/V". Those belong in the structural diagram. This one is about the *feeling* of attention — one token looking at every other token with varying intensity.\n\nThese are starting points, not ceilings. For the water heater: add a thermostat slider, animate the convection current, toggle heating vs standby. For the attention diagram: let the user click any token to become the query, scrub through layers, animate the weights settling. The goal is always to *show* how the thing works, not just *label* it.\n\n\n## UI components\n\n### Aesthetic\nFlat, clean, white surfaces. Minimal 0.5px borders. Generous whitespace. No gradients, no shadows (except functional focus rings). Everything should feel native to claude.ai — like it belongs on the page, not embedded from somewhere else.\n\n### Tokens\n- Borders: always `0.5px solid var(--color-border-tertiary)` (or `-secondary` for emphasis)\n- Corner radius: `var(--border-radius-md)` for most elements, `var(--border-radius-lg)` for cards\n- Cards: white bg (`var(--color-background-primary)`), 0.5px border, radius-lg, padding 1rem 1.25rem\n- Form elements (input, select, textarea, button, range slider) are pre-styled — write bare tags. Text inputs are 36px with hover/focus built in; range sliders have 4px track + 18px thumb; buttons have outline style with hover/active. Only add inline styles to override (e.g., different width).\n- Buttons: pre-styled with transparent bg, 0.5px border-secondary, hover bg-secondary, active scale(0.98). If it triggers sendPrompt, append a ↗ arrow.\n- **Round every displayed number.** JS float math leaks artifacts — `0.1 + 0.2` gives `0.30000000000000004`, `7 * 1.1` gives `7.700000000000001`. Any number that reaches the screen (slider readouts, stat card values, axis labels, data-point labels, tooltips, computed totals) must go through `Math.round()`, `.toFixed(n)`, or `Intl.NumberFormat`. Pick the precision that makes sense for the context — integers for counts, 1–2 decimals for percentages, `toLocaleString()` for currency. For range sliders, also set `step="1"` (or step="0.1" etc.) so the input itself emits round values.\n- Spacing: use rem for vertical rhythm (1rem, 1.5rem, 2rem), px for component-internal gaps (8px, 12px, 16px)\n- Box-shadows: none, except `box-shadow: 0 0 0 Npx` focus rings on inputs\n\n### Metric cards\nFor summary numbers (revenue, count, percentage) — surface card with muted 13px label above, 24px/500 number below. `background: var(--color-background-secondary)`, no border, `border-radius: var(--border-radius-md)`, padding 1rem. Use in grids of 2-4 with `gap: 12px`. Distinct from raised cards (which have white bg + border).\n\n### Layout\n- Editorial (explanatory content): no card wrapper, prose flows naturally\n- Card (bounded objects like a contact record, receipt): single raised card wraps the whole thing\n- Don\'t put tables here — output them as markdown in your response text\n\n**Grid overflow:** `grid-template-columns: 1fr` has `min-width: auto` by default — children with large min-content push the column past the container. Use `minmax(0, 1fr)` to clamp.\n\n**Table overflow:** Tables with many columns auto-expand past `width: 100%` if cell contents exceed it. In constrained layouts (≤700px), use `table-layout: fixed` and set explicit column widths, or reduce columns, or allow horizontal scroll on a wrapper.\n\n### Mockup presentation\nContained mockups — mobile screens, chat threads, single cards, modals, small UI components — should sit on a background surface (`var(--color-background-secondary)` container with `border-radius: var(--border-radius-lg)` and padding, or a device frame) so they don\'t float naked on the widget canvas. Full-width mockups like dashboards, settings pages, or data tables that naturally fill the viewport do not need an extra wrapper.\n\n### 1. Interactive explainer — learn how something works\n*"Explain how compound interest works" / "Teach me about sorting algorithms"*\n\nUse `imagine_html` for the interactive controls — sliders, buttons, live state displays, charts. Keep prose explanations in your normal response text (outside the tool call), not embedded in the HTML. No card wrapper. Whitespace is the container.\n\n```html\n<div style="display: flex; align-items: center; gap: 12px; margin: 0 0 1.5rem;">\n  <label style="font-size: 14px; color: var(--color-text-secondary);">Years</label>\n  <input type="range" min="1" max="40" value="20" id="years" style="flex: 1;" />\n  <span style="font-size: 14px; font-weight: 500; min-width: 24px;" id="years-out">20</span>\n</div>\n\n<div style="display: flex; align-items: baseline; gap: 8px; margin: 0 0 1.5rem;">\n  <span style="font-size: 14px; color: var(--color-text-secondary);">£1,000 →</span>\n  <span style="font-size: 24px; font-weight: 500;" id="result">£3,870</span>\n</div>\n\n<div style="margin: 2rem 0; position: relative; height: 240px;">\n  <canvas id="chart"></canvas>\n</div>\n```\n\nUse `sendPrompt()` to let users ask follow-ups: `sendPrompt(\'What if I increase the rate to 10%?\')`\n\n### 2. Compare options — decision making\n*"Compare pricing and features of these products" / "Help me choose between React and Vue"*\n\nUse `imagine_html`. Side-by-side card grid for options. Highlight differences with semantic colors. Interactive elements for filtering or weighting.\n\n- Use `repeat(auto-fit, minmax(160px, 1fr))` for responsive columns\n- Each option in a card. Use badges for key differentiators.\n- Add `sendPrompt()` buttons: `sendPrompt(\'Tell me more about the Pro plan\')`\n- Don\'t put comparison tables inside this tool — output them as regular markdown tables in your response text instead. The tool is for the visual card grid only.\n- When one option is recommended or "most popular", accent its card with `border: 2px solid var(--color-border-info)` only (2px is deliberate — the only exception to the 0.5px rule, used to accent featured items) — keep the same background and border as the other cards. Add a small badge (e.g. "Most popular") above or inside the card header using `background: var(--color-background-info); color: var(--color-text-info); font-size: 12px; padding: 4px 12px; border-radius: var(--border-radius-md)`.\n\n### 3. Data record — bounded UI object\n*"Show me a Salesforce contact card" / "Create a receipt for this order"*\n\nUse `imagine_html`. Wrap the entire thing in a single raised card. All content is sans-serif since it\'s pure UI. Use an avatar/initials circle for people (see example below).\n\n```html\n<div style="background: var(--color-background-primary); border-radius: var(--border-radius-lg); border: 0.5px solid var(--color-border-tertiary); padding: 1rem 1.25rem;">\n  <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 16px;">\n    <div style="width: 44px; height: 44px; border-radius: 50%; background: var(--color-background-info); display: flex; align-items: center; justify-content: center; font-weight: 500; font-size: 14px; color: var(--color-text-info);">MR</div>\n    <div>\n      <p style="font-weight: 500; font-size: 15px; margin: 0;">Maya Rodriguez</p>\n      <p style="font-size: 13px; color: var(--color-text-secondary); margin: 0;">VP of Engineering</p>\n    </div>\n  </div>\n  <div style="border-top: 0.5px solid var(--color-border-tertiary); padding-top: 12px;">\n    <table style="width: 100%; font-size: 13px;">\n      <tr><td style="color: var(--color-text-secondary); padding: 4px 0;">Email</td><td style="text-align: right; padding: 4px 0; color: var(--color-text-info);">m.rodriguez@acme.com</td></tr>\n      <tr><td style="color: var(--color-text-secondary); padding: 4px 0;">Phone</td><td style="text-align: right; padding: 4px 0;">+1 (415) 555-0172</td></tr>\n    </table>\n  </div>\n</div>\n```\n\n\n## Art and illustration\n*"Draw me a sunset" / "Create a geometric pattern"*\n\nUse `imagine_svg`. Same technical rules (viewBox, safe area) but the aesthetic is different:\n- Fill the canvas — art should feel rich, not sparse\n- Bold colors: mix `--color-text-*` categories for variety (info blue, success green, warning amber)\n- Art is the one place custom `<style>` color blocks are fine — freestyle colors, `prefers-color-scheme` for dark mode variants if you want them\n- Layer overlapping opaque shapes for depth\n- Organic forms with `<path>` curves, `<ellipse>`, `<circle>`\n- Texture via repetition (parallel lines, dots, hatching) not raster effects\n- Geometric patterns with `<g transform="rotate()">` for radial symmetry\n', 'uuid': 'af7a723e-fcee-4842-b548-d17ca9e4e0d8'}

{'type': 'text', 'text': "Content rendered and shown to the user. Please do not duplicate the shown content in text because it's already visually represented.", 'uuid': '9c9d7f66-45a5-4e79-92bc-2243b5cafc16'} {'type': 'text', 'text': '[This tool call rendered an interactive widget in the chat. The user can already see the result — do not repeat it in text or with another visualization tool.]', 'uuid': 'daa5b268-11a1-4215-8d8d-bc06bbc8d602'}
Now paste this into OpenCode to replace your current `frontend/src/App.jsx` and `frontend/index.html`:

---

**OpenCode prompt:**
```
Replace frontend/src/App.jsx with the full UI I'll paste below. 
Also update frontend/index.html to NOT use CDN scripts in head — 
instead make it a plain Vite HTML that just imports App.jsx as module.
The App.jsx should replicate this exact layout:
- Topbar: logo + version badge + status indicators (ollama, agents, latency, mem) — poll GET /api/health every 5s
- Left panel (260px): Agent swarm list — each agent card shows avatar, name, role, status badge, quote — click to cycle status — Consensus meter at bottom animating
- Center: Dark canvas with rotating 3D knowledge graph (D3 force simulation or canvas dots+edges on a sphere), query input + depth select + INITIATE button at bottom — POST to /api/research
- Right panel (280px): Live OSINT mini-globe (canvas), Active Tasks list from GET /api/sessions polling every 3s

Color scheme:
- Background: #07080f
- Accent teal: #00d4b4
- Violet: #8b5cf6
- Amber: #f59e0b  
- Rose: #f43f5e
- Cyan: #22d3ee
- All borders: #1e2535
- Font: Courier New monospace throughout

Agent avatars: colored square badges (teal/violet/amber/rose/cyan per agent)
Status badges: Speaking=green, Thinking=violet, Writing=amber, Idle=gray
Consensus bar: gradient rose→violet→teal, animates slowly

No comments. No docstrings. Code only.
```

The interactive preview above shows exactly what it'll look like — rotating globe, agent swarm, live consensus meter, all clickable. Click the agent cards to cycle their statuses.

---

### 🧑 You

but when i run it it is using my 100 cpu so its is not doing research .so provide me any solution for better usage

---

### 🤖 Claude

Your CPU is maxing out because the **rotating 3D globe animation** is running a canvas render loop at 60fps constantly — even when no research is happening. That's the main culprit, not the research engine itself.

---

## Fix 1 — Stop the animation (immediate, in OpenCode)

```
In frontend/src/App.jsx:
- Remove the canvas globe animation entirely
- Replace center panel with a simple static ASCII/text knowledge graph using D3 force (static, no animation loop)
- Only animate when research status = "running"
- Add requestAnimationFrame throttle: max 10fps not 60fps

No comments. Code only.
```

---

## Fix 2 — Throttle Ollama CPU usage (bigger impact)

The real research CPU hog is Ollama running `mistral:7b` on your CPU. Fix it:

```bash
# Limit Ollama CPU threads in your .env
```

Add this to your `.env`:
```bash
OLLAMA_NUM_THREADS=2
OLLAMA_MAX_LOADED_MODELS=1
```

And restart Ollama:
```bash
OLLAMA_NUM_THREADS=2 ollama serve
```

---

## Fix 3 — Switch to lighter models for research

Edit `.env`:
```bash
# Change this:
FAST_MODEL=llama3.2:3b
SMART_MODEL=mistral:7b-instruct

# To this:
FAST_MODEL=qwen2.5:3b
SMART_MODEL=qwen2.5:3b   # same model for both, no context switching
```

Using one model instead of two means Ollama loads it once and keeps it in RAM — no constant loading/unloading which spikes CPU.

---

## Fix 4 — Limit concurrent operations in research engine

Paste in OpenCode:
```
In backend/core/research_engine.py:
- Add asyncio.Semaphore(1) — process only 1 sub-question at a time
- Add await asyncio.sleep(0.5) between each LLM call
- Reduce max search results to 2 per sub-question
- For depth "quick" and "standard" limit sub-questions to max 3

No comments. Code only.
```

---

## Fix 5 — Use quick depth always for testing

In the UI select **Quick (3 questions)** not Deep — Deep spawns 8 parallel search+scrape+summarize chains which all hammer CPU simultaneously.

---

## Priority order

| Fix | Impact | Time |
|---|---|---|
| Stop globe animation | High (frees ~30% CPU) | 2 min |
| `OLLAMA_NUM_THREADS=2` | High (caps CPU cores used) | 30 sec |
| Switch to single model | Medium | 1 min |
| Semaphore in engine | Medium | 5 min |
| Use Quick depth | High (immediate) | 0 |

Do Fix 2 and the depth change first — those alone will drop you from 100% to ~60-70% CPU which is manageable for a research task on your ProBook.

---

### 🧑 You

i will check it tomorrow now i will push it in github

---

### 🤖 Claude

Good call. Here's the push:

```bash
cd /home/sunny77/deepresearch

# Create .gitignore first
cat > .gitignore << 'EOF'
__pycache__/
*.pyc
*.pyo
.env
chroma_db/
omniresearch.db
deepresearch.db
node_modules/
frontend/dist/
*.gguf
.DS_Store
EOF

# Init and push
git add .
git commit -m "feat: OmniResearch v1 - local multi-agent research platform"
git branch -M main
git remote add origin https://github.com/pshreyas77/omniresearch.git
git push -u origin main
```

---

**Before pushing**, create the repo on GitHub first:
1. Go to github.com/new
2. Name it `omniresearch`
3. **Don't** add README or .gitignore (you already have one)
4. Copy the repo URL and replace in the command above

---

One important thing — your `.env` has Ollama URLs and model names, nothing secret, but good habit to never push it. The `.gitignore` above excludes it. Push a `.env.example` instead which is already in your project.

Good luck tomorrow with the CPU fixes. 🚀

---

### 🧑 You

https://github.com/pshreyas77/omniresearch.git

---

### 🤖 Claude

```bash
cd /home/sunny77/deepresearch
git remote add origin https://github.com/pshreyas77/omniresearch.git
git push -u origin main
```

But I can't run that for you — I don't have access to your terminal.

Run these commands yourself:

```bash
cd /home/sunny77/deepresearch

# Check if remote already added
git remote -v

# If not, add it
git remote add origin https://github.com/pshreyas77/omniresearch.git

# Push
git branch -M main
git push -u origin main
```

GitHub will ask for your **username + password**. Use a **Personal Access Token** not your password:

1. Go to github.com → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token → check `repo` scope
3. Copy token → paste as password when git asks

---

After push, your repo will be live at:
```
https://github.com/pshreyas77/omniresearch
```

Let me know if you hit any auth errors.

---

### 🧑 You

Fix 1 — Stop the animation (immediate, in OpenCode)

```
In frontend/src/App.jsx:
- Remove the canvas globe animation entirely
- Replace center panel with a simple static ASCII/text knowledge graph using D3 force (static, no animation loop)
- Only animate when research status = "running"
- Add requestAnimationFrame throttle: max 10fps not 60fps

No comments. Code only.
```

Fix 2 — Throttle Ollama CPU usage (bigger impact)
The real research CPU hog is Ollama running `mistral:7b` on your CPU. Fix it:
bash

```bash
# Limit Ollama CPU threads in your .env
```

Add this to your `.env`:
bash

```bash
OLLAMA_NUM_THREADS=2
OLLAMA_MAX_LOADED_MODELS=1
```

And restart Ollama:
bash

```bash
OLLAMA_NUM_THREADS=2 ollama serve
```

Fix 3 — Switch to lighter models for research
Edit `.env`:
bash

```bash
# Change this:
FAST_MODEL=llama3.2:3b
SMART_MODEL=mistral:7b-instruct

# To this:
FAST_MODEL=qwen2.5:3b
SMART_MODEL=qwen2.5:3b   # same model for both, no context switching
```

Using one model instead of two means Ollama loads it once and keeps it in RAM — no constant loading/unloading which spikes CPU.

---

## Fix 4 — Limit concurrent operations in research engine

Paste in OpenCode:
```
In backend/core/research_engine.py:
- Add asyncio.Semaphore(1) — process only 1 sub-question at a time
- Add await asyncio.sleep(0.5) between each LLM call
- Reduce max search results to 2 per sub-question
- For depth "quick" and "standard" limit sub-questions to max 3

No comments. Code only.
```

Fix 5 — Use quick depth always for testing
In the UI select Quick (3 questions) not Deep — Deep spawns 8 parallel search+scrape+summarize chains which all hammer CPU simultaneously.
Priority order
FixImpactTimeStop globe animationHigh (frees ~30% CPU)2 min`OLLAMA_NUM_THREADS=2`High (caps CPU cores used)30 secSwitch to single modelMedium1 minSemaphore in engineMedium5 minUse Quick depthHigh (immediate)0
Do Fix 2 and the depth change first — those alone will drop you from 100% to ~60-70% CPU which is manageable for a research task on your ProBook.  instead of this use any small model

---

### 🤖 Claude

For your ProBook with 8GB RAM, best small model for research:

## Best option: `qwen2.5:0.5b`

```bash
ollama pull qwen2.5:0.5b
```

- Only ~400MB RAM
- Runs on 1-2 CPU cores
- Fast enough for summarization tasks
- Won't kill your system

---

## Update .env

```bash
FAST_MODEL=qwen2.5:0.5b
SMART_MODEL=qwen2.5:0.5b
OLLAMA_NUM_THREADS=2
OLLAMA_MAX_LOADED_MODELS=1
```

---

## OpenCode prompt (all fixes combined)

```
Apply these changes:

1. In .env replace model lines with:
FAST_MODEL=qwen2.5:0.5b
SMART_MODEL=qwen2.5:0.5b
OLLAMA_NUM_THREADS=2
OLLAMA_MAX_LOADED_MODELS=1

2. In backend/core/research_engine.py:
- Add semaphore = asyncio.Semaphore(1) at top of research()
- Wrap each sub-question block with: async with semaphore:
- Add await asyncio.sleep(0.3) after each LLM call
- Cap sub-questions: quick=2, standard=3, deep=5
- Max search results per sub-question = 2

3. In frontend/src/App.jsx:
- Remove canvas globe and all requestAnimationFrame loops entirely
- Replace center panel background with static SVG hex grid pattern (CSS only, no JS)
- Show a simple text-based node list instead of 3D globe
- Only show a CSS spinner animation when status = "running"

No comments. No docstrings. Code only.
```

---

## Model comparison for your system

| Model | RAM | Speed | Research quality |
|---|---|---|---|
| qwen2.5:0.5b | 400MB | Very fast | Acceptable |
| qwen2.5:1.5b | 1GB | Fast | Good |
| qwen2.5:3b | 2GB | Medium | Better |
| mistral:7b | 5GB | Slow | Best but kills CPU |

Start with `qwen2.5:1.5b` — it's the sweet spot. Fast enough to not freeze your system, smart enough to write coherent research summaries.

```bash
ollama pull qwen2.5:1.5b
```

---

### 🧑 You

still not loading in localhost:3000

---

### 🤖 Claude

Run this and paste the output:

```bash
cd /home/sunny77/deepresearch/frontend
npm run dev
```

And this in a second terminal:

```bash
curl http://localhost:3000
```

Also check:

```bash
# See if port 3000 is actually being used
ss -tlnp | grep 3000

# Check if vite config exists
cat /home/sunny77/deepresearch/frontend/vite.config.js
```

Paste whatever output you get — I need to see the actual error before guessing a fix.

---

### 🧑 You

still not loading

---

### 🤖 Claude

Paste the output of these exact commands one by one:

```bash
# 1. Check if frontend process is running
ss -tlnp | grep 3000
```

```bash
# 2. Check npm run dev output
cd /home/sunny77/deepresearch/frontend && npm run dev 2>&1 | head -30
```

```bash
# 3. Check if App.jsx exists and has content
wc -l /home/sunny77/deepresearch/frontend/src/App.jsx
```

```bash
# 4. Check vite config
cat /home/sunny77/deepresearch/frontend/vite.config.js
```

```bash
# 5. Check package.json
cat /home/sunny77/deepresearch/frontend/package.json
```

Without seeing the actual error output I'm just guessing. Paste what you get from these 5 commands and I'll give you the exact fix.

---
