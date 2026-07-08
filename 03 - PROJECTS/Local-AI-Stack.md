---
date: 2026-07-08
type: project
tags: [project, local-ai, obsidian, notebooklm, hermes-agent, apple-silicon, b2b-automation, cost-optimization]
status: active
ai-first: true
source: "Personal implementation log"
---

# Local AI Stack: Obsidian + NotebookLM + Hermes Agent on Apple Silicon

**For future Claude:** Complete implementation log of replacing $340/month cloud AI subscriptions with a fully local, self-learning second brain running on Mac Mini M4. Covers architecture, memory engine, hardware specs, automation bridges, and ROI.

---

## 1. The Three-Layer Architecture

Traditional vector search fails to track global themes and complex relationships in large files. Our setup divides labor across four system layers:

| Layer | Primary Software | Input Source | Output Target |
|-------|-----------------|--------------|---------------|
| **Active Execution** | Hermes Agent / Claude Code | Obsidian Vault / User Commands | Local terminal / SQLite State |
| **Passive Semantic** | Google NotebookLM / notebooklm-py | Local PDF and Markdown files | Structured summaries / Audio overviews |
| **Durable Memory** | Obsidian Vault | Raw input logs / Agent outputs | PARA-structured notes |
| **Ambient Capture** | Omi / SuperWhisper | Ambient audio / Voice inputs | Markdown files in Obsidian inbox |

**Key Insight**: Obsidian stores your data securely but lacks native reasoning. NotebookLM excels at digesting external literature but lacks native local storage or linking. Together, they form a unified brain.

---

## 2. The 5-Tier Memory Engine

Mathematical context compression:
```
C(t) = S_base + Compress(L(t)) + U_profile
```

Where:
- `C(t)` = context window size at turn t
- `S_base` = system prompt size
- `Compress(L(t))` = compressed historical logs using SQLite FTS5
- `U_profile` = user profile (capped at 1,300 tokens)

| Level | Tier | Storage | Capacity | Purpose |
|-------|------|---------|----------|---------|
| **1 (Hot)** | local `memory.md` / `user.md` | Agent profile | 1,300 tokens | Instant preferences, active guidelines |
| **2 (Session Log)** | SQLite `state.db` | FTS5 search engine | Cross-session | Fast history searches, message retrieval |
| **3 (Active Context)** | Dynamic memory buffers | Retrieval plugins | Task-relevant | Dynamic retrieval for current task |
| **4 (Durable Knowledge)** | Obsidian PARA notes | Markdown on disk | Permanent | Developed skills, corporate guidelines |
| **5 (Ambient Context)** | Omi audio logs + transcripts | `/Omi_Memories/` | Continuous | Background audio refined into summaries |

**Result**: Clean context window, no degradation after 10+ turns, VRAM stays free.

---

## 3. Hardware Specification

### Why Apple Silicon (Mac Mini M4)

Unified memory architecture = CPU + GPU share single memory pool. No VRAM bottleneck. Load large models without multi-GPU configs.

| Spec | Minimum | Recommended (M4 Pro) |
|------|---------|---------------------|
| **Memory Bandwidth** | 120 GB/s | 273 GB/s |
| **RAM** | 24 GB | 48 GB+ |
| **Models Supported** | Qwen 2.5 Coder 14B, Gemma 3 27B | Qwen3.5-Coder 32B, Llama-3.3-70B |
| **Power Draw** | 10–30W sustained | 15–40W |
| **Monthly Electricity** | <$5 | <$8 |

### Software Stack Setup

```bash
# Install base dependencies
brew install ripgrep ffmpeg node python

# Install Ollama runtime
curl -fsSL https://ollama.com/install.sh | sh

# Pull recommended models
ollama pull qwen3.5-coder:32b
ollama pull gemma3:27b
ollama pull deepseek-r1:14b
```

### Hermes Config (`~/.hermes/config.yaml`)

```yaml
provider: ollama
model: qwen3.5-coder:32b
api_base: http://localhost:11434
```

---

## 4. Automation Pathways & Bridges

### Bridge 1: Hermes ↔ Obsidian
```bash
# Set vault path
export OBSIDIAN_VAULT_PATH="E:/_Knowledge/ObsidianVault"

# Use hermes-agent-obsidian-plugin for sidebar sessions
```

### Bridge 2: Hermes ↔ NotebookLM (via notebooklm-py)

```python
# Automated upload from Obsidian to NotebookLM
from notebooklm import NotebookLM

client = NotebookLM(session_cookie="your_cookie_here")
client.upload_source(vault_path="/Agent_Workspace/research.md")
```

### Bridge 3: macOS Computer Use (for audio overviews)

When NotebookLM API isn't available, Hermes uses `macos-computer-use` skill to:
1. Open Chrome → `notebooklm.google.com`
2. Click elements to generate audio overviews
3. Download finished assets to local drive

### Bridge 4: Claude Code Alternative Backend

For coding tasks, Claude Code writes/runs tests directly in Obsidian folders. Over time, `CLAUDE.md` trains it as a personalized assistant.

---

## 5. Case Study: Huberman Health Vault (Bulk Ingestion)

**Manual effort**: 300 episodes × transcription + extraction = hundreds of hours  
**Automated pipeline**: Minutes

```mermaid
graph LR
    A[YouTube Playlist URLs] --> B[ytcli Parallel Download]
    B --> C[Structured MD in /inbox]
    C --> D[notebooklm-py Batch Upload]
    D --> E[NotebookLM: Huberman Health Vault]
    E --> F[Structured Query: Protocols + Citations]
    F --> G[Obsidian Permanent Notes + Wiki-links]
```

**Query example**: *"Compile all sleep protocols, reference scientific studies, return with exact citations"*

Output: Visual graph where videos cluster around sleep, cold exposure, memory retention.

---

## 6. Content Generation Loop

NotebookLM generates 12+ deliverable types from one notebook:
- Mind maps, study guides, briefing docs, audio overviews

**Workflow**:
1. Open Obsidian sidebar → launch Hermes session
2. Prompt: *"Draft content series on Huberman sleep protocols for newsletter"*
3. Hermes reads synthesized MD notes + `voice-guidelines.md`
4. Outputs finished drafts to folder, ready for review

**All local. Company guidelines + research stay confidential.**

---

## 7. Personal Assistant & Ambient Context

| Component | Function |
|-----------|----------|
| **Omi Wearable** | Captures spoken agreements → syncs to `/Omi_Memories` |
| **Morning Standup Cron** | 9:00 AM trigger → reads calendar + yesterday's Omi logs |
| **SuperWhisper** | Local speech-to-text dictation → Apple Silicon processor |
| **Converse Mode** | Forces clarifying questions before file edits |

**Loop**: Ambient context → Structured summaries → Actionable schedules → You stay in control.

---

## 8. Vault Maintenance Schedule

| Frequency | Tasks |
|-----------|-------|
| **Weekly** | Clear orphan notes; trim `MEMORY.md` if >4,000 chars |
| **Monthly** | Audit PARA dirs; review `issues-fixes-log.md`; write new crash-prevention rules |
| **On Failure** | Same as monthly + root cause analysis |

**Limits to enforce**:
- Directory access boundaries (agent can't escape vault)
- Parallel transcription throttling on 32B models
- Context window caps per tier

---

## 9. ROI Analysis

| Cost Category | Cloud (Old) | Local (New) |
|---------------|-------------|-------------|
| **Monthly Subscriptions** | $340 | $0 |
| **Hardware (Mac Mini M4)** | $0 | $599 (one-time) |
| **Electricity** | Included in cloud | ~$5/month |
| **Year 1 Total** | $4,080 | $659 |
| **Year 2+ Annual** | $4,080 | $60 |

### Savings
- **Year 1**: $3,421
- **Year 2+**: $4,020/year

### What You Gain
- Zero API limits or rate limits
- Zero prompt injection risk (data never leaves machine)
- 24/7 B2B pipeline execution
- Full data sovereignty
- Sub-5W silent operation

---

## 10. Current Vault Integration Status

| Component | Status | Location |
|-----------|--------|----------|
| **Obsidian Vault** | ✅ Active | `E:/_Knowledge/ObsidianVault` |
| **Hermes Agent** | ✅ Configured | `~/.hermes/config.yaml` → Ollama |
| **Ollama Models** | 🔄 Pending | `qwen3.5-coder:32b`, `gemma3:27b` |
| **NotebookLM Bridge** | 📋 Planned | `notebooklm-py` + cookie auth |
| **Omi Capture** | 📋 Planned | `/Omi_Memories/` inbox |
| **PARA Structure** | ✅ Active | `00-INBOX` through `07-SYSTEM` |
| **Memory Tiers** | 🔄 Partial | Levels 1, 2, 4 active; 3, 5 building |

---

## 11. Next Implementation Steps

- [ ] Pull Ollama models (`qwen3.5-coder:32b`, `gemma3:27b`)
- [ ] Configure `OBSIDIAN_VAULT_PATH` in Hermes
- [ ] Set up `notebooklm-py` with session cookies
- [ ] Build `macos-computer-use` workflow for NotebookLM audio
- [ ] Integrate Omi wearable → `/Omi_Memories` sync
- [ ] Implement Level 3 (Active Context) dynamic retrieval
- [ ] Create `voice-guidelines.md` for brand tone
- [ ] Schedule weekly/monthly maintenance cron jobs
- [ ] Document `issues-fixes-log.md` template

---

## 12. Key Files in This Vault

| File | Purpose |
|------|---------|
| `03 - PROJECTS/Local-AI-Stack.md` | This note |
| `05 - MAPS/Agentic Systems MOC.md` | Architecture patterns |
| `05 - MAPS/Digital Garden MOC.md` | PKM methodology |
| `Research/AI Tools/MCP-Ollama-Local-LLM-Production-Guide.md` | Technical MCP setup |
| `genericagent/memory/autonomous_operation_sop.md` | Agent SOP framework |
| `house-rules.md` | Night Shift automation rules |

---

*Created: 2026-07-08 | Status: Implementation in progress | Hardware: Mac Mini M4 (on order) | Target: Full local B2B pipeline by 2026-07-31*