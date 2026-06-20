# Night Shift Quick Reference

## Overview
Automated knowledge processing pipeline for your Obsidian vault. Three runs execute daily:

| Run | Time | Mission |
|-----|------|---------|
| **Scout** | 11:00 PM | Intake raw captures, classify into literature notes |
| **Refinery** | 3:00 AM | Extract atomic notes from literature |
| **Editor** | 6:00 AM | Link notes, detect contradictions, update index |

## Installation

```powershell
# Install scheduled tasks
.\setup-night-shift.ps1

# Verify installation
Get-ScheduledTask "Ruflo Night Shift*"

# Uninstall
.\setup-night-shift.ps1 -Uninstall
```

## Manual Execution

```powershell
# Run Scout manually (test mode)
.\scout-run.ps1 -DryRun

# Run Refinery manually
.\refinery-run.ps1

# Run Editor manually
.\editor-run.ps1

# Run with custom vault path
.\scout-run.ps1 -VaultPath "E:\_Knowledge\ObsidianVault"
```

## Output Locations

```
E:\_Knowledge\ObsidianVault/
├── 00 - INBOX/           # Drop raw captures here
├── 0-raw/                # Raw source files (immutable)
├── 1-desk/               # Classified literature notes
│   ├── article/
│   ├── book/
│   ├── paper/
│   ├── _quarantine/     # Items missing sources
│   └── _needs-work/     # Atoms that failed quality checks
├── 2-atoms/              # Atomic notes (permanent)
│   ├── concepts/
│   └── people/
├── 3-threads/
│   ├── _friction/       # Contradiction flags
│   └── orphans/         # Orphaned notes report
├── sources/archived/     # Processed literature notes
├── briefings/            # Morning briefs
│   └── YYYY-MM-DD — Morning Brief.md
└── log.md                # Run history
```

## Morning Brief Structure

Each morning brief includes:

1. **Scout Summary** — Items processed, classified, quarantined
2. **Refinery Summary** — Atoms extracted, sources archived
3. **Editor Summary** — Links added, friction flags, orphans

## [FRICTION] System

Contradictions are auto-detected when:
- New atom contains: "but", "however", "contradicts", "updated view"
- Same concept has opposite claims in different notes
- Temporal conflicts (was true, now changed)

Resolution happens during morning review, not overnight.

## Troubleshooting

### Task won't run
```powershell
# Check task status
Get-ScheduledTaskInfo "Ruflo Night Shift - Scout Run"

# Run manually
Start-ScheduledTask "Ruflo Night Shift - Scout Run"

# View last result
(Get-ScheduledTask "Ruflo Night Shift - Scout Run").LastTaskResult
```

### Script errors
```powershell
# Run with verbose output
.\scout-run.ps1 -Verbose

# Check PowerShell execution policy
Get-ExecutionPolicy

# Temporarily allow
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```

### Missing sources
Items without verifiable sources go to `1-desk/_quarantine/`. Review and either:
- Add source URL/file path
- Delete the item
- Move to `00 - INBOX/` for manual processing

## Customization

### Change schedule
Edit `setup-night-shift.ps1` and modify the `-At` times:
```powershell
$Trigger = New-ScheduledTaskTrigger -Daily -At 11:00PM  # Change this
```

### Add content types
Edit `scout-run.ps1` and add to the `Get-FileType` function:
```powershell
".webm" { return "video" }  # Add new extension
```

### Adjust quality gates
Edit `refinery-run.ps1` and modify the `New-AtomicNote` function quality checks.

## Monitoring

```powershell
# View all tasks
Get-ScheduledTask "Ruflo Night Shift*" | Get-ScheduledTaskInfo

# Export run history
Get-Content .\log.md -Tail 50

# Check briefings
Get-ChildItem .\briefings\ | Sort-Object LastWriteTime -Descending | Select-Object -First 5
```

---
*For full playbook details, see:*
- `01-scout-run.md` — Scout Run playbook
- `02-refinery-run.md` — Refinery Run playbook
- `03-editor-run.md` — Editor Run playbook
- `house-rules.md` — Prime Directive & operating rules