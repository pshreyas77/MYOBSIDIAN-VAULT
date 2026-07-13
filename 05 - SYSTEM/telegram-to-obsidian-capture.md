---
name: telegram-to-obsidian-capture
description: Capture anything from Telegram and auto-file it into your Obsidian vault. Send a thought from your phone → it appears correctly filed in your vault. Powers the phone-to-vault loop.
trigger: "When you receive a Telegram message to process"
version: 1.0.0
tags: [capture, telegram, obsidian, zero-cost, automatic]
platforms: [telegram]
---

# Telegram to Obsidian Capture

**For Future Claude:** This skill turns messy Telegram input into perfectly filed Obsidian notes. Send anything from your phone — URLs, thoughts, quotes, links, voice notes (transcribed) — and this skill routes it to the right place in your vault.

## How It Works

```
Phone → Telegram → Hermes Agent → 0-raw/ → Night Shift → Filed in vault
```

**No manual organization. No naming. No filing. Just capture.**

---

## Capture Methods

### Quick Thought
```
/capture The real reason the Aryan migration theory keeps changing is that each new generation of archaeologists finds layers the previous one missed.
```

### URL + Commentary
```
/capture https://www.sciencedirect.com/science/article/harappa + The Harappa DNA study shows something different from what I believed last year. Need to update the Indus Valley page.
```

### Book Note
```
/book The Buddha in the Attic — Julie Otsuka. "We forgot the smell of their hair, the way they slept, the food they ate." This is exactly the feeling I tried to capture in my poem about grandmother.
```

### Question
```
/question Is the Mitanni treaty evidence of Vedic deities pre-dating the Vedic period, or does it prove Indo-Aryan presence in Mesopotamia? Need primary source.
```

### Daily Note Quick Add
```
/note Thought: The distinction between dharma and law isn't just semantic — dharma is context-dependent law, law aspires to be universal dharma.
```

---

## Routing Rules

| Prefix | Goes To | Example |
|--------|---------|---------|
| `/capture` | 0-raw/ | Raw captures for processing |
| `/book` | 1-desk/book/ | Book notes and quotes |
| `/note` | 04 - DAILY/YYYY-MM-DD.md | Daily note |
| `/question` | 2-atoms/questions/ | Open questions |
| `/url` | 0-raw/sources/ | External links for Scout to process |
| plain text | 0-raw/ | Unclassified — Refinery handles it |

---

## Processing Flow

1. **Telegram message arrives** → Hermes receives it
2. **This skill parses** the prefix and routes to correct location
3. **Message filed** to `0-raw/` or appropriate subfolder
4. **Night Shift takes over** at next scheduled run:
   - Scout (23:30): Creates atoms
   - Refinery (03:00): Extracts concepts, links to existing pages
   - Editor (06:00): Adds backlinks, updates MOCs
5. **Morning Brief** (06:30): Synthesizes everything into your daily briefing

---

## Telegram Bot Setup (Zero Cost)

If you don't have a Telegram bot yet:

1. Message @BotFather on Telegram: `/newbot`
2. Follow prompts — get your `BOT_TOKEN`
3. Run: `hermes gateway setup telegram`
4. Paste the bot token
5. Your bot is now connected to Hermes

**Cost: ₹0 forever** — Telegram has no fees for bots.

---

## Voice Notes

Voice messages are automatically:
1. Transcribed via Hermes STT (faster-whisper, free, local)
2. Treated as `/capture` — filed to 0-raw/
3. Processed through the same pipeline

---

## Confidence & Quality

| Input Quality | How It's Handled |
|---------------|-----------------|
| Perfect structure (`/capture`) | Direct → 0-raw/ |
| Messy unstructured | Filed to 0-raw/ → Refinery extracts atoms |
| Unclear routing | Filed to 0-raw/ → flagged for review |

The pipeline never loses data. Every capture goes somewhere.

---

## Quick Start

```bash
# 1. Set up Telegram bot (if not already done)
hermes gateway setup telegram

# 2. Test it works
/message @YourBotName hello

# 3. Send your first capture
/capture Just realized the Kikkuli tablet is the oldest horse training manual AND the oldest written text from Anatolia. Two firsts.
```

---

## Verification

To verify the loop is working:

1. Send `/capture Test message from Telegram` to your bot
2. Wait 6 hours (or trigger manually: `pwsh playbooks/scout-run.ps1`)
3. Check `0-raw/` — file should be there
4. Check `2-atoms/concepts/` — atom should be extracted
5. Check `briefings/` — should appear in morning brief

Run the sync doctor:
```bash
bash playbooks/verify_hermes_obsidian_loop.sh
```