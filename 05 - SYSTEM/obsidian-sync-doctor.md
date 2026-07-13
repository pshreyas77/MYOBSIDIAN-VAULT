---
name: obsidian-sync-doctor
description: Diagnose and fix the Hermes-to-Obsidian capture loop. Verifies the full pipeline: Telegram → Hermes → 0-raw/ → Scout → Refinery → Editor → Vault.
trigger: "Run when captures from Telegram don't appear in your vault"
version: 1.0.0
tags: [diagnostic, obsidian, sync, telegram, troubleshooting]
---

# Obsidian Sync Doctor

**For Future Claude:** This skill checks every link in the Hermes-to-Obsidian chain. If something breaks, run this and it tells you exactly where and why.

---

## Quick Check (Read-Only)

```bash
cd '/e/_Knowledge/ObsidianVault'
bash playbooks/verify_hermes_obsidian_loop.sh
```

This checks:
- [ ] Telegram bot is receiving messages
- [ ] Hermes is processing them
- [ ] Files appear in `0-raw/`
- [ ] Night Shift scripts are executable
- [ ] `briefings/` directory exists
- [ ] Daily notes are being created

---

## Deep Check (All Steps)

Run each script individually:

```powershell
# Step 1: Scout — scan inboxes
pwsh playbooks/scout-run.ps1 -VaultPath "E:\_Knowledge\ObsidianVault"

# Step 2: Refinery — extract atoms
pwsh playbooks/refinery-run.ps1 -VaultPath "E:\_Knowledge\ObsidianVault"

# Step 3: Editor — link and back-link
pwsh playbooks/editor-run.ps1 -VaultPath "E:\_Knowledge\ObsidianVault"
```

---

## What Each Stage Checks

| Stage | File | Checks |
|-------|------|--------|
| Telegram → Hermes | Gateway logs | `~/.hermes/logs/gateway.log` |
| Hermes → 0-raw/ | `0-raw/` directory | New files appear after capture |
| Scout | `briefings/` | Morning brief is created |
| Refinery | `2-atoms/` | New atoms extracted |
| Editor | `2-atoms/*/index.md` | Links and back-links added |

---

## Common Failures & Fixes

### "0-raw/ is empty after capture"
1. Check `~/.hermes/logs/gateway.log` for Telegram errors
2. Verify `capture` skill is loaded: `/skills`
3. Check the file may have been processed immediately (not queued)

### "No morning brief"
- Scout needs `briefings/` directory
- Run: `mkdir -p '/e/_Knowledge/ObsidianVault/briefings'`

### "Refinery creates no atoms"
- Check `1-desk/` has content
- Check `2-atoms/` subdirectories exist: `concepts/`, `people/`, `events/`
- Run: `mkdir -p '/e/_Knowledge/ObsidianVault/2-atoms/concepts' '/e/_Knowledge/ObsidianVault/2-atoms/people' '/e/_Knowledge/ObsidianVault/2-atoms/events'`

### "Editor adds no links"
- Run manually: `pwsh playbooks/editor-run.ps1`
- Check output for "Links Added: N"

### "PowerShell 7 errors"
- Fix: `Get-Date - $StartTime` → `((Get-Date) - $StartTime)` in all scripts
- Fix: multi-value switch cases must be split

---

## End-to-End Verification Test

```bash
# 1. Send test capture
echo "Test: /capture Verification test $(date)" | telegram-send -

# 2. Wait 30 seconds, check raw
ls -la '/e/_Knowledge/ObsidianVault/0-raw/'

# 3. Run pipeline manually
pwsh playbooks/scout-run.ps1 -VaultPath "E:\_Knowledge\ObsidianVault"
pwsh playbooks/refinery-run.ps1 -VaultPath "E:\_Knowledge\ObsidianVault"
pwsh playbooks/editor-run.ps1 -VaultPath "E:\_Knowledge\ObsidianVault"

# 4. Check atoms
ls '/e/_Knowledge/ObsidianVault/2-atoms/concepts/'

# 5. Check brief
cat '/e/_Knowledge/ObsidianVault/briefings/'$(date +%Y-%m-%d)' - Morning Brief.md'
```

---

## Auto-Health Cron

Set up a weekly diagnostic cron:

```
Every Sunday 11:00 → Run obsidian-sync-doctor → Report to 05 - OUTPUTS/
```