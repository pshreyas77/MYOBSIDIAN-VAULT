---
title: "Best open source cloud models for Ollama"
date: 2026-03-11
tags:
  - machine-learning
  - llm-ai
  - linux
  - geopolitics
source: claude-export
---

# Best open source cloud models for Ollama

> **Conversation Overview**

The person asked for recommendations on which open source cloud models are best to use through Ollama, referencing a list of available models. Claude provided a structured breakdown of top models organized by use case categories: best overall and coding/agent models (Qwen3-Coder, Devstral-Small-2, Devstral-2), best reasoning/thinking models (DeepSeek-V3.1, Qwen3-Next, Nemotron-3-Nano), best lightweight/efficient models (Qwen3.5, Gemma3, Ministral-3), and best multimodal/vision models (Qwen3-VL, Kimi-K2.5).

Claude noted the person is running a local setup on Feren OS, with VRAM as the primary hardware constraint, and tailored the final recommendations accordingly. A summary table was provided mapping specific use cases to recommended models, with Qwen3.5 and Gemma3 highlighted as the most flexible options for scaling based on available system resources. Key technical details referenced include model parameter sizes, pull counts, and capability flags such as tools support, vision, and thinking mode.

**Date:** 2026-03-11  
**Topics:** [[Machine-Learning]] · [[LLM-AI]] · [[Linux]] · [[Geopolitics]]

---

### 🧑 You

which open source cloud models are best to use through ollama from this

---

### 🤖 Claude

Looking at this list, the standout open-source cloud models worth using through Ollama depend on what you need:

**Best overall / coding & agents**
- **Qwen3-Coder** (30B or 480B) — massive pull count (3.5M), tools support, long context. Great for agentic coding.
- **Devstral-Small-2** (24B) — vision + tools, built specifically for software engineering agents and multi-file editing.
- **Devstral-2** (123B) — same as above but beefier, if you have the VRAM.

**Best reasoning / thinking**
- **DeepSeek-V3.1** (671B) — hybrid thinking + non-thinking, tools support. Very capable but massive.
- **Qwen3-Next** (80B) — strong performance-per-parameter, thinking mode, tools.
- **Nemotron-3-Nano** (30B) — thinking + tools at a more manageable size.

**Best lightweight / efficient**
- **Qwen3.5** — runs from 0.8B to 122B, vision + tools + thinking. Best range of size options here.
- **Gemma3** — 33M pulls (most popular on the list), runs on a single GPU, solid general purpose.
- **Ministral-3** — vision + tools, edge-focused, 3B–14B range.

**Best multimodal (vision)**
- **Qwen3-VL** (2M pulls) — strongest vision-language in the Qwen family, tools + thinking.
- **Kimi-K2.5** — native multimodal with vision + language + agentic capabilities.

---

**My top picks for practical local use:**

| Use case | Pick |
|---|---|
| Coding agent | Qwen3-Coder (30B) |
| General chat | Gemma3 (27B) |
| Vision tasks | Qwen3-VL (8B or 30B) |
| Reasoning/thinking | Qwen3-Next (80B) |
| Low VRAM | Qwen3.5 (4B or 9B) |

Since you're on Feren OS with a local setup, VRAM is likely the main constraint — Qwen3.5 and Gemma3 give you the most flexibility to scale up or down based on what your system can handle.

---
