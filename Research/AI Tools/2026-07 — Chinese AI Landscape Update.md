---
date: 2026-07-08
type: research
subtype: reference
tags: [ai, chinese-ai, deepseek, qwen, kimi, glm, benchmarks, local-llm]
priority: high
status: completed
source: "BenchLM, TokenMix, Vals AI, OpenRouter stats, model cards, API docs"
ai-first: true
---

# Chinese AI Landscape — July 2026 Update

**For future Claude:** Replaces your June 2026 note (`Research/AI Tools/2026-06-19 — AI-Specific Researcher Tools 2026 — Complete Table.md`). Chinese AI moves weekly. Key changes: Qwen3.7 Max leads, DeepSeek V4 on Huawei Ascend, GLM-5.2 agentic capabilities, pricing war intensifies.

---

## 1. Current Leaderboard (July 2026)

| Model | Developer | Benchmark | License | Cost/1M Input | Best For |
|-------|-----------|-----------|---------|---------------|----------|
| **Qwen3.7 Max** | Alibaba | 84 (BenchLM) | Apache 2.0 | $0.48 | General reasoning, legal, medical |
| **GLM-5.2** | Z.AI (Zhipu) | 83 (BenchLM) | Open-weight | Variable | Coding (SWE-bench 77.8%), agentic |
| **DeepSeek V4 Pro** | DeepSeek | 80 (BenchLM) | MIT | $0.028 | Lowest cost, coding, reasoning |
| **Kimi K2.5** | Moonshot | ~60 (Vals AI) | Modified MIT | $0.60 | Finance, long-context, agentic workflows |
| **Qwen3.5 9B** | Alibaba | 81.7 (GPQA) | Apache 2.0 | $0.10 | Local deployment, high-volume |

---

## 2. Key Developments Since June 2026

| Development | Details |
|-------------|---------|
| **Qwen3.7 Max release** | Now leads Chinese models on composite benchmarks; multimodal with video understanding |
| **DeepSeek V4 on Huawei Ascend 950PR** | First major model running on domestic Chinese chips; delayed twice from April 2026 due to yield issues |
| **GLM-5.2 agentic capabilities** | Strongest Chinese model for tool use and multi-step reasoning |
| **Pricing war intensifies** | Chinese models are 10–180x cheaper than Claude Opus 4.6 / GPT-5.4 |
| **US-China gap** | ~6 months on standard benchmarks; 8+ months on novel evaluations (ARC-AGI 2) |

---

## 3. Access & Infrastructure

- **API availability**: All major models have API access; Qwen and DeepSeek have most reliable international endpoints
- **Local deployment**: Qwen3.5 9B (Q4_K_M) is optimal for 8GB RAM; DeepSeek 7B also viable
- **Censorship**: All Chinese models have embedded safety filters; avoid for politically sensitive topics

---

## 4. For Your 8GB RAM Laptop (i5-8350U)

| Use Case | Model | Quantization | Context | Notes |
|----------|-------|--------------|---------|-------|
| **Primary: General reasoning** | Qwen2.5 7B | Q4_K_M | 4096 | Best all-rounder |
| **Secondary: Coding** | DeepSeek 7B | Q4_K_M | 4096 | Strong on code |
| **Classification/Router** | Phi-3 3.8B | Q4_K_M | 4096 | Fast, use as router front-end |
| **Chinese content** | Qwen3.5 9B | Q4_K_M | 4096 | Best Chinese model for local |

**Avoid**: GLM-5.2 (too large), Kimi K2.5 (not available locally), Qwen3.7 Max (too large)

---

## 5. Tier 1 — Technically Strong, Undercovered (Updated)

| Model | Lab | Why Interesting |
|-------|-----|-----------------|
| **MiMo V2.6 Pro** | Xiaomi | Most-used model on OpenRouter by wide margin; Xiaomi has 3× OpenAI's share |
| **StepFun Step-3.5** | StepFun Shanghai | Multimodal — text, video, music, audio; Step 3.5 Flash = cheapest math model |
| **GLM-5.2 / Zhipu AI** | Zhipu AI Beijing | First to train frontier model entirely on Huawei Ascend chips; agentic leader |
| **MiniMax M3** | MiniMax | Predicts user intent mid-conversation; frontier coding + multimodal + computer use |
| **Yuanbao** | Tencent | Hunyuan + DeepSeek R1 reasoning; WeChat integration; top of China iOS charts |

---

## 6. Vault Updates Required

- [ ] Replace `Research/AI Tools/2026-06-19 — AI-Specific Researcher Tools 2026 — Complete Table.md` with this updated version
- [ ] Create `Research/AI Tools/2026-07 — Chinese AI Landscape Update.md` with this content
- [ ] Update `05 - MAPS/AI & Technology MOC.md` — refresh Chinese AI section
- [ ] Update `History-Watchdog` and `Health-Autopilot` model configs with July recommendations
- [ ] Note: Ollama pulls for qwen2.5:7b, deepseek-r1:7b, deepseek-coder-v2 still valid

---

## 7. Sources

| Source | Type |
|--------|------|
| BenchLM leaderboard | Benchmark |
| TokenMix pricing tracker | Market data |
| Vals AI evaluations | Benchmark |
| OpenRouter traffic stats | Usage data |
| Model cards (HuggingFace) | Technical specs |

---

*Report 9 of 20 | Generated: 2026-07-08 | Priority: 🟡 High | Domain: AI/Tech*