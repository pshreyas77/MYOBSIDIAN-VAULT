---
title: GenericAgent Integration
description: GenericAgent AI assistant integrated with Obsidian Vault
date: 2026-04-20
tags: [AI, agent, automation, GenericAgent]
aliases: [GA Integrations, AI Agent]
---

# 🤖 GenericAgent - Obsidian Vault Integration

**Location:** `/home/sunny77/Documents/Obsidian Vault/genericagent/`

> Self-evolving autonomous agent with **~3K lines** of core code

---

## Quick Links

| Resource | Path |
|----------|------|
| **Main Script** | `genericagent/agentmain.py` |
| **GUI Launcher** | `genericagent/launch.pyw` |
| **Configuration** | `genericagent/mykey.py` |
| **Integration Guide** | `genericagent/INTEGRATION_GUIDE.md` |
| **Qwen Wrapper** | `genericagent/qwen_agent_wrapper.py` |

---

## Core Features

- 🧠 **Self-Evolving:** Crystallizes each task into reusable skills
- 🌐 **Browser Control:** CDP-based web automation with session preservation
- 💻 **System Control:** Terminal, files, mouse, keyboard
- 📱 **Mobile Control:** ADB for Android devices
- 🔍 **Vision:** Screen capture and OCR
- ⚡ **<30K Context:** Highly efficient token usage

---

## The 9 Atomic Tools

| Tool | Purpose | Example |
|------|---------|---------|
| `bash` | Terminal commands | `ls -la`, `pip install` |
| `python` | Code execution | Data processing scripts |
| `browser` | Web automation | Login, scraping, navigation |
| `file` | File operations | Read, write, delete |
| `mouse` | Cursor control | Click, drag, position |
| `keyboard` | Input simulation | Type, hotkey combinations |
| `vision` | Screen analysis | OCR, element detection |
| `adb` | Android control | App automation, screenshots |
| `code` | VS Code integration | Open files, run commands |

---

## Usage Commands

### CLI Mode
```bash
cd "/home/sunny77/Documents/Obsidian Vault/genericagent"
python agentmain.py
```

### GUI Mode
```bash
python launch.pyw
```

### Python Integration
```python
import sys
sys.path.insert(0, "/home/sunny77/Documents/Obsidian Vault/genericagent")
from qwen_agent_wrapper import QwenGenericAgent

agent = QwenGenericAgent()
agent.run_task("Find all Markdown files")
```

---

## Skill System

Tasks are automatically crystallized into reusable skills:

```
[Task] → [Auto-Explore] → [Crystallize] → [Skill Saved]
                              ↓
                    [Reusable on Similar Tasks]
```

Check skills: `python qwen_agent_wrapper.py --list-skills`

---

## Related Topics

- [[02 - AREAS/02 AI & Technology/00_AI & Technology MOC]]
- [[00_OBSIDIAN-SECOND-BRAIN-SETUP]]
- [[00_OBSIDIAN RESEARCH SKILLS HUB]]

---

*GenericAgent: Minimal, Self-Evolving, Autonomous*


## 📂 Topic Clusters

- [[00_Agents_MOC|Agents]]
- [[00_Obsidian RAG System_MOC|Obsidian Rag System]]
- [[00_Other_MOC|Other]]
- [[00_Projects_MOC|Projects]]
- [[00_Research_MOC|Research]]
- [[00_ai_MOC|Ai]]
- [[00_career_MOC|Career]]
- [[00_communism_MOC|Communism]]
- [[00_data-science_MOC|Data-Science]]
- [[00_games_MOC|Games]]
- [[00_knowledge_MOC|Knowledge]]
- [[00_marvel-dc_MOC|Marvel-Dc]]
- [[00_movies_MOC|Movies]]
- [[00_os-systems_MOC|Os-Systems]]
- [[00_philosophy-comparison_MOC|Philosophy-Comparison]]
- [[00_power-scaling_MOC|Power-Scaling]]
- [[00_programming_MOC|Programming]]
- [[00_security_MOC|Security]]
- [[00_web-dev_MOC|Web-Dev]]
- [[00_year-2025_MOC|Year-2025]]
- [[00_year-2026_MOC|Year-2026]]
