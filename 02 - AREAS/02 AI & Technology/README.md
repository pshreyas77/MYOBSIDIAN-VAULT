# J.A.R.V.I.S. - FREE VERSION

**Just A Rather Very Intelligent System**

A personal AI assistant living in your Obsidian vault, powered by completely **free** local AI.

![Free](https://img.shields.io/badge/Cost-%24%200-4CAF50)
![Ollama](https://img.shields.io/badge/Backend-Ollama-blue)
![Obsidian](https://img.shields.io/badge/Knowledge-Obsidian-purple)

---

## ✨ Features

| Feature | Status | Free? |
|---------|--------|-------|
| **Local AI** | ✅ Ollama | ✅ 100% Free |
| **Vault Search** | ✅ Read/Write notes | ✅ Free |
| **Voice (Optional)** | ✅ STT + TTS | ✅ Free |
| **Long-term Memory** | ✅ JSON-based | ✅ Free |
| **12 Built-in Tools** | ✅ Search, write, execute | ✅ Free |

---

## 🚀 Quick Start

```bash
# 1. Go to project in your vault
cd "/home/sunny77/Documents/Obsidian Vault/projects/jarvis"

# 2. Run setup (installs everything)
bash setup.sh

# 3. Configure Obsidian plugin (see below)

# 4. Launch JARVIS
python main.py
```

---

## 📁 File Structure

```
Obsidian Vault/
└── projects/
    └── jarvis/
        ├── main.py              # Entry point
        ├── llm_client.py        # Universal LLM client (NEW)
        ├── obsidian_client.py   # Vault integration
        ├── config.py            # Settings (Updated for FREE)
        ├── tools.py             # 12 built-in tools
        ├── audio_handler.py     # Voice I/O
        ├── claude_client.py     # Anthropic client (fallback)
        ├── requirements.txt     # Dependencies
        ├── setup.sh             # One-click install (Updated)
        ├── jarvis.sh            # Quick launcher
        ├── .env.example         # Configuration template (Updated)
        ├── SETUP.md             # Detailed setup guide
        └── README.md            # This file
```

---

## 🔧 Backends (All Free Options)

### Option 1: OLLAMA (Recommended ⭐)

**Completely free**, runs locally on your computer.

```bash
# Install Ollama (one-time)
curl -fsSL https://ollama.com/install.sh | sh

# Download model (~3GB)
ollama pull llama3.2

# Start server
ollama serve
```

No API keys. No costs. 100% private.

### Option 2: NVIDIA Free Tier

```bash
# Get key: https://build.nvidia.com
# Edit .env:
OLLAMA_ENABLED=false
OPENAI_API_KEY=nvapi-xxxx
OPENAI_BASE_URL=https://integrate.api.nvidia.com/v1
```

### Option 3: DeepSeek Free Tier

```bash
# Get key: https://platform.deepseek.com
# Edit .env:
OLLAMA_ENABLED=false
OPENAI_API_KEY=sk-xxxx
OPENAI_BASE_URL=https://api.deepseek.com/v1
```

### Option 4: Anthropic (Only if you have credits)

```bash
# Not FREE - only if you already have API access
ANTHROPIC_API_KEY=sk-ant-...
```

---

## 🔌 Obsidian Integration

1. Open Obsidian → Settings → Community Plugins
2. Turn off Safe Mode
3. Search **"Local REST API"**
4. Install & Enable
5. Copy API key → paste in `.env`

JARVIS now has full access to your vault.

---

## 💬 Usage Examples

```
> search Buddhism meditation
Found 3 notes about Buddhism...

> read notes/tibetan philosophy
[Shows note content]

> create daily note about my research
Added to today's note.

> what do I know about ancient civilizations?
[AI searches vault and provides answer]

> status
Backend: Ollama (llama3.2)
Vault: 21,228 notes
```

---

## Available Tools

| Tool | Description |
|------|-------------|
| `search_vault` | Search notes by content |
| `read_note` | Read specific note |
| `write_note` | Create new note |
| `create_daily_note` | Add to daily log |
| `get_vault_stats` | Show vault info |
| `execute_command` | Safe shell commands |
| `open_website` | Open URLs |
| `get_current_time` | Date/time |
| `list_recent_notes` | Recently modified |
| `find_related_notes` | Topic-based search |

---

## 🎤 Voice Mode (Optional)

Set in `.env`:
```
VOICE_ENABLED=true
TEXT_TO_SPEECH_ENABLED=true
```

Requirements:
```bash
sudo apt install python3-pyaudio portaudio19-dev espeak
```

Run with voice:
```bash
python main.py --voice
```

---

## 📊 Performance (Free Backends)

| Setup | RAM | Speed | Cost |
|-------|-----|-------|------|
| llama3.2 | 4GB | Fast | **$0** |
| mistral | 6GB | Medium | **$0** |
| qwen2.5 | 6GB | Medium | **$0** |

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Ollama not found | `curl -fsSL https://ollama.com/install.sh \| sh` |
| Out of memory | Use `phi4` model (smaller) |
| No audio | Install `portaudio19-dev espeak` |
| Obsidian error | Check Local REST API plugin + key |
| Import errors | Run `pip install -r requirements.txt` |

---

## 🤖 Architecture

```
┌────────────────────────────────────────────────────────┐
│                      J.A.R.V.I.S.                       │
├────────────────────────────────────────────────────────┤
│  ┌────────────┬──────────────┬────────────────────┐  │
│  │  Ollama    │   Obsidian   │     Audio          │  │
│  │  (Local)   │   Client     │     Handler        │  │
│  └─────┬───────┴─────┬────────┴─────────┬──────────┘  │
│        │             │                  │             │
│        └─────────────┼──────────────────┘             │
│                      │                                │
│              ┌───────┴───────┐                       │
│  ┌──────────┴───────────┐  │                       │
│  │ Universal LLM Client │  │                       │
│  │  (Ollama/Claude/    │  │                       │
│  │   OpenAI)            │  │                       │
│  └───────────┬──────────┘  │                       │
│              │             │                        │
│      ┌───────┴───────┐   │                       │
│      │   Tool        │   │                       │
│      │   Registry    │   │                       │
│      └───────┬───────┘   │                       │
│              │             │                        │
│      ┌───────┴───────┐   │                       │
│      │    main.py    │   │                       │
│      │   (JARVIS)    │   │                       │
│      └───────────────┘   │                       │
└──────────────────────────────────────────────────────┘
```

---

## 📄 License

MIT - Personal use only.

---

**"At your service, Sir."** - J.A.R.V.I.S.

Built with ❤️ for Obsidian + Free local AI