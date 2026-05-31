# J.A.R.V.I.S. Setup Guide - FREE VERSION

Complete guide to setting up your free JARVIS assistant using Ollama or other free APIs.

## Quick Start (30 seconds)

```bash
# 1. Navigate to the project
cd "/home/sunny77/Documents/Obsidian Vault/projects/jarvis"

# 2. Run setup
bash setup.sh

# 3. Edit .env and add Obsidian API key

# 4. Launch JARVIS
source venv/bin/activate
python main.py
```

## Detailed Setup

### Prerequisites

- Python 3.8+
- Linux/macOS (tested on Ubuntu)
- Obsidian vault

### Option 1: OLLAMA (Recommended - Completely FREE)

Ollama runs AI models **locally on your computer** - no API keys needed, no costs!

#### Step 1: Install Ollama (One-time)

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Verify installation
ollama --version
```

#### Step 2: Download a Model (One-time)

```bash
# Recommended: llama3.2 (fast, good quality)
ollama pull llama3.2

# Alternatives:
# ollama pull mistral      # Better reasoning
# ollama pull qwen2.5      # Multilingual
# ollama pull phi4         # Smaller/faster
```

#### Step 3: Start Ollama Server

```bash
# Start the server (keep running in background)
ollama serve

# Or run in background:
nohup ollama serve &
```

#### Step 4: Run JARVIS

```bash
cd "/home/sunny77/Documents/Obsidian Vault/projects/jarvis"
source venv/bin/activate
python main.py
```

That's it! JARVIS will automatically detect and use Ollama.

---

### Option 2: NVIDIA Free Tier

NVIDIA offers free API credits for testing.

1. Sign up: https://build.nvidia.com
2. Get API key from your account
3. Edit `.env`:
   ```
   OLLAMA_ENABLED=false
   OPENAI_API_KEY=nvapi-your-key
   OPENAI_BASE_URL=https://integrate.api.nvidia.com/v1
   OPENAI_MODEL=nvidia/llama-3.1-nemotron-70b-instruct
   ```
4. Run JARVIS

---

### Option 3: DeepSeek (Free Tier)

DeepSeek offers free API tier with generous limits.

1. Sign up: https://platform.deepseek.com
2. Get API key
3. Edit `.env`:
   ```
   OLLAMA_ENABLED=false
   OPENAI_API_KEY=sk-your-key
   OPENAI_BASE_URL=https://api.deepseek.com/v1
   OPENAI_MODEL=deepseek-chat
   ```

---

## Obsidian Integration

### Install Local REST API Plugin

JARVIS needs access to your Obsidian vault to search and create notes.

1. Open Obsidian
2. Go to **Settings → Community Plugins**
3. Turn off **Safe Mode**
4. Click **Browse**
5. Search for **"Local REST API"**
6. Install and **Enable**
7. In plugin settings, copy the **API Key**
8. Paste it in `.env`:
   ```
   OBSIDIAN_API_KEY=your-key-here
   ```

---

## Usage Examples

Once running, try these commands:

```
# Search your vault
search Buddhism teachings

# Read a specific note
read notes/meditation guide

# Create a daily note
create daily note about research findings

# Natural language
What do I know about ancient civilizations?

# Time
what time is it?

# Help
help
```

---

## Model Comparison

| Model | Size | Speed | Quality | Hardware |
|-------|------|-------|---------|----------|
| llama3.2 | 3GB | Fast | Good | 8GB RAM |
| mistral | 4GB | Medium | Better | 8GB+ RAM |
| qwen2.5 | 4GB | Medium | Excellent | 8GB+ RAM |

For slower/older computers, try:
```bash
ollama pull phi4  # Small and fast
```

---

## Troubleshooting

### Ollama not connecting

```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# Restart Ollama
ollama serve
```

### Out of memory

```bash
# Use smaller model
ollama pull phi4

# Edit .env
OLLAMA_MODEL=phi4
```

### Obsidian API not working

- Ensure Local REST API plugin is **Enabled**
- Check OBSIDIAN_API_KEY in `.env` matches plugin settings
- Make sure Obsidian is running

### Import errors

```bash
# Reinstall packages
cd "/home/sunny77/Documents/Obsidian Vault/projects/jarvis"
source venv/bin/activate
pip install -r requirements.txt
```

---

## Next Steps

- **Enable voice**: Set `VOICE_ENABLED=true` in `.env`
- **Add custom tools**: Edit `tools.py`
- **Customize personality**: Edit system prompt in `config.py`
- **Integrate with MemPalace**: Add your Memories plugin

Your JARVIS is now running **completely free** using local AI!