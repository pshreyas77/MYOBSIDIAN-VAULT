---
title: "System storage usage scanner script"
date: 2026-03-20
tags:
  - machine-learning
  - llm-ai
  - data-analysis
  - linux
  - stock-market
  - creative
  - web-dev
  - game-design
source: claude-export
---

# System storage usage scanner script

> **Conversation Overview**

The person is a Feren OS user who needed help analyzing and reclaiming disk storage space on their system. They requested a Bash script to scan total system storage usage and identify where space was being consumed most heavily, with the intent to copy and paste it directly into their terminal.

Claude created a comprehensive interactive Bash script (`storage_scan.sh`) that scans multiple storage categories including disk partitions, top directories by size, home folder breakdown, APT package cache, Snap packages, Flatpak apps, installed kernels, trash, large files over 100MB, system logs, and Docker storage if present. The script uses color-coded output with visual usage bars and includes a built-in cleanup cheatsheet with ready-to-run commands.

After the person ran the script, Claude analyzed the results and identified the primary culprit as approximately 151GB of orphaned temporary git pack files located at `~/.local/share/opencode/snapshot/`, left behind by an interrupted opencode AI coding session. Claude provided a prioritized breakdown of all space consumers including Ollama models (~12GB), Flatpak apps including Alpaca (~9.4GB total), a local llama model file (~1.9GB), llama.cpp directory (~1.4GB), an Arch Linux ISO (~1.5GB), old kernels, APT cache, and trash. Claude then provided a consolidated one-shot cleanup command sequence addressing all major issues, estimating the cleanup would reduce disk usage from approximately 62% to around 28% used, with the opencode snapshot deletion alone recovering the majority of space.

**Date:** 2026-03-20  
**Topics:** [[Machine-Learning]] · [[LLM-AI]] · [[Data-Analysis]] · [[Linux]] · [[Stock-Market]] · [[Creative]] · [[Web-Dev]] · [[Game-Design]]

---

### 🧑 You

write  me an script to scan my total system storage used and where it is used more so that i can clear it for my feren os i will copy and paste script their

---

### 🤖 Claude

{'type': 'text', 'text': '     1\t---\n     2\tname: frontend-design\n     3\tdescription: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.\n     4\tlicense: Complete terms in LICENSE.txt\n     5\t---\n     6\t\n     7\tThis skill guides creation of distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. Implement real working code with exceptional attention to aesthetic details and creative choices.\n     8\t\n     9\tThe user provides frontend requirements: a component, page, application, or interface to build. They may include context about the purpose, audience, or technical constraints.\n    10\t\n    11\t## Design Thinking\n    12\t\n    13\tBefore coding, understand the context and commit to a BOLD aesthetic direction:\n    14\t- **Purpose**: What problem does this interface solve? Who uses it?\n    15\t- **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, etc. There are so many flavors to choose from. Use these for inspiration but design one that is true to the aesthetic direction.\n    16\t- **Constraints**: Technical requirements (framework, performance, accessibility).\n    17\t- **Differentiation**: What makes this UNFORGETTABLE? What\'s the one thing someone will remember?\n    18\t\n    19\t**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work - the key is intentionality, not intensity.\n    20\t\n    21\tThen implement working code (HTML/CSS/JS, React, Vue, etc.) that is:\n    22\t- Production-grade and functional\n    23\t- Visually striking and memorable\n    24\t- Cohesive with a clear aesthetic point-of-view\n    25\t- Meticulously refined in every detail\n    26\t\n    27\t## Frontend Aesthetics Guidelines\n    28\t\n    29\tFocus on:\n    30\t- **Typography**: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend\'s aesthetics; unexpected, characterful font choices. Pair a distinctive display font with a refined body font.\n    31\t- **Color & Theme**: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes.\n    32\t- **Motion**: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Use Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions. Use scroll-triggering and hover states that surprise.\n    33\t- **Spatial Composition**: Unexpected layouts. Asymmetry. Overlap. Diagonal flow. Grid-breaking elements. Generous negative space OR controlled density.\n    34\t- **Backgrounds & Visual Details**: Create atmosphere and depth rather than defaulting to solid colors. Add contextual effects and textures that match the overall aesthetic. Apply creative forms like gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, and grain overlays.\n    35\t\n    36\tNEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character.\n    37\t\n    38\tInterpret creatively and make unexpected choices that feel genuinely designed for the context. No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices (Space Grotesk, for example) across generations.\n    39\t\n    40\t**IMPORTANT**: Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate code with extensive animations and effects. Minimalist or refined designs need restraint, precision, and careful attention to spacing, typography, and subtle details. Elegance comes from executing the vision well.\n    41\t\n    42\tRemember: Claude is capable of extraordinary creative work. Don\'t hold back, show what can truly be created when thinking outside the box and committing fully to a distinctive vision.\n    43\t', 'uuid': 'c6838d29-6e05-479a-954a-f207ac297e31'}
Here's a clean, interactive Bash script — just copy and paste it into your terminal:

{'type': 'text', 'text': 'File created successfully: /mnt/user-data/outputs/storage_scan.sh', 'uuid': '69421022-859b-4129-a65d-88bc161c9139'}

{'type': 'local_resource', 'file_path': '/mnt/user-data/outputs/storage_scan.sh', 'name': 'storage scan', 'mime_type': 'text/x-sh', 'uuid': 'fca649e3-1d20-4215-b760-3b97687284ea'}
Download the file above, or copy the script directly. Here's how to run it:

**Basic run (your home + accessible dirs):**
```bash
bash storage_scan.sh
```

**Full system scan (recommended — sees everything):**
```bash
sudo bash storage_scan.sh
```

---

**What it scans:**

| Section | What it shows |
|---|---|
| 📦 Disk Partitions | All mounted drives with usage bars |
| 📊 Root `/` Usage | Visual fill bar with used/free |
| 🔍 Top 15 Directories | Biggest space hogs system-wide |
| 🏠 Home Folder | Per-folder breakdown of `~/` |
| 📦 APT Cache | `/var/cache/apt` size + clean command |
| 📎 Snap Packages | Total snap size + old revisions |
| 📦 Flatpak | Size + unused runtime cleaner |
| 🧠 Old Kernels | Finds removable old kernels |
| 🗑 Trash | Trash folder size |
| 🐘 Large Files | Files >100MB anywhere on disk |
| 📋 Logs | `/var/log` breakdown + journal vacuum |
| 🧹 Cleanup Cheatsheet | Ready-to-run cleanup commands |

Since you're on an 8GB RAM machine with Feren OS, the APT cache, snap revisions, and old kernels are usually the quickest wins for reclaiming space.

---

### 🤖 Claude

Excellent scan results! Here's a full breakdown of what's eating your 270G and exactly what to do:

---

## 🚨 Critical Finding — `opencode` Temp Files: ~151G

This is the **#1 culprit** — corrupted/abandoned git pack temp files:
```
~/.local/share/opencode/snapshot/.../objects/pack/tmp_pack_*
```
These `tmp_pack_` files are clearly orphaned temporary files from an interrupted operation. **Safe to delete:**
```bash
rm -rf ~/.local/share/opencode/snapshot/
```
This alone frees **~151G**. That's more than half your used space.

---

## 📊 Full Breakdown & Actions

| What | Size | Action |
|---|---|---|
| `opencode` tmp pack files | **~151G** | `rm -rf ~/.local/share/opencode/snapshot/` |
| Ollama models (system) | **~12G** | `ollama list` → remove unused with `ollama rm <name>` |
| Flatpak total | **9.4G** | Remove Alpaca (2.3G) if unused + `flatpak uninstall --unused` |
| Flatpak - Alpaca app | **2.3G** | `flatpak uninstall com.jeffser.Alpaca` |
| `~/models/llama-3.2.gguf` | **1.9G** | Delete if duplicate of Ollama models |
| `~/llama.cpp/` | **1.4G** | Delete if you're using Ollama instead |
| Arch Linux ISO | **1.5G** | `rm ~/Downloads/archlinux-2026.02.01-x86_64.iso` |
| Old kernels (3 old) | **~1-1.5G** | `sudo apt autoremove --purge` |
| APT cache | **319M** | `sudo apt clean` |
| Trash | **20M** | `rm -rf ~/.local/share/Trash/files/* ~/.local/share/Trash/info/*` |

---

## ✅ One-shot Cleanup Command

Run this to get back ~165G+ in one go:

```bash
# 1. The big one — opencode orphaned temp files
rm -rf ~/.local/share/opencode/snapshot/

# 2. Remove Arch ISO if you don't need it
rm ~/Downloads/archlinux-2026.02.01-x86_64.iso

# 3. Old kernels + APT cleanup
sudo apt autoremove --purge && sudo apt clean

# 4. Flatpak unused runtimes
flatpak uninstall --unused

# 5. Trash + thumbnail cache
rm -rf ~/.local/share/Trash/files/* ~/.local/share/Trash/info/*
rm -rf ~/.cache/thumbnails/*

# 6. Journal logs
sudo journalctl --vacuum-time=7d
```

---

**After the `opencode` delete alone, you'll go from 62% → ~28% used.** The `opencode` snapshot directory looks like it was from an interrupted AI coding session that left huge pack files behind — nothing you need.

---
