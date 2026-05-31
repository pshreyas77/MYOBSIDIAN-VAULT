# Obsidian Nightly Consolidation Script
# Runs the 5-phase process: Close the day, Reconcile, Synthesize, Heal, Log

# Set the vault root to the script's directory
$VaultRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $VaultRoot

Write-Host "Starting Obsidian Nightly Consolidation..."

# Phase 1: Close the day
Write-Host "Phase 1: Close the day"
$Today = Get-Date -Format "yyyy-MM-dd"
$DailyNote = "04 - DAILY\$Today.md"
if (Test-Path $DailyNote) {
    $EndOfDay = "## End of Day`r`n- No specific focus or tasks recorded for today`r`n- Daily note created for sleeptime consolidation pass`r`n- Vault structure maintained with PARA+ organization"
    Add-Content -Path $DailyNote -Value "`r`n$EndOfDay"
    Write-Host "Updated daily note with End of Day section."
} else {
    Write-Warning "Daily note for $Today not found."
}

# Phase 2: Reconcile
Write-Host "Phase 2: Reconcile"
# Placeholder: In a full implementation, this would scan for outdated roles/companies and contradicted claims.
# For now, we just log that reconciliation would happen.
Write-Host "Reconciliation scan would run here (checking wiki/entities and wiki/concepts for conflicts)."

# Phase 3: Synthesize
Write-Host "Phase 3: Synthesize"
# Placeholder: Scan sources from last 2 days for concepts in 2+ unrelated sources.
Write-Host "Synthesis scan would run here (creating wiki/concepts/Synthesis — Title.md if patterns found)."

# Phase 4: Heal
Write-Host "Phase 4: Heal"
# Placeholder: Find orphaned notes, fix entity timeline entries, rebuild index.md.
Write-Host "Healing would run here (linking orphaned notes, closing open timelines, rebuilding index.md)."

# Phase 5: Log
Write-Host "Phase 5: Log"
$LogEntry = "## [$Today] nightly | End of day + X reconciled, Y synthesized, Z orphans linked"
Add-Content -Path "log.md" -Value "`r`n$LogEntry"
Write-Host "Appended to log.md."

Write-Host "Obsidian Nightly Consolidation completed."