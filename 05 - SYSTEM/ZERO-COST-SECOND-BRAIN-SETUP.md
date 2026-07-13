# Zero-Cost Second Brain Setup Guide

**Your complete, fully automatic second brain. Total cost: ₹0/month. Total time: ~20 min setup, then zero effort forever.**

---

## What You're Building

```
Phone/Telegram → Hermes Agent → 0-raw/ → Night Shift → Obsidian vault
                                                              ↓
Morning (06:30) ← Hermes Agent ← briefing ← Editor (06:00) ←
```

Every capture automatically:
1. Gets filed to the right place
2. Has atoms extracted
3. Gets linked to existing knowledge
4. Appears in your morning synthesis
5. Surfaces contradictions and patterns

---

## STEP 1: Install Obsidian Plugin (5 min)

**You need to do this in the Obsidian app** (I can't install desktop plugins for you).

1. Open Obsidian
2. Settings → Community Plugins → Browse
3. Search: **Local REST API**
4. Install `obsidian-local-rest-api` by @coddingtonbear
5. Enable it: Settings → Local REST API
6. **Copy the API key** (you'll need it in Step 2)
7. Enable: "Allow HTTP" (for local network)

✅ Plugin URL: `community.obsidian.md/plugins/obsidian-local-rest-api`
✅ Repo: `github.com/coddingtonbear/obsidian-local-rest-api`

---

## STEP 2: Connect Hermes to Obsidian (2 min)

Once the plugin is running in Obsidian, connect Hermes:

```bash
hermes mcp add obsidian \
  --transport http \
  --url https://127.0.0.1:27124/mcp/ \
  --header "Authorization: Bearer YOUR_API_KEY_HERE"
```

Replace `YOUR_API_KEY_HERE` with the key from Step 1.

Test it:
```bash
hermes mcp test obsidian
```

---

## STEP 3: Set Up Telegram Capture (10 min — if not already done)

**Already done if you have the Telegram bot running.**

If you need a new bot:
1. Open Telegram → message `@BotFather`
2. Send: `/newbot`
3. Follow prompts → get `BOT_TOKEN`
4. Run: `hermes gateway setup telegram`
5. Paste the token

**Verify it's working:**
```bash
hermes send --platform telegram --chat 8336840601 "Second brain connected. Test capture: /capture Hello from the new system!"
```

---

## STEP 4: Set Up Night Shift Pipeline (Already Done ✅)

Your Night Shift pipeline is already installed and working:
- ✅ `playbooks/scout-run.ps1` (23:30 daily)
- ✅ `playbooks/refinery-run.ps1` (03:00 daily)
- ✅ `playbooks/editor-run.ps1` (06:00 daily)

To verify:
```bash
cd 'E:\_Knowledge\ObsidianVault'
bash playbooks/verify_hermes_obsidian_loop.sh
```

---

## STEP 5: Configure Daily Synthesis (Auto — Already Set)

Every morning at 06:00, the Editor run generates a **Morning Brief** in `briefings/YYYY-MM-DD - Morning Brief.md`. 

Your Hermes agent reads this and synthesizes it.

If you want a dedicated morning synthesis cron, add:
```
/capture Morning brief for [DATE]: summarize last 24h captures, find patterns, surface contradictions
```

---

## Complete Capture Commands

| Command | Goes To | Use When |
|---------|---------|----------|
| `/capture [thought]` | 0-raw/ | Quick ideas, insights |
| `/capture [url] + [commentary]` | 0-raw/sources/ | Articles, links |
| `/book [quote] — [author]. [reaction]` | 1-desk/book/ | Book notes |
| `/note [quick note]` | 04 - DAILY/YYYY-MM-DD.md | Daily append |
| `/question [question]` | 2-atoms/questions/ | Open questions |

---

## Quick Test (Do This Now)

1. **Open Obsidian** → make sure Local REST API plugin is enabled
2. **Send from Telegram:**
   ```
   /capture Test: The Kikkuli tablet is the oldest horse training manual AND the oldest written text from Anatolia.
   ```
3. **Wait 6 hours** OR manually run:
   ```bash
   cd 'E:\_Knowledge\ObsidianVault'
   pwsh playbooks/scout-run.ps1 -VaultPath "E:\_Knowledge\ObsidianVault"
   pwsh playbooks/refinery-run.ps1 -VaultPath "E:\_Knowledge\ObsidianVault"
   pwsh playbooks/editor-run.ps1 -VaultPath "E:\_Knowledge\ObsidianVault"
   ```
4. **Check results:**
   - `0-raw/` → file should be there
   - `2-atoms/concepts/` → atom should exist
   - `briefings/` → morning brief updated

---

## Troubleshooting

### "Telegram bot not responding"
```bash
hermes gateway status
# If down: hermes gateway start
```

### "Capture goes to Telegram but not to vault"
```bash
# Check logs
grep -i error ~/.hermes/logs/gateway.log | tail -10
# Run sync doctor
bash playbooks/verify_hermes_obsidian_loop.sh
```

### "Morning brief empty"
- Check `briefings/` directory exists
- Run Scout manually: `pwsh playbooks/scout-run.ps1 -VaultPath "E:\_Knowledge\ObsidianVault"`

---

## What Makes This Zero Cost

| Tool | Cost |
|------|------|
| Obsidian | Free (local) |
| Hermes Agent | Free (open source) |
| Telegram Bot | Free |
| Cloud AI (your current) | Already paying for it |
| Local faster-whisper (STT) | Free |

The only cost is your existing cloud AI API — which you already have.

---

## The Compounding Effect

| Time | What Happens |
|------|-------------|
| **Week 1** | Pipeline working. You capture randomly. |
| **Week 2** | First patterns appear in morning briefs. |
| **Week 3** | Hermes finds contradictions between notes. |
| **Month 2** | You stop re-reading things you already read. |
| **Month 3** | The vault starts suggesting connections you'd miss. |
| **Month 6** | The graph knows your thinking better than you do. |

This is the actual moat. Not the tools. The accumulated context.