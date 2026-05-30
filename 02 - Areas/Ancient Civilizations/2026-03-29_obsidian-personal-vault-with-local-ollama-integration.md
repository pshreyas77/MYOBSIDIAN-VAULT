---
title: "Obsidian personal vault with local Ollama integration"
date: 2026-03-29
tags:
  - machine-learning
  - llm-ai
  - data-analysis
  - linux
  - obsidian
  - stock-market
  - osint
  - research
  - creative
  - web-dev
  - game-design
source: claude-export
---

# Obsidian personal vault with local Ollama integration

> **Conversation Overview**

The person asked Claude to create a complete setup script to transform their existing Obsidian installation into a personal AI-powered knowledge vault, running entirely on local infrastructure via Ollama on Feren OS (an Ubuntu-based Linux distribution). The goal was a self-contained, privacy-respecting personal data vault with no cloud dependencies.

Claude produced a comprehensive bash script (`obsidian_vault_setup.sh`) that handles the full setup end-to-end. The script creates a structured vault folder hierarchy with ten named directories (Inbox, Daily Notes, Knowledge Base, Projects, Research, AI Conversations, OSINT, Finance, Career, Archive, Assets), writes all necessary Obsidian configuration files (app.json, hotkeys.json, appearance.json, core-plugins.json, daily-notes.json), and pre-populates plugin data files for four community plugins — Local GPT, Smart Connections, Templater, and Dataview — so they connect to Ollama automatically upon installation. The Local GPT configuration includes eight custom AI actions and a detailed system prompt. The script also generates four note templates (Daily Note, Research Note, AI Chat, Literature Note), a Dataview-powered HOME.md dashboard, a dark monolith CSS theme using JetBrains Mono and Syne fonts with an amber accent color, three shell utility commands (`vault-ollama-start`, `vault-ollama-stop`, `vault-status`) optimized for an 8GB RAM environment, an autostart desktop entry for Ollama, and a plugin installation guide saved to the desktop. The script pulls two Ollama models: `qwen2.5:1.5b` for chat and `nomic-embed-text` for semantic embeddings via Smart Connections.

**Date:** 2026-03-29  
**Topics:** [[Machine-Learning]] · [[LLM-AI]] · [[Data-Analysis]] · [[Linux]] · [[Obsidian]] · [[Stock-Market]] · [[OSINT]] · [[Research]] · [[Creative]] · [[Web-Dev]] · [[Game-Design]]

---

### 🧑 You

i want to make my obsedian like my personal data vault which is powered by ollama locally . so provide me complete script to modify and make it my personal space . feren os i i am using obsedian already so i just want to make it my personal vault

---

### 🤖 Claude

{'type': 'text', 'text': '     1\t---\n     2\tname: frontend-design\n     3\tdescription: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.\n     4\tlicense: Complete terms in LICENSE.txt\n     5\t---\n     6\t\n     7\tThis skill guides creation of distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. Implement real working code with exceptional attention to aesthetic details and creative choices.\n     8\t\n     9\tThe user provides frontend requirements: a component, page, application, or interface to build. They may include context about the purpose, audience, or technical constraints.\n    10\t\n    11\t## Design Thinking\n    12\t\n    13\tBefore coding, understand the context and commit to a BOLD aesthetic direction:\n    14\t- **Purpose**: What problem does this interface solve? Who uses it?\n    15\t- **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, etc. There are so many flavors to choose from. Use these for inspiration but design one that is true to the aesthetic direction.\n    16\t- **Constraints**: Technical requirements (framework, performance, accessibility).\n    17\t- **Differentiation**: What makes this UNFORGETTABLE? What\'s the one thing someone will remember?\n    18\t\n    19\t**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work - the key is intentionality, not intensity.\n    20\t\n    21\tThen implement working code (HTML/CSS/JS, React, Vue, etc.) that is:\n    22\t- Production-grade and functional\n    23\t- Visually striking and memorable\n    24\t- Cohesive with a clear aesthetic point-of-view\n    25\t- Meticulously refined in every detail\n    26\t\n    27\t## Frontend Aesthetics Guidelines\n    28\t\n    29\tFocus on:\n    30\t- **Typography**: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend\'s aesthetics; unexpected, characterful font choices. Pair a distinctive display font with a refined body font.\n    31\t- **Color & Theme**: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes.\n    32\t- **Motion**: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Use Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions. Use scroll-triggering and hover states that surprise.\n    33\t- **Spatial Composition**: Unexpected layouts. Asymmetry. Overlap. Diagonal flow. Grid-breaking elements. Generous negative space OR controlled density.\n    34\t- **Backgrounds & Visual Details**: Create atmosphere and depth rather than defaulting to solid colors. Add contextual effects and textures that match the overall aesthetic. Apply creative forms like gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, and grain overlays.\n    35\t\n    36\tNEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character.\n    37\t\n    38\tInterpret creatively and make unexpected choices that feel genuinely designed for the context. No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices (Space Grotesk, for example) across generations.\n    39\t\n    40\t**IMPORTANT**: Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate code with extensive animations and effects. Minimalist or refined designs need restraint, precision, and careful attention to spacing, typography, and subtle details. Elegance comes from executing the vision well.\n    41\t\n    42\tRemember: Claude is capable of extraordinary creative work. Don\'t hold back, show what can truly be created when thinking outside the box and committing fully to a distinctive vision.\n    43\t', 'uuid': '9a90c079-9712-40db-8e00-8cad2727add1'}
Let me think through what you need first — this is a multi-part setup:

1. **Ollama backend scripts** (model management, API bridge)
2. **Obsidian plugins config** (Local GPT, Smart Connections, Templater)
3. **A master setup script** that wires everything together on Feren OS
4. **A beautiful Obsidian CSS snippet** for your dark vault aesthetic

{'type': 'text', 'text': 'File created successfully: /home/claude/obsidian_vault_setup.sh', 'uuid': 'b7d0bfaa-3e1f-499e-ad13-a2836c0dc0af'}

{'type': 'text', 'text': '{"returncode":0,"stdout":"✔ Syntax OK\\n","stderr":""}', 'uuid': 'a81e2ee4-b9c8-4b41-af04-e4513be73797'}

{'type': 'text', 'text': '{"returncode":0,"stdout":"done\\n","stderr":""}', 'uuid': 'c8a84520-f6e2-4999-be7c-1e3a065275df'}

{'type': 'local_resource', 'file_path': '/mnt/user-data/outputs/obsidian_vault_setup.sh', 'name': 'obsidian vault setup', 'mime_type': 'text/x-sh', 'uuid': 'eb247f42-6d2d-4377-be92-28c578c5c3be'}
Here's your complete vault setup script. Here's what it does, top to bottom:

**What the script builds:**

- **Vault folder structure** — 10 organized folders (Inbox, Daily Notes, Research, AI Conversations, OSINT, Finance, Career, etc.) inside your existing vault path
- **Obsidian configs** — `app.json`, `hotkeys.json`, `appearance.json`, `core-plugins.json`, `daily-notes.json` — all pre-configured
- **Plugin data files** — Pre-configured `data.json` for Local GPT, Smart Connections, Templater, and Dataview so they work with Ollama immediately on install
- **Local GPT actions** — 8 custom AI actions (Summarize, Generate Tags, Find Connections, Research Expand, Devil's Advocate, Zettelkasten convert, Action Items, Ask About This) with a system prompt that knows your interests
- **CSS theme** — Dark monolith aesthetic: `#0d0d0d` background, amber (`#e8a838`) accent, JetBrains Mono + Syne fonts, styled headings/tags/code/graph
- **4 templates** — Daily Note, Research Note, AI Chat, Literature Note
- **HOME.md dashboard** — Dataview queries for recent notes, AI chats, tag cloud
- **3 shell commands** — `vault-ollama-start`, `vault-ollama-stop`, `vault-status` (memory-optimized for 8GB RAM)
- **Autostart entry** — Ollama starts with your desktop session

**To run it:**
```bash
# Edit VAULT_PATH at the top first (line ~30)
nano obsidian_vault_setup.sh

# Then run
bash obsidian_vault_setup.sh
```

After running, open Obsidian, point it to your vault, then install the 8 plugins listed in `~/Desktop/VAULT_PLUGIN_INSTALL.md`. The configs are already waiting for them.

---
