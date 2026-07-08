---
date: 2026-07-08
type: research
subtype: technical-guide
tags: [ai, mcp, ollama, local-llm, production, agentic-systems]
priority: high
status: completed
source: "MCP spec (July 2026), Ollama docs, LiteLLM proxy, production deployment patterns"
ai-first: true
---

# MCP Server + Ollama Local LLM — Production Guide

**For future Claude:** Technical backbone for all 3 new projects (History Watchdog, Health Autopilot, Dravidian Graph). Your hardware: i5-8350U, 8GB RAM, integrated graphics. This guide makes it work in production.

---

## 1. MCP (Model Context Protocol) Architecture

### Current Spec (July 2026)

| Aspect | Detail |
|--------|--------|
| **Transport** | stdio (local processes) vs HTTP/SSE (remote servers) |
| **Auth** | OAuth 2.0 or API key; no standardized auth yet |
| **Discovery** | Tool schemas exposed via JSON-RPC; clients auto-discover capabilities |
| **Multi-server** | No native orchestration; use mcp-cli or custom gateway |

### Production Pattern

```
User Request → Your App (FastAPI/Node) → LiteLLM Proxy → Ollama (local)
                              ↓
                        MCP Servers (filesystem, web, memory, code)
```

---

## 2. Ollama on Your Hardware (i5-8350U, 8GB RAM, Integrated Graphics)

### Realistic Constraints

| Constraint | Value |
|------------|-------|
| **Max model size** | 7B–9B parameters (Q4_K_M quantization) |
| **Context window** | 4096 tokens (safe); 8192 if you close all other apps |
| **Speed** | ~5–15 tokens/sec depending on model and CPU load |
| **Simultaneous models** | Do NOT run multiple models; use a router pattern |

### Recommended Models

| Use Case | Model | Quantization | Context | Notes |
|----------|-------|--------------|---------|-------|
| **General reasoning** | Qwen2.5 7B | Q4_K_M | 4096 | Best all-rounder |
| **Coding** | DeepSeek 7B | Q4_K_M | 4096 | Strong on code |
| **Classification/Router** | Phi-3 3.8B | Q4_K_M | 4096 | Fast, use as router front-end |
| **Chinese content** | Qwen3.5 9B | Q4_K_M | 4096 | Best Chinese model for local |

---

## 3. Structured Output & Function Calling

Ollama (as of 2025) supports:

- **JSON mode**: `format: json` — forces JSON output
- **Tool calling**: Native function calling via `tools` parameter (stabilized 2025)
- **System prompts**: Reliable for constraining output format

### Production Tip

Always validate JSON output with Pydantic/Zod schemas; LLMs occasionally hallucinate keys.

---

## 4. MCP Server Setup for Your Projects

### History Watchdog

| MCP Server | Purpose |
|------------|---------|
| `filesystem` | Read vault notes, write findings |
| `web` | Search news, academic sources |
| `memory` | Store findings across runs |
| `git` | Track changes to vault |

```yaml
# History Watchdog MCP config
mcp_servers:
  filesystem:
    command: npx
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/vault"]
  web:
    command: uvx
    args: ["mcp-server-web-search"]
  memory:
    command: node
    args: ["mcp-memory-server/dist/index.js"]
```

### Health Autopilot

| MCP Server | Purpose |
|------------|---------|
| `filesystem` | Read daily logs, write weekly reviews |
| `python` | Calculate macros, progression, macros |
| `memory` | Track adherence, bloodwork trends |

### Dravidian Graph

| MCP Server | Purpose |
|------------|---------|
| `filesystem` | Read entity notes, write graph data |
| `python` | NetworkX operations, Cytoscape.js JSON export |
| `web` | Verify election data, caste demographics |

---

## 5. Configuration Template

```yaml
# ollama_config.yaml
models:
  general:
    name: qwen2.5:7b
    quant: Q4_K_M
    ctx: 4096
    system: "You are a precise research assistant. Respond in JSON."
  coding:
    name: deepseek-r1:7b
    quant: Q4_K_M
    ctx: 4096
    system: "You are a coding assistant. Write clean, documented code."
  router:
    name: phi3:3.8b
    quant: Q4_K_M
    ctx: 2048
    system: "Classify the user request into: general, coding, or research."

mcp_servers:
  filesystem:
    command: npx
    args: ["-y", "@modelcontextprotocol/server-filesystem", "E:/_Knowledge/ObsidianVault"]
  web:
    command: uvx
    args: ["mcp-server-web-search"]
  memory:
    command: node
    args: ["mcp-memory-server/dist/index.js"]
  python:
    command: uvx
    args: ["mcp-server-python"]
```

---

## 6. Genericagent SOP Integration

```yaml
# genericagent/memory/autonomous_operation_sop.md pattern
agent:
  name: "History Watchdog Scout"
  pattern: ReAct
  model: qwen2.5:7b
  mcp_servers: [filesystem, web, memory]
  
  loop:
    - observe: "Check RSS feeds, news APIs, and vault MOCs for changes"
    - reason: "Analyze if update is significant and novel"
    - act: "Store finding in memory; flag if critical"
    - reflect: "Was the analysis accurate? Should I alert the user?"

  memory:
    type: vector_store
    backend: chromadb
    retrieval: similarity_search
```

---

## 7. Vault Updates Required

- [ ] Create `Research/AI Tools/MCP-Ollama-Local-LLM-Production-Guide.md` with this content
- [ ] Create `ollama_config.yaml` in `genericagent/config/` or project root
- [ ] Update `genericagent/memory/autonomous_operation_sop.md` with MCP patterns
- [ ] Update all 3 project hubs (History Watchdog, Health Autopilot, Dravidian Graph) with MCP configs
- [ ] Test Ollama pulls: `ollama pull qwen2.5:7b`, `ollama pull deepseek-r1:7b`, `ollama pull phi3:3.8b`

---

## 8. Sources

| Source | Type |
|--------|------|
| MCP spec (July 2026) | Technical spec |
| Ollama docs / GitHub | Documentation |
| LiteLLM proxy docs | Proxy pattern |
| Production deployment blogs | Best practices |

---

*Report 10 of 20 | Generated: 2026-07-08 | Priority: 🟡 High | Domain: AI/Tech*