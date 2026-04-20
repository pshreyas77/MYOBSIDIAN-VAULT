---
title: "OmniResearch Local Intelligence Platform"
date: 2026-03-17
tags:
  - python
  - sql
  - machine-learning
  - llm-ai
  - data-analysis
  - linux
  - obsidian
  - history
  - stock-market
  - osint
  - research
  - projects
  - creative
  - finance
  - web-dev
  - game-design
source: qwen-export
model: qwen3.5-plus
---

# OmniResearch Local Intelligence Platform

**Date:** 2026-03-17  
**Model:** `qwen3.5-plus`  
**Topics:** [[Python]] · [[SQL]] · [[Machine-Learning]] · [[LLM-AI]] · [[Data-Analysis]] · [[Linux]] · [[Obsidian]] · [[History]] · [[Stock-Market]] · [[OSINT]] · [[Research]] · [[Projects]] · [[Creative]] · [[Finance]] · [[Web-Dev]] · [[Game-Design]]

---

### 🧑 You

Based on my analysis of:

    Local Deep Researcher (LangGraph-based, Ollama integration, research loops)
    GPT Researcher (Web UI, multi-format reports, deep research modes)
    MiroFish (multi-agent simulation, knowledge graphs, prediction engine)
    Shadowbroker (OSINT aggregation, real-time data, visualization)

Here's your complete OpenCode prompt:
🎯 OpenCode Prompt: Build "OmniResearch" - Ultimate Local Research Engine
Markdown
Copy
Code Preview

# Project: OmniResearch - Local-First Deep Research & Intelligence Platform

## Overview
Build a comprehensive, open-source research platform that runs entirely locally (no cloud dependencies) combining deep research automation, multi-agent simulation, and OSINT aggregation. It should surpass existing tools (GPT Researcher, Local Deep Researcher, Perplexity) in capabilities while remaining lightweight enough for 8GB RAM systems.

## Core Architecture Requirements

### 1. Tech Stack (Local-First)
- **Backend**: Python 3.10+ with FastAPI
- **Frontend**: React/Vue.js with WebGL visualization (Three.js or D3)
- **LLM Engine**: Ollama integration (primary), optional LMStudio
- **Database**: SQLite (default) or ChromaDB for vector storage
- **Task Queue**: Celery with Redis (optional) or asyncio for simplicity
- **Deployment**: Docker Compose one-liner setup

### 2. Key Features to Implement

#### A. Deep Research Engine (GPT Researcher + Local Deep Researcher hybrid)
- **Multi-step research loops**: Query → Search → Read → Summarize → Reflect → Finalize
- **Configurable depth levels**: Quick (1 loop), Standard (3 loops), Deep (5+ loops)
- **Source diversity**: Web (DuckDuckGo/SearXNG), local files (PDF, DOCX, CSV, TXT), ArXiv, GitHub
- **Citation tracking**: Every claim linked to source with confidence scoring
- **Report generation**: Markdown, PDF, DOCX with professional formatting
- **Research memory**: Save/load research sessions, continue interrupted research

#### B. Multi-Agent Simulation (MiroFish-inspired)
- **Agent spawning**: Create 10-100 specialized AI agents with distinct personas
- **Persona templates**: Economist, Skeptic, Optimist, Historian, Technical Expert, etc.
- **Debate mode**: Agents discuss findings, challenge each other's conclusions
- **Prediction tracking**: Log agent predictions, compare against future outcomes
- **Consensus algorithm**: Weighted voting system for final conclusions

#### C. OSINT Intelligence Map (Shadowbroker-inspired)
- **Real-time feeds**: Flight tracking (ADS-B Exchange), maritime (AIS), weather, seismic
- **Geospatial visualization**: Interactive globe showing data points
- **Entity extraction**: Auto-identify people, organizations, locations from research
- **Relationship mapping**: Knowledge graph of connections between entities
- **Alert system**: Monitor topics, notify on significant changes

#### D. Knowledge Management
- **Vector search**: Embeddings for semantic document search (nomic-embed-text or local equivalent)
- **GraphRAG**: Knowledge graphs for complex relationship queries
- **Zettelkasten integration**: Bidirectional linking, note-taking, idea discovery
- **Import/Export**: Zotero, Obsidian, Notion compatibility

### 3. Advanced Capabilities

#### Research Automation
- **Scheduled research**: Cron-like scheduling for topic monitoring
- **Diff tracking**: Compare research results over time, highlight changes
- **Multi-language**: Auto-translate sources, research in any language
- **Fact-checking**: Cross-reference claims across multiple sources

#### Visualization & UI
- **Dark mode default**: Professional, hacker-aesthetic interface
- **Research tree**: Visual graph of research path, branches, dead-ends
- **Timeline view**: Chronological display of events found
- **Source credibility dashboard**: Domain reputation, bias indicators
- **Mobile-responsive**: Works on tablet/phone for field research

#### Local AI Optimization
- **Model quantization**: Auto-select 4-bit quantized models for speed
- **Context window management**: Smart chunking, recursive summarization
- **Parallel processing**: Async operations for I/O bound tasks
- **Memory-efficient**: Streaming responses, generator patterns for large docs

### 4. API & Extensibility

- **REST API**: Full programmatic access
- **Plugin system**: Python hooks for custom data sources, processors
- **Webhook support**: Trigger external actions on research completion
- **CLI tool**: `omni-research "query" --depth deep --output report.pdf`

### 5. Configuration & Deployment

#### Environment Variables (.env)
```bash
# LLM Configuration
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
FAST_MODEL=llama3.2:3b
SMART_MODEL=mistral:7b-instruct
EMBEDDING_MODEL=nomic-embed-text

# Search Configuration
SEARCH_ENGINE=duckduckgo  # or searxng, brave
SEARXNG_URL=  # optional
MAX_SEARCH_RESULTS=10
CONCURRENT_SEARCHES=3

# Research Configuration
MAX_RESEARCH_LOOPS=5
MAX_SOURCES_PER_QUERY=20
TIMEOUT_SECONDS=300

# Database
DATABASE_URL=sqlite:///./omni_research.db
VECTOR_DB_PATH=./chroma_db

# Features
ENABLE_OSINT=false  # Set true to enable real-time feeds
ENABLE_MULTI_AGENT=false  # Set true for agent simulation

Docker Compose Setup
Single command deployment:
bash
Copy

docker-compose up -d
# Exposes: Web UI (3000), API (8000), Ollama proxy (11434)

6. Project Structure
plain
Copy

omni-research/
├── backend/
│   ├── api/              # FastAPI routes
│   ├── core/             # Research engine, agents
│   ├── osint/            # Data feed aggregators
│   ├── models/           # Pydantic schemas
│   └── services/         # Search, LLM, storage
├── frontend/
│   ├── src/
│   │   ├── components/   # UI components
│   │   ├── pages/        # Routes
│   │   └── stores/       # State management
│   └── public/
├── agents/               # Agent persona definitions
├── plugins/              # Extension modules
├── notebooks/            # Example Jupyter notebooks
└── docker-compose.yml

7. Key Differentiators (Make it Better)

    Hybrid Reasoning: Combine chain-of-thought with multi-agent debate for higher accuracy
    Local-First Privacy: All data stays on device, encrypted at rest
    Adaptive Depth: Auto-adjust research depth based on query complexity
    Living Documents: Reports update automatically as new information arrives
    Research Templates: Pre-built modes (Investment Research, Academic Lit Review, OSINT Investigation, etc.)
    Cost Tracking: Monitor API costs (if using cloud backup), optimize for free local inference
    Offline Mode: Full functionality without internet (using cached data + local docs)

8. Success Metrics

    Answer accuracy > 85% on complex research queries
    Report generation < 5 minutes for standard depth
    Memory usage < 4GB peak for 8GB RAM systems
    Startup time < 30 seconds
    100% offline capability for core features

9. Deliverables

    Complete, documented source code
    Docker Compose deployment
    CLI tool
    Web interface
    Plugin development guide
    Example research templates
    Benchmark suite comparing to Perplexity/GPT Researcher

Constraints

    Must run on 8GB RAM, no GPU (CPU-only inference)
    Python 3.10+ compatible
    Fully open source (MIT or Apache 2.0 license)
    No hard dependencies on cloud APIs (optional fallbacks only)

plain
Copy


---

## 🚀 How to Use This with OpenCode

1. **Open OpenCode** (or any AI coding agent like Claude Code, Aider, etc.)
2. **Paste this entire prompt**
3. **Specify scope**: "Implement Phase 1: Core research engine with web UI" or "Build complete MVP"
4. **Iterate**: Start with backend API + simple frontend, add features incrementally

## 💡 Implementation Priority

| Phase | Features | Time Estimate |
|-------|----------|---------------|
| **1** | Basic research loop, web search, FastAPI backend, simple React UI | 2-3 days |
| **2** | Report generation (PDF/DOCX), citation tracking, research history | 1-2 days |
| **3** | Multi-agent debate, local file ingestion, vector search | 2-3 days |
| **4** | OSINT feeds, visualization, knowledge graph | 2-3 days |
| **5** | Polish, Docker, plugins, documentation | 1-2 days |

**Total MVP**: ~2 weeks for full-featured system

Want me to refine any specific section or break down a particular feature into technical specifications?

---
