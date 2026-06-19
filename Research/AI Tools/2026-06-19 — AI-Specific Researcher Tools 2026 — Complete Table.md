---
date: 2026-06-19
type: literature
subtype: reference
source: conversation transcript
author: Claude (compiled from web research)
status: to-process
ai-first: true
tags: [research-tools, ai-platforms, reference]
---

## For future Claude
Comprehensive reference table of AI research tools organized by category: pure AI research platforms, deep research options, specialized tools by task, Chinese AI alternatives, and optimal stacks for different use cases. Updated June 2026.

---

# AI-Specific Researcher Tools 2026 — Complete Table

> Compiled from web research June 2026. Does NOT include generic chatbots — only specialized research platforms.

---

## Pure AI Research Platforms (Not Generic Chatbots)

| Tool | What It Does | Free? |
|------|--------------|-------|
| **Undermind.ai** | Deep academic search, shows reasoning chain | Free tier |
| **Elicit.org** | Systematic evidence gathering, comparison tables across papers | Free tier |
| **Consensus.app** | Evidence-meter answers from 200M+ papers | Free tier |
| **SciSpace** | Chat with PDFs, thematic analysis, copilot feature | Free tier |
| **Paperguide.ai** | Full end-to-end: literature review + writing + citations | Free tier |
| **ResearchRabbit** | Citation graph explorer, paper discovery | Fully free |
| **Litmaps** | Visual citation network maps | Free tier |
| **Inciteful.xyz** | Find bridge papers between two papers | Fully free |
| **Scholarcy** | Converts papers → interactive flashcards | Free tier |
| **Scite.ai** | Shows if paper was SUPPORTED or DISPUTED by later research | Free tier |

---

## Deep Research Mode — Where to Get Free

Deep Research available free in: **Gemini, ChatGPT, DeepSeek, Grok, Kimi, Perplexity**.

**Claude Deep Research = paid only.** (Oklahoma State University)

> **Important caveat:** These systems search only open websites, not scholarly content behind paywalls. For scholarly deep research, use **Elicit, Undermind, or SciSpace** instead — they search Semantic Scholar data.

---

## Specialized AI Tools by Task

| Task | Best Tool |
|------|-----------|
| Systematic literature review | Elicit |
| Citation verification (supported/disputed) | Scite.ai |
| Visual citation map | Litmaps or Connected Papers |
| Chat with uploaded PDFs | SciSpace or Claude |
| Multi-doc synthesis | NotebookLM |
| Paper → flashcards | Scholarcy |
| Find bridge between 2 papers | Inciteful.xyz |
| Data analysis + charts via chat | Julius AI (free tier) |
| Academic writing polish | Paperpal (free tier) |

---

## Important Warning

- **Semantic Scholar** remains best free 200M-paper search
- **ResearchRabbit** and **Connected Papers** are cleanest citation-graph explorers
- **NotebookLM** is best multi-source synthesis sandbox
- **Scite** is the one to trust for citation context (AI Paper Writer)

**But:** Many academic AI systems are based on Semantic Scholar, which is vast but still smaller than Google Scholar and specialized library databases — so you won't get comprehensive search with one tool alone. (Oklahoma State University)

**Use minimum 2-3 tools in combo. No single tool = complete coverage.**

---

## Optimal Free Stack for Your Use Case

### UCH / Indian History Research
```
Perplexity → Elicit (papers) → Scite (verify study) → NotebookLM (synthesize) → Claude (critical analysis)
```

### Political/Media Research
```
Consensus → GDELT → MediaCloud → Claude (bias framing)
```

### Quick Claim Verification
```
Undermind → Scite → primary source
```

---

## New Tools You Likely Don't Use Yet

| Tool | Purpose |
|------|---------|
| **Undermind** | Best reasoning-chain academic search |
| **Julius AI** | Chat with data/spreadsheets free |
| **Scholarcy** | Paper → flashcard pipeline |
| **Inciteful** | Gap analysis between two papers |
| **SciSummary** | Bulk paper summarization with figure interpretation |

---

## Chinese AI Tools — Complete Guide (June 2026)

### Big 4 — Use These Now

| Model | Lab | Access | Best For |
|-------|-----|--------|----------|
| **DeepSeek** | DeepSeek (Hangzhou) | chat.deepseek.com — free, no card | General research, reasoning, math, coding |
| **Kimi** | Moonshot AI (Beijing) | kimi.com — free tier | Long docs, paper summarization, deep research |
| **Qwen** | Alibaba | chat.qwen.ai — free tier | Multilingual (119 langs), broad knowledge |
| **Doubao** | ByteDance | doubao.com — free | Creative writing, content |

### Benchmarks (June 2026 — Verified Data)

Current Chinese leaderboard:
- **DeepSeek V4 Pro** at 87
- **GLM-5.1** at 83
- **Kimi K2.6** at 81
- **Qwen3.5 397B** at 79

All within striking distance of Western frontier models. **Kimi K2.6** became first open-weight model to beat GPT-5.4 on SWE-Bench Pro for coding. **DeepSeek V3.2** holds price/performance throne. (BenchLM, TokenMix)

### For Research Specifically

**Kimi is your best Chinese research tool:**
- Leads for long document reading, paper summarization, and deep research
- Ultimate study companion (Jilo)

**DeepSeek runner-up:**
- Free, exceptional at math and logical reasoning
- **Deep Seek Deep Research:** searches web, compiles structured reports. Free, no limit like Perplexity. (Oklahoma State University)

---

## Lesser Known Chinese AI — Underrated

| Tool | Lab | Why Interesting |
|------|-----|-----------------|
| **GLM / Zhipu AI** | Zhipu AI Beijing | chat.zhipuai.cn — strong reasoning, free tier |
| **Doubao** | ByteDance | Native video reasoning, 5× cheaper than DeepSeek API |
| **MiniMax** | MiniMax | hailuoai.com — multimodal, video generation |
| **Moonshot** | Moonshot | 1M token context window |
| **Yi** | 01.AI | Open weights, stable, less hallucination |
| **Step** | StepFun | stepfun.com — fast, cheap, vision+video |
| **Baidu ERNIE** | Baidu | yiyan.baidu.com — real-time web search built in |

---

## Open Weight = Run Locally Free

**Qwen3.5** strongest multilingual choice, unmatched Chinese/Japanese/Korean under Apache 2.0. **DeepSeek** cheapest API at $0.14–0.30/M tokens. (Remote OpenClaw)

Models you can pull via Ollama right now on Feren OS:
```bash
ollama pull qwen2.5:7b
ollama pull deepseek-r1:7b
ollama pull deepseek-coder-v2
```
All run on i5-8350U with 8GB RAM at 7B size.

---

## Critical Warning — Censorship

All Chinese models carry hard-coded content restrictions on politically sensitive topics. (Remote OpenClaw)

**Specifically blocked or heavily filtered:**
- Tiananmen, Tibet, Taiwan, Xinjiang
- CCP criticism
- Falun Gong
- Any anti-CCP political analysis

**For Indian political research, history, religion — no problem.** For anything touching China politically — use Western AI.

DeepSeek and Kimi are more permissive than Baidu (ERNIE) and ByteDance (Doubao), which enforce stricter content policies. (Jilo)

---

## Best Use Combo for Your Research

| Use Case | Tool |
|----------|------|
| Long document analysis | Kimi (best long context) |
| Deep research report | DeepSeek Deep Research (free, web search) |
| Multilingual sources | Qwen (119 languages) |
| Local/private | Ollama + qwen2.5:7b |
| Coding projects | DeepSeek V4 Pro |

**Bottom line:** DeepSeek + Kimi = best free Chinese AI for research. Both English-friendly, internationally accessible, genuinely competitive with Claude/GPT on most tasks. Use alongside Western tools — never as sole source.

---

## Tier 1 — Technically Strong, Nobody Talks About

| Model | Lab | Access | Why Interesting |
|-------|-----|--------|-----------------|
| **MiMo V2.5 Pro** | Xiaomi | OpenRouter free preview | Most-used model on OpenRouter by wide margin. Xiaomi has 3× OpenAI's share. Almost zero Western coverage. (Digital Applied Team) |
| **StepFun / Step-3** | StepFun Shanghai | stepfun.com | Founded by former Microsoft VP Jiang Daxin. Multimodal — text, video, music, audio. Step 3.5 Flash = cheapest math model alive. (Second Talent) |
| **GLM / Zhipu AI** | Zhipu AI Beijing | chatglm.cn | First to train frontier model entirely on Huawei Ascend chips — zero Nvidia hardware. Tops open-source leaderboards. (Remote OpenClaw) |
| **MiniMax M3** | MiniMax | hailuoai.com | Predicts user intent mid-conversation. Only Chinese model combining frontier coding + multimodal + computer use. |
| **Yuanbao** | Tencent | yuanbao.tencent.com | Built on Hunyuan model + DeepSeek R1 reasoning. Available directly through WeChat. Rose to top of China iOS charts. (Second Talent) |

---

## Tier 2 — Academic / Open Weight Gems

| Model | Origin | Access | Why Useful |
|-------|--------|--------|------------|
| **WuDao 3.0 / Aquila** | BAAI (Beijing AI Institute) | HuggingFace | 1.75 trillion parameters. Includes AquilaChat, AquilaCode, visual/multimodal systems. Multi-language, multi-chip compatible. Non-profit research grade. (Second Talent) |
| **MOSS** | Fudan University | GitHub/HuggingFace | First open-source conversational model in China with plugin support. Apache-2 license. (IntuitionLabs) |
| **ChatGLM-6B** | Tsinghua + Zhipu | HuggingFace | Supports 1M tokens with INT4 quantization on 6GB GPU — lowest deployment barrier of all Chinese models. Runs on your machine. (Index.dev) |
| **Baichuan-4** | Baichuan AI | baichuan-ai.com | Four public APIs. Supports image + text input. Strong general knowledge, math, coding. Open weights available. (Second Talent) |

---

## Tier 3 — Domain Specific (Nobody Knows These)

Chinese teams fine-tuned open models for specific domains: (IntuitionLabs)

| Model | Domain | Source |
|-------|--------|--------|
| ChatLaw | Legal — Chinese law | Beijing Univ. of Posts & Telecom |
| DoctorGLM | Medical | ShanghaiTech University |
| EduChat | Education | Open academic |
| TigerBot | Finance/economics | No |
| 360 Zhinao | General, security | 360 Security Group |

All on HuggingFace. Free weights. Fine-tune or query directly.

---

## Tier 4 — Multimodal Hidden Ones

| Tool | What It Does | Access |
|------|--------------|--------|
| **HunyuanVideo** | Tencent — best open-weight video generation | HuggingFace |
| **Hunyuan3D** | Tencent — 3D model generation from text/image | HuggingFace |
| **Seedance 2.0** | ByteDance — video quality benchmark setter | Via Doubao app |
| **Kling** | Kuaishou — video generation, global access | klingai.com free tier |
| **Jimeng AI** | ByteDance — image+video gen | jimeng.jianying.com |
| **RedNote OCR model** | Xiaohongshu — character recognition model that surprised many | Interconnects Limited |

---

## The Real Hidden Story

Chinese share crossed **45% of OpenRouter traffic**. One year ago Chinese AI providers were less than 2% of OpenRouter tokens. **MiMo-V2-Pro** is single most-used model on the platform by wide margin — but almost no Western media covers it. (Digital Applied Team)

Most people chase DeepSeek/Kimi headlines. Meanwhile Xiaomi's MiMo quietly became the world's most-used open model.

---

## Practical Access — All Free Tiers

```
stepfun.com        → Step-3 chat, free
chatglm.cn         → GLM chat, free
yuanbao.tencent.com → Yuanbao (Hunyuan+DeepSeek), free
klingai.com        → Kling video, free tier
hailuoai.com       → MiniMax/Hailuo video, free
baichuan-ai.com    → Baichuan chat, free tier
```

**HuggingFace pull:**
```
→ THUDM/chatglm3-6b (runs 6GB RAM)
→ baichuan-inc/Baichuan2-7B-Chat
→ WuDao/AquilaChat-7B
→ fnlp/moss-moon-003-sft
```

**Summary:** Real hidden gems = **MiMo (Xiaomi)**, **StepFun**, **GLM (Zhipu)**, domain models (ChatLaw/DoctorGLM), and **ChatGLM-6B** for local use on low VRAM. Nobody in India talks about any of these.

---

## Links
- Related: [[AI Research Tools]], [[Chinese AI Models]], [[NotebookLM]], [[Elicit]], [[Scite.ai]], [[Perplexity]], [[DeepSeek]], [[Kimi]]
- Applied in: [[Research Workflow]], [[Literature Review Process]]

## Metadata
- Compiled: 2026-06-19
- Source: Conversation transcript (web research via multiple sources)
- Tags: research-tools, ai-platforms, reference, chinese-ai