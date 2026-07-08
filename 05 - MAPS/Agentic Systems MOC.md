---
date: 2026-07-08
type: map
tags: [moc, agentic-systems, ai-agents, architecture, sop, evaluation]
priority: medium
status: completed
ai-first: true
---

# Agentic Systems MOC

**For future Claude:** You have 4+ agent projects (genericagent, History Watchdog, Health Autopilot, autoresearch, InfiniteBrain Night Shift) but no unifying map. This MOC provides architecture patterns, SOP framework, and evaluation methodology.

---

## 1. Architecture Patterns

| Pattern | Description | Your Projects |
|---------|-------------|---------------|
| **ReAct** | Reasoning + Acting loop; LLM thinks, then uses tool, then observes | History Watchdog (news monitoring) |
| **Plan-and-Execute** | LLM plans steps first, then executes sequentially | Health Autopilot (12-week protocol) |
| **Multi-agent** | Multiple specialized agents with router/scheduler | Dravidian Graph (entity extraction + relation inference + verification) |
| **Reflection** | Agent reviews own output and self-corrects | Autoresearch (draft review) |

---

## 2. SOP Framework for Your Agents

```yaml
# genericagent SOP template
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

### Core SOP Components

| Component | Purpose | Implementation |
|-----------|---------|----------------|
| **Observe** | Input gathering | MCP servers (filesystem, web, memory) |
| **Reason** | Analysis & decision | Local LLM (qwen2.5:7b) + structured prompts |
| **Act** | Tool execution | MCP tool calls, file writes, memory stores |
| **Reflect** | Self-correction | Compare output to expected schema; flag anomalies |
| **Memory** | Persistent context | ChromaDB vector store + JSON logs |

---

## 3. Evaluation & Observability

| Aspect | Tool/Method | Metrics |
|--------|-------------|---------|
| **Tracing** | Langfuse or OpenTelemetry | Step latency, tool call count, error rate |
| **Task Completion** | Automated checklists | % tasks completed, % requiring human intervention |
| **Tool Use Accuracy** | Log analysis | Correct tool selection, parameter validity |
| **Hallucination Rate** | Manual review (sampled) | Factual errors per 1000 tokens |
| **Memory Evaluation** | Precision/recall on retrieval | Retrieved vs ideal context overlap |

---

## 4. Your Agent Inventory

| Agent | Pattern | Model | MCP Servers | Status |
|-------|---------|-------|-------------|--------|
| **genericagent (base)** | ReAct | qwen2.5:7b | filesystem, web, memory | Framework |
| **History Watchdog Scout** | ReAct | qwen2.5:7b | filesystem, web, memory | Spec'd |
| **Health Autopilot** | Plan-and-Execute | Phi-3 3.8B → Qwen2.5 7B | filesystem, python, memory | Spec'd |
| **Dravidian Graph Builder** | Multi-agent | Qwen2.5 7B + DeepSeek 7B | filesystem, python, web | Spec'd |
| **Autoresearch** | Reflection | DeepSeek 7B | filesystem, web | Active |
| **Night Shift (InfiniteBrain)** | Pipeline | Mixed | filesystem, web, memory, git | Active |

---

## 5. Vault Integration

- **Links to**: `genericagent/memory/autonomous_operation_sop.md`
- **Links to**: `03 - PROJECTS/History-Watchdog.md`
- **Links to**: `03 - PROJECTS/Health-Autopilot.md`
- **Links to**: `03 - PROJECTS/Dravidian-Lineage-Graph.md`
- **Links to**: `03 - PROJECTS/autoresearch.md`
- **Links to**: `house-rules.md` (Night Shift rules)

---

*Report 16 of 20 | Generated: 2026-07-08 | Priority: 🟢 Medium | Domain: AI/Tech*