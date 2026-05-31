---
title: "Cleaning up Obsidian's cluttered graph"
date: 2026-03-29
tags:
  - machine-learning
  - llm-ai
  - linux
  - obsidian
  - buddhism
  - stock-market
  - research
  - web-dev
  - game-design
source: claude-export
---

# Cleaning up Obsidian's cluttered graph

> **Conversation Overview**

The user, who goes by the username "sunny77" and runs Feren OS with an Intel i5-8350U processor and 8GB RAM, sought help optimizing their Obsidian graph view and setting up free, unlimited AI capabilities within Obsidian. Their vault is located at `/home/sunny77/Documents/Obsidian Vault/` and contains a research project called "BUDDHA" (referenced throughout as Buddha research or UCH research). They already had three community plugins installed: calendar, dataview, and terminal.

The conversation progressed through several technical stages. First, Claude diagnosed the cluttered graph view as likely caused by auto-generated links from plugins like Dataview, and provided graph settings adjustments. Then the user asked about free AI in Obsidian, and Claude recommended Local GPT and Smart Connections plugins configured with Ollama as the local backend. The Obsidian Terminal plugin was found to be broken (throwing a `TypeError: Cannot read properties of undefined (reading 'addSetting')` error), so the system terminal (Konsole) was used instead. Claude guided the user to locate their vault path using `find ~/ -name "*.obsidian" -type d`, navigate to `.obsidian/plugins/`, and install both plugins via `curl` commands. A mistake occurred where plugin folders were initially created in the vault root rather than `.obsidian/plugins/`, which was corrected using `mv` commands.

By the end of the conversation, both plugins were successfully installed and moved to the correct location. The user was revealed to already have Ollama installed with an extensive model list including `qwen2.5:1.5b`, `llama3.2:3b`, `nomic-embed-text:latest`, and several cloud models. Smart Connections was already showing semantic similarity scores in the right panel. Claude recommended using `nomic-embed-text` for Smart Connections embeddings and `llama3.2:3b` for Local GPT chat, with configuration pointing to `http://localhost:11434`. The final step of configuring Local GPT settings in Obsidian was pending at the conversation's end.

**Date:** 2026-03-29  
**Topics:** [[Machine-Learning]] · [[LLM-AI]] · [[Linux]] · [[Obsidian]] · [[Buddhism]] · [[Stock-Market]] · [[Research]] · [[Web-Dev]] · [[Game-Design]]

---

### 🧑 You

how to optimize my obsedian graph . it has so many links which i did not do

---

### 🤖 Claude

That's your Obsidian Graph View showing your Buddha research vault. The dense web with numbered nodes (1–86) suggests auto-generated links or a plugin is creating connections you didn't manually make.

Here's how to diagnose and clean it up:

**Find what's creating the extra links**

The numbered nodes are almost certainly from a plugin. Check:
- Settings → Community Plugins → look for **Dataview**, **Strange New Worlds**, or **Graph Analysis**
- These plugins can auto-resolve links or create implicit connections

**In Graph View settings (the gear icon top-right of graph)**

- Turn off **Tags** — tag co-occurrence creates phantom edges
- Turn off **Attachments** — images/PDFs show as nodes
- Reduce **Link distance** and increase **Repel force** to spread it out visually
- Use **Filters → Files** to show only specific folders

**The numbered nodes specifically**

Those look like **block references** (`^27`, `^12` etc.) being rendered as nodes. In Graph settings, toggle off **Show orphans** and check if a plugin like Breadcrumbs or Strange New Worlds is active.

**Quick cleanup steps:**

1. Open a numbered note (click node 27 for example) — see what it actually is
2. If they're auto-generated, disable the responsible plugin
3. Use **Groups** in graph settings to color-code by folder so the real structure is visible

What plugins do you have enabled? That'll pinpoint the culprit fast.

---

### 🧑 You

can i install any AI and use it for free unlimited in obsedian??

---

### 🤖 Claude

Yes, but with some nuance. Here are your best options given your setup (Ollama already running locally):

---

**Best option for you: Ollama + Smart Connections or Local GPT**

Since you already have Ollama running with qwen2.5, you're halfway there.

1. In Obsidian → Settings → Community Plugins → Browse
2. Search **"Local GPT"** or **"Smart Connections"**
3. Install → in plugin settings, set provider to **Ollama**, endpoint `http://localhost:11434`
4. Pick your model (qwen2.5:1.5b works on your 8GB RAM)

This gives you **truly free + unlimited + offline** AI inside Obsidian.

---

**What each plugin does**

| Plugin | Best for |
|---|---|
| **Local GPT** | Right-click any note → ask AI about it |
| **Smart Connections** | Semantic search across your whole vault, find related notes |
| **Copilot** | ChatGPT-style sidebar, supports Ollama |

---

**Free cloud options (limited)**

- **Copilot plugin** supports Gemini API — Google gives ~1500 free requests/day
- OpenRouter free tier also works with Copilot

---

**My recommendation for your Buddha research vault**

Go with **Smart Connections + Ollama**. It'll let you semantically search across all your research notes — ask things like *"what did I write about Gandharan iconography"* and it finds relevant notes automatically. Very powerful for your UCH research.

Want a step-by-step setup guide for Local GPT + Ollama?

---

### 🧑 You

guide me to setup this using obsedian terminal if it is possible??

---

### 🤖 Claude

Yes, absolutely possible! Let me give you the full guide.

---

## Step 1: Verify Ollama is Running

In Obsidian Terminal (the one you already have open), type:

```bash
ollama list
```
You should see your qwen2.5 model listed. Then:
```bash
curl http://localhost:11434/api/tags
```
If it returns JSON, Ollama is live. ✅

---

## Step 2: Pull a Good Model for Note Analysis

Your RAM supports these well:
```bash
# Lightweight but smart (recommended)
ollama pull qwen2.5:1.5b

# If you want slightly better reasoning
ollama pull llama3.2:1b
```

---

## Step 3: Install Plugins via Obsidian Terminal

The terminal in Obsidian runs in your **vault directory**. First confirm location:
```bash
pwd
```

Then navigate to plugins folder:
```bash
cd .obsidian/plugins
```

**Install Local GPT:**
```bash
mkdir local-gpt && cd local-gpt
curl -L https://github.com/pfrankov/obsidian-local-gpt/releases/latest/download/main.js -o main.js
curl -L https://github.com/pfrankov/obsidian-local-gpt/releases/latest/download/manifest.json -o manifest.json
curl -L https://github.com/pfrankov/obsidian-local-gpt/releases/latest/download/styles.css -o styles.css
cd ..
```

**Install Smart Connections:**
```bash
mkdir smart-connections && cd smart-connections
curl -L https://github.com/brianpetro/obsidian-smart-connections/releases/latest/download/main.js -o main.js
curl -L https://github.com/brianpetro/obsidian-smart-connections/releases/latest/download/manifest.json -o manifest.json
curl -L https://github.com/brianpetro/obsidian-smart-connections/releases/latest/download/styles.css -o styles.css
cd ..
```

---

## Step 4: Enable Plugins in Obsidian

After running the curl commands:

1. Press `Ctrl+,` → Community Plugins
2. Turn off **Safe Mode** if it's on
3. You'll see **Local GPT** and **Smart Connections** listed
4. Toggle both **ON**

---

## Step 5: Configure Local GPT

1. Settings → Local GPT
2. Set these:
```
Provider: Ollama
URL: http://localhost:11434
Model: qwen2.5:1.5b
```
3. Save

Now right-click any note → you'll see **Local GPT** context menu options like *Summarize*, *Continue writing*, *Ask anything*

---

## Step 6: Configure Smart Connections

1. Settings → Smart Connections
2. Set:
```
AI Provider: Ollama
Model: qwen2.5:1.5b
```
3. Click **Build Index** — it will scan your entire Buddha research vault

After indexing, open the Smart Connections panel (ribbon icon) and ask:
```
What did I write about Gandharan iconography?
What are my critical arguments about Buddha evidence?
```

---

## Troubleshooting

If curl fails in Obsidian Terminal:
```bash
# Check if you have internet
ping -c 2 google.com

# Alternative: use wget
wget -O main.js https://github.com/pfrankov/obsidian-local-gpt/releases/latest/download/main.js
```

If Ollama connection refused:
```bash
# Start Ollama manually
ollama serve &
```

---

Try **Step 1 first** and paste what you see — I'll help you proceed from there!

---

### 🧑 You

first how to open terminal in it??

---

### 🤖 Claude

Good question! Here are all the ways to open the terminal in Obsidian:

---

## Method 1: Ribbon Icon
Look at the **left sidebar icons** — there should be a **terminal/command prompt icon** `>_`
Click it → terminal opens

---

## Method 2: Command Palette (Easiest)
```
Ctrl + P
```
Type: `terminal` or `open terminal`
Click **"Terminal: Open Terminal"**

---

## Method 3: Right-Click in File Explorer
1. In the left panel, right-click any **folder**
2. You'll see **"Open Terminal"** in context menu
3. It opens terminal **in that folder's location** ✅

---

## Method 4: Hotkey (if set)
Check Settings → Community Plugins → Terminal → Hotkeys

---

## If You Don't See Terminal at All

That means the **Obsidian Terminal plugin isn't installed yet.**

Install it first:
1. `Ctrl + ,` → Community Plugins
2. Turn off Safe Mode
3. Click **Browse**
4. Search **"Terminal"** by Polyipseity
5. Install + Enable

---

## Verify It Worked

Once terminal opens you should see something like:
```
user@hostname:~/your-vault-path$
```

**Which method worked for you?** Or does the terminal plugin need to be installed first?

---

### 🧑 You

it is showing this when i try to open terminal

---

### 🤖 Claude

That error is a **plugin bug**, not a terminal issue.

```
TypeError: Cannot read properties of undefined (reading 'addSetting')
```

This means the **Terminal plugin is outdated** or incompatible with your current Obsidian version.

---

## Fix Steps

**Step 1: Update the Terminal plugin**
1. `Ctrl + ,` → Community Plugins
2. Click **Check for updates**
3. Update Terminal if available

---

**Step 2: If no update available — Reinstall it**
1. Community Plugins → find **Terminal**
2. Click **Uninstall**
3. Browse → search Terminal → **Reinstall**

---

**Step 3: If still broken — Use Obsidian's built-in approach**

Just use your **system terminal instead** — it works exactly the same:

On Feren OS, open terminal normally:
```
Ctrl + Alt + T
```
Then navigate to your vault:
```bash
cd ~/path-to-your-obsidian-vault
cd .obsidian/plugins
```

To find your vault path, in Obsidian:
- Bottom left → click **"Obsidian V..."** vault name
- It shows the full path

---

**Using system terminal is actually better** for installing plugins since it has full permissions and no plugin dependency issues.

Want to proceed with system terminal? Just find your vault path and we continue from Step 3 of the setup guide.

---

### 🧑 You

~ ⚡ main is  v1.0.0 via 寧 v1.3.10  v3.10.12  ❯ cd ~/path-to-your-obsidian-vault cd .obsidian/plugins bash: cd: /home/sunny77/path-to-your-obsidian-vault: No such file or directory bash: cd: .obsidian/plugins: No such file or directory ~ ⚡ main is  v1.0.0 via 寧 v1.3.10  v3.10.12  ❯

---

### 🤖 Claude

Haha, that was a placeholder path! Let's find your actual vault location.

---

## Find Your Vault Path

```bash
find ~/ -name "*.obsidian" -type d 2>/dev/null
```

Or look for your BUDDHA folder:
```bash
find ~/ -name "BUDDHA EVIDENCE*" 2>/dev/null
```

Or just list common locations:
```bash
ls ~/Documents
ls ~/Desktop
ls ~/ | grep -i obsidian
ls ~/ | grep -i buddha
ls ~/ | grep -i vault
```

---

Paste what you see and I'll give you the **exact cd command** to run. Your vault is somewhere on your system, we just need to locate it!

---

### 🧑 You

~ ⚡ main is  v1.0.0 via 寧 v1.3.10  v3.10.12  ❯ cd ~/path-to-your-obsidian-vault cd .obsidian/plugins bash: cd: /home/sunny77/path-to-your-obsidian-vault: No such file or directory bash: cd: .obsidian/plugins: No such file or directory ~ ⚡ main is  v1.0.0 via 寧 v1.3.10  v3.10.12  ❯ find ~/ -name "*.obsidian" -type d 2>/dev/null /home/sunny77/Documents/Obsidian Vault/.obsidian find ~/ -name "BUDDHA EVIDENCE*" 2>/dev/null ~ ⚡ main is  v1.0.0 via 寧 v1.3.10  v3.10.12 took 16s  ❯ find ~/ -name "BUDDHA EVIDENCE*" 2>/dev/null ~ ⚡ main is  v1.0.0 via 寧 v1.3.10  v3.10.12 took 2s  ❯ ls ~/Documents ls ~/Desktop ls ~/ | grep -i obsidian ls ~/ | grep -i buddha ls ~/ | grep -i vault 'Obsidian Vault'   perplexcia   The_48_Laws_of_Power_Simplified.pdf ~ ⚡ main is  v1.0.0 via 寧 v1.3.10  v3.10.12  ❯

---

### 🤖 Claude

Found it! Your vault is at `/home/sunny77/Documents/Obsidian Vault/`

---

## Now Run These Exactly:

```bash
cd "/home/sunny77/Documents/Obsidian Vault"
```
```bash
ls
```
Paste what you see (your notes/folders list), then:

```bash
cd .obsidian/plugins
ls
```

This confirms we're in the right place, then we install the AI plugins right there.

---

### 🧑 You

~ ⚡ main is  v1.0.0 via 寧 v1.3.10  v3.10.12  ❯ cd "/home/sunny77/Documents/Obsidian Vault" ~/Documents/Obsidian Vault ⚡ main  ❯ ls BUDDHA ~/Documents/Obsidian Vault ⚡ main  ❯ cd .obsidian/plugins ls calendar  dataview  terminal Obsidian Vault/.obsidian/plugins ⚡ main  ❯

---

### 🤖 Claude

Perfect! You're in the right place. You already have **dataview, calendar, terminal** installed.

Now let's install the AI plugins:

---

## Install Local GPT

```bash
mkdir local-gpt && cd local-gpt
```
```bash
curl -L "https://github.com/pfrankov/obsidian-local-gpt/releases/latest/download/main.js" -o main.js
```
```bash
curl -L "https://github.com/pfrankov/obsidian-local-gpt/releases/latest/download/manifest.json" -o manifest.json
```
```bash
curl -L "https://github.com/pfrankov/obsidian-local-gpt/releases/latest/download/styles.css" -o styles.css
```
```bash
cd ..
```

---

## Install Smart Connections

```bash
mkdir smart-connections && cd smart-connections
```
```bash
curl -L "https://github.com/brianpetro/obsidian-smart-connections/releases/latest/download/main.js" -o main.js
```
```bash
curl -L "https://github.com/brianpetro/obsidian-smart-connections/releases/latest/download/manifest.json" -o manifest.json
```
```bash
curl -L "https://github.com/brianpetro/obsidian-smart-connections/releases/latest/download/styles.css" -o styles.css
```
```bash
cd ..
```

---

Run them **one by one** and paste the output after each batch. Once done, we enable them in Obsidian settings!

---

### 🧑 You

should i install it in obsedian terminal??

---

### 🤖 Claude

**No!** Use your **system terminal** (the one you're already using — the one showing `sunny77`).

You're already in the right place:
```
Obsidian Vault/.obsidian/plugins ⚡ main ❯
```

Just **paste the commands directly there** one by one. 

The Obsidian terminal plugin is broken anyway (that error we saw). System terminal works perfectly and you're already navigated to the correct plugins folder.

So just continue right there and run:
```bash
mkdir local-gpt && cd local-gpt
```
That's the first command — go ahead!

---

### 🤖 Claude

I see the problem! The plugins got created in the **wrong folder** — they're in the vault root instead of `.obsidian/plugins/`.

Let me fix this:

---

## Move Plugins to Correct Location

```bash
mv local-gpt .obsidian/plugins/
mv smart-connections .obsidian/plugins/
```

Then verify:
```bash
ls .obsidian/plugins/
```

You should see:
```
calendar  dataview  terminal  local-gpt  smart-connections
```

---

## Then Reload Obsidian

Press `Ctrl + R` inside Obsidian (or close and reopen it), then:

1. `Ctrl + ,` → Community Plugins
2. You'll see **Local GPT** and **Smart Connections** listed
3. Toggle both **ON**

---

Also I notice the `main.js` for smart-connections was never downloaded! After moving, run:

```bash
cd .obsidian/plugins/smart-connections
curl -L "https://github.com/brianpetro/obsidian-smart-connections/releases/latest/download/main.js" -o main.js
```

Then go back:
```bash
cd ../../..
```

Run the `mv` commands first and paste the output!

---

### 🧑 You

~/Documents/Obsidian Vault ⚡ main  ❯ mv local-gpt .obsidian/plugins/ mv smart-connections .obsidian/plugins/ ~/Documents/Obsidian Vault ⚡ main  ❯ ls .obsidian/plugins/ ``` You should see: ``` calendar  dataview  terminal  local-gpt  smart-connections calendar  dataview  local-gpt  smart-connections  terminal You: command not found Command 'calendar' not found, but can be installed with: sudo apt install calendar ~/Documents/Obsidian Vault ⚡ main  ❯ cd .obsidian/plugins/smart-connections curl -L "https://github.com/brianpetro/obsidian-smart-connections/releases/latest/download/main.js" -o main.js  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current                                 Dload  Upload   Total   Spent    Left  Speed  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0 100  933k  100  933k    0     0   855k      0  0:00:01  0:00:01 --:--:--  855k .obsidian/plugins/smart-connections ⚡ main via ⬡ v20.20.1 took 1s  ❯ cd ../../.. ~/Documents/Obsidian Vault ⚡ main  ❯

---

### 🤖 Claude

Everything is installed correctly! All 5 plugins are in place. ✅

Now just **reload Obsidian**:

---

## In Obsidian

1. Press `Ctrl + R` to reload
2. Go to `Ctrl + ,` → **Community Plugins**
3. Scroll down and **enable both:**
   - ✅ Local GPT
   - ✅ Smart Connections

---

## Configure Local GPT for Ollama

Once enabled:
1. Settings → **Local GPT** → click settings icon
2. Set:
```
Provider: Ollama
URL: http://localhost:11434
Model: qwen2.5:1.5b
```

---

## Configure Smart Connections

1. Settings → **Smart Connections**
2. Set AI provider to **Ollama**
3. Click **Build Index** to scan your Buddha vault

---

## Test It

Right-click any note in your vault → you should see **Local GPT** options like:
- Summarize
- Continue writing  
- Ask anything about this note

Let me know what you see after enabling them in Obsidian!

---

### 🧑 You

still not getting how to use it

---

### 🤖 Claude

I can see two important things from your screenshots:

1. **Smart Connections is working!** ✅ — Right panel shows related notes with similarity scores (0.86, 0.85, 0.83...) — that's already working!
2. **Ollama is not found** in the Obsidian terminal — because it's a different shell (`sh-5.3$` not your zsh)

---

## Two Things To Do

### 1. First — Install Ollama properly

In your **system terminal (Konsole)** run:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
Then:
```bash
ollama serve &
ollama pull qwen2.5:1.5b
```

---

### 2. Configure Local GPT in Obsidian

1. `Ctrl + ,` → Community Plugins → find **Local GPT** → click the **gear icon**
2. Set:
```
Provider: Ollama
URL: http://localhost:11434
Model: qwen2.5:1.5b
```

---

### 3. How to USE Smart Connections (already working!)

Look at your **right panel** — those are already semantic matches! To use the chat:
- Click the **chat bubble icon** in the left ribbon
- Or `Ctrl + P` → type **Smart Connections: Open Chat**

---

### 4. How to USE Local GPT

- Open any note
- Select some text
- Right-click → **Local GPT** → choose action

Smart Connections is already running Sunny — you're further along than you think! 🎉

---

### 🧑 You

.:++++++++//////////-           Icons: WhiteSur-dark [GTK2/3]               `-++++++---:::://///.         Terminal: konsole             `.:///+++.             `        Terminal Font: JetBrains Mono 10            `.........                       CPU: Intel i5-8350U (8) @ 3.600GHz                                            GPU: Intel UHD Graphics 620                                            Memory: 3178MiB / 7785MiB                                                                                                                                        ~ ⚡ main is  v1.0.0 via 寧 v1.3.10  v3.10.12  ❯ ollama list NAME                            ID              SIZE      MODIFIED     qwen2.5:1.5b                    65ec06548149    986 MB    5 days ago      lfm2.5-thinking:1.2b            95bd9d45385f    731 MB    10 days ago     nomic-embed-text:latest         0a109f422b47    274 MB    11 days ago     llama3.2:3b                     a80c4f17acd5    2.0 GB    12 days ago     llama3.2:latest                 a80c4f17acd5    2.0 GB    2 weeks ago     starcoder2:3b                   9f4ae0aff61e    1.7 GB    2 weeks ago     mistral:7b-instruct             6577803aa9a0    4.4 GB    2 weeks ago     nemotron-3-super:cloud          be3943c5a818    -         2 weeks ago     deepseek-v3.1:671b-cloud        d3749919e45f    -         2 weeks ago     nemotron-3-nano:30b-cloud       01d0d069a149    -         2 weeks ago     qwen3.5:cloud                   a7bf6f7891c3    -         2 weeks ago     gemini-3-flash-preview:cloud    ebade0d31690    -         2 weeks ago     minimax-m2.5:cloud              c0d5751c800f    -         2 weeks ago     dolphin-phi-small:latest        45d0fe5503b3    1.8 GB    3 weeks ago     dolphin-phi:2.7b-v2.6-q4_K_M    cff9506fc46b    1.8 GB    3 weeks ago     kimi-k2.5:cloud                 6d1c3246c608    -         3 weeks ago     glm-4.7:cloud                   023608864819    -         4 weeks ago     mistral-large-3:675b-cloud      3130fd5a5a1e    -         4 weeks ago     kimi-k2-thinking:cloud          9752ffb77f53    -         4 weeks ago     tinydolphin:latest              0f9dd11f824c    636 MB    5 weeks ago     ~ ⚡ main is  v1.0.0 via 寧 v1.3.10  v3.10.12  ❯

---

### 🤖 Claude

Wow, you have an amazing model list! And Ollama is already installed and running perfectly. 🎉

I can see you even have **cloud models** (gemini-3-flash-preview, deepseek-v3.1, etc.)!

---

## Now Configure Local GPT in Obsidian

`Ctrl + ,` → Community Plugins → **Local GPT** → gear icon ⚙️

Set these:
```
Provider: Ollama
URL: http://localhost:11434
Model: llama3.2:3b
```
*(llama3.2:3b is best balance for your RAM)*

---

## For Smart Connections

`Ctrl + ,` → **Smart Connections** → settings:
```
Embedding model: nomic-embed-text
```
You already have `nomic-embed-text:latest` installed — this is **perfect** for Smart Connections, it's literally designed for semantic search!

Then click **Build Index** — it will scan your entire Buddha vault.

---

## Best Models to Use for Each Task

| Task | Best Model from your list |
|---|---|
| Note chat / Q&A | `llama3.2:3b` |
| Fast responses | `qwen2.5:1.5b` |
| Embeddings | `nomic-embed-text` |
| Deep reasoning | `gemini-3-flash-preview:cloud` *(needs internet)* |

---

Go to Local GPT settings now and paste a screenshot — let's get it connected!

---
