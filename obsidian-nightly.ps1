# Obsidian Nightly Consolidation Script
# Runs daily at 22:00 via Windows Task Scheduler (ObsidianNightly task)
# Reads _CLAUDE.md for vault-specific paths

$vault = "E:\_Knowledge\ObsidianVault"
$date = Get-Date -Format "yyyy-MM-dd"

Set-Location $vault

$prompt = @"
obsidian-nightly consolidation pass — read _CLAUDE.md first for vault paths.

Phase 1 — Close the day:
- Read today's daily note: `04 - DAILY/$date.md`
- If it doesn't exist: read `00 - SYSTEM/Templates/Daily Note.md`, substitute `$date` for the date field, create `04 - DAILY/$date.md`
- Append `## End of Day` section with a 3-5 bullet summary of what happened today
- Move any completed kanban tasks to Done (check `00 - SYSTEM/` for kanban boards)

Phase 2 — Reconcile:
- Scan `wiki/entities/` for outdated roles/companies that conflict with newer notes
- Scan `wiki/concepts/` for claims contradicted by recently ingested sources
- Auto-resolve clear winners. Flag ambiguous ones in `wiki/decisions/`

Phase 3 — Synthesize:
- Scan sources ingested today and yesterday (check `raw-sources/`, recent daily notes)
- Find concepts that appear in 2+ unrelated sources
- Create `wiki/concepts/Synthesis — Title.md` with evidence and interpretation

Phase 4 — Heal:
- Find notes created today with no incoming links, add links from relevant existing pages
- Check entity pages for timeline entries missing an `until: present` that should be closed
- Update `index.md` if it exists

Phase 5 — Log:
- Read `log.md`, append: `## [$date] nightly | End of day + X reconciled, Y synthesized, Z orphans linked`

Do not ask questions. Do not fix anything destructive — only add, update, link. Save and stop.
"@

$env:CLAUDE_DANGEROUSLY_SKIP_PERMISSIONS = "1"
& claude -p $prompt --output-format stream 2>&1

"$date | Obsidian nightly consolidation completed" | Out-File -FilePath "$vault\logs\nightly-consolidation.log" -Append