# J.A.R.V.I.S. - Run Later Instructions

**Created:** 2026-04-19
**Location:** `/home/sunny77/Documents/Obsidian Vault/projects/jarvis/`

---

## Quick Start (When You're Ready)

### Step 1: Open Terminal

```bash
cd "/home/sunny77/Documents/Obsidian Vault/projects/jarvis"
```

### Step 2: Run Setup (First Time Only)

```bash
bash setup.sh
```

This will:
- Install Python dependencies
- Check for Ollama (free local AI)
- Configure your vault path
- Create `.env` file

### Step 3: Configure Obsidian Plugin

1. Open Obsidian → Settings → Community Plugins
2. Search **"Local REST API"**
3. Install & Enable
4. Copy the API key
5. Edit `.env` file and paste the key:
   ```
   OBSIDIAN_API_KEY=your-key-here
   ```

### Step 4: Launch JARVIS

```bash
# Option A: Quick launch
./jarvis.sh

# Option B: Manual
source venv/bin/activate
python main.py

# Option C: With voice
python main.py --voice
```

---

## Prerequisites Checklist

Before running, ensure you have:

- [ ] Python 3.8+ installed
- [ ] Ollama installed (for free local AI)
- [ ] Obsidian Local REST API plugin enabled
- [ ] `.env` file configured

---

## Install Ollama (One-Time)

If not already installed:

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Download AI model (~3GB)
ollama pull llama3.2

# Start server (keep running)
ollama serve
```

---

## Basic Commands

Once JARVIS is running:

```
search Buddhism meditation      # Search your vault
read notes/tibetan philosophy  # Read a note
create note about research     # Create new note
what time is it?              # Get time
status                         # System status
help                           # Show all commands
exit                           # Quit
```

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| "Ollama not found" | Run `ollama serve` in another terminal |
| "Module not found" | Run `pip install -r requirements.txt` |
| "Obsidian API error" | Check Local REST API plugin & key |
| Out of memory | Use smaller model: `ollama pull phi4` |

---

## Files Reference

| File | Purpose |
|------|---------|
| `main.py` | Start JARVIS |
| `setup.sh` | Install dependencies |
| `jarvis.sh` | Quick launcher |
| `.env` | Configuration |
| `SETUP.md` | Detailed guide |
| `README.md` | Full documentation |

---

## Backend Options

**Default (Recommended):** Ollama (local, free)

**Alternatives** (edit `.env`):
- NVIDIA Free Tier
- DeepSeek Free Tier
- Anthropic (paid)

---

**Your JARVIS is ready when you are!**

Just run: `cd "/home/sunny77/Documents/Obsidian Vault/projects/jarvis" && ./jarvis.sh`