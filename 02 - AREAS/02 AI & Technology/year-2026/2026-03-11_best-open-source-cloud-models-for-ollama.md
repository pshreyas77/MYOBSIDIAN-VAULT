---
title: "Best open source AI models for Ollama"
date: 2026-06-06
tags:
  - machine-learning
  - llm-ai
  - linux
  - ollama
  - open-source
source: claude-export
---

# Best open source AI models for Ollama

> **For future Claude**: This note tracks the best open-source models available through Ollama as of June 2026. Hardware constraints (8GB RAM, integrated GPU on HP ProBook) limit local runs — cloud/API access required for larger models. Updated from March 2026 version with Kimi K2.6, DeepSeek V4, Qwen3 235B, Gemma 4, OpenClaw, vLLM, and Ollama v0.24.0.

**Date:** 2026-06-06 (updated from 2026-03-11) · **Hardware:** HP ProBook (8GB RAM, integrated GPU) · **Topics:** [[Machine-Learning]] · [[LLM-AI]] · [[Linux]] · [[Ollama]]

---

## Top Models by Category (June 2026)

### 🏆 Best Coding / Agentic

| Model | Size | Key Strengths | Local? |
|-------|------|---------------|--------|
| **Kimi K2.6** | — | Top open-source coding model, native multimodal (vision + language + agentic) | ❌ |
| **Qwen3-Coder** | 30B / 480B | 3.5M pulls, tools support, long context, great for agents | ❌ |
| **Devstral-Small-2** | 24B | Vision + tools, multi-file editing, built for SWE agents | ❌ |
| **Devstral-2** | 123B | Beefier Devstral, same agentic focus | ❌ |

> **Kimi K2.6 note:** K2.6 is the current top open-source coding model as of June 2026. Native multimodal with vision + language + agentic capabilities. (Source: research, 2026-06)

### 🧠 Best Reasoning / Thinking

| Model | Size | Key Strengths | Local? |
|-------|------|---------------|--------|
| **DeepSeek V4** | 671B | 1M token context window, hybrid thinking + non-thinking, tools support | ❌ |
| **Qwen3-Next** | 80B | Strong performance-per-parameter, thinking mode, tools | ❌ |
| **DeepSeek-V3.1** | 671B | Previous generation, still very capable | ❌ |
| **Nemotron-3-Nano** | 30B | Thinking + tools at manageable size | ❌ |

> **DeepSeek V4 note:** Released with 1M token context (up from V3.1). Apache 2.0 licensed. (Source: research, 2026-06)

### ⚡ Best Lightweight / Efficient

| Model | Size | Key Strengths | Local? |
|-------|------|---------------|--------|
| **Qwen3.5** | 0.8B–122B | Runs from 0.8B to 122B, vision + tools + thinking, most flexible | ✅ small sizes |
| **Gemma 4** | 26B | Google MoE, 85 tok/s on consumer GPU, Apache 2.0 | ✅ |
| **Gemma3** | — | 33M pulls, single GPU, solid general purpose | ✅ |
| **Ministral-3** | 3B–14B | Vision + tools, edge-focused | ✅ |

> **Gemma 4 note:** Google MoE architecture, 26B parameters, achieves 85 tok/s on consumer hardware. Apache 2.0 licensed. (Source: research, 2026-06)

### 👁️ Best Multimodal / Vision

| Model | Size | Key Strengths | Local? |
|-------|------|---------------|--------|
| **Qwen3-VL** | 2M–30B pulls | Strongest vision-language in Qwen family, tools + thinking | ❌ large |
| **Kimi K2.6** | — | Native multimodal with vision + language + agentic | ❌ |
| **Qwen3.5** | 4B–122B | Vision support across size range | ✅ small sizes |

### 🔧 Tooling & Infrastructure

| Tool | Note |
|------|------|
| **Ollama v0.24.0** | 4,500+ models, Gemma 4 support, regular releases |
| **vLLM** | #1 GitHub contributors 2025, top inference engine |
| **OpenClaw** | 302k+ GitHub stars, fastest-growing project, local AI with 50+ integrations |

> **OpenClaw note:** As of June 2026, OpenClaw has 302k+ GitHub stars — fastest-growing GitHub project. Local AI with 50+ integrations. Previous note (Feb 2026) was unclear on what OpenClaw was; now confirmed as a major open-source local AI platform. (Source: research, 2026-06)

---

## Recommendations for HP ProBook (8GB RAM, Integrated GPU)

**Hardware constraint:** 8GB RAM, integrated GPU — large models cannot run locally.

### What CAN run locally:

| Use Case | Model | Size | Notes |
|----------|-------|------|-------|
| General chat | **Gemma 4** | 26B | 85 tok/s, Apache 2.0 |
| Lightweight tasks | **Qwen3.5** | 4B–9B | Vision + tools + thinking |
| Fast inference | **Gemma3** | — | 33M pulls, single GPU |

### What requires cloud/API:

- Kimi K2.6 (coding)
- DeepSeek V4 (reasoning, 1M context)
- Qwen3 235B-A22B (Apache 2.0)
- Qwen3-Coder 480B
- Devstral-2 123B
- DeepSeek-V3.1 671B

---

## Quick Reference (Updated Table)

| Use Case | Recommended Model | Why |
|----------|-------------------|-----|
| Coding agent | **Kimi K2.6** | Top open-source coding model (June 2026) |
| General chat | **Gemma 4** (26B) | Fast, Apache 2.0, runs on consumer GPU |
| Vision tasks | **Qwen3-VL** (8B) or **Kimi K2.6** | Both strong, pick based on size |
| Reasoning/thinking | **DeepSeek V4** (cloud) | 1M token context |
| Low VRAM | **Qwen3.5** (4B–9B) | Most flexible size range |
| Local inference | **Ollama v0.24.0** | 4,500+ models, Gemma 4 support |

---

## Changelog

- **2026-06-06**: Major update — added Kimi K2.6 (top coding), DeepSeek V4 (1M context), Qwen3 235B-A22B (Apache 2.0), Gemma 4 (Google MoE, 26B, 85 tok/s), OpenClaw (302k stars), vLLM (#1 contributors 2025), Ollama v0.24.0. Updated hardware section for HP ProBook.
- **2026-03-11**: Original note — Qwen3-Coder, Devstral, DeepSeek-V3.1, Qwen3.5, Gemma3, Qwen3-VL, Kimi-K2.5

---