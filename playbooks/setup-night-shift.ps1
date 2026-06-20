# Night Shift Setup — Automated Knowledge Processing
# Windows Task Scheduler Installation Script

param(
    [string]$VaultPath = "E:\_Knowledge\ObsidianVault",
    [switch]$Uninstall = $false
)

$ErrorActionPreference = "Stop"
$ScriptDir = "$VaultPath\playbooks"

Write-Host "=== Night Shift Setup ===" -ForegroundColor Cyan
Write-Host "Vault: $VaultPath" -ForegroundColor Gray
Write-Host ""

if ($Uninstall) {
    # Remove scheduled tasks
    Write-Host "Removing scheduled tasks..." -ForegroundColor Yellow

    $Tasks = @(
        "Ruflo Night Shift - Scout Run",
        "Ruflo Night Shift - Refinery Run",
        "Ruflo Night Shift - Editor Run"
    )

    foreach ($Task in $Tasks) {
        if (Get-ScheduledTask -TaskName $Task -ErrorAction SilentlyContinue) {
            Unregister-ScheduledTask -TaskName $Task -Confirm:$false
            Write-Host "  Removed: $Task" -ForegroundColor Green
        } else {
            Write-Host "  Not found: $Task" -ForegroundColor Gray
        }
    }

    Write-Host "`nUninstall complete. Scripts retained in $ScriptDir" -ForegroundColor Cyan
    return
}

# Verify scripts exist
Write-Host "Verifying scripts..." -ForegroundColor Magenta

$Scripts = @(
    @{ Name = "Scout Run"; File = "scout-run.ps1"; Time = "11:00 PM" },
    @{ Name = "Refinery Run"; File = "refinery-run.ps1"; Time = "3:00 AM" },
    @{ Name = "Editor Run"; File = "editor-run.ps1"; Time = "6:00 AM" }
)

foreach ($Script in $Scripts) {
    $Path = "$ScriptDir\$($Script.File)"
    if (Test-Path $Path) {
        Write-Host "  ✓ $($Script.Name): $Path" -ForegroundColor Green
    } else {
        Write-Host "  ✗ Missing: $($Script.File)" -ForegroundColor Red
        throw "Script not found: $Path"
    }
}

Write-Host "`nCreating scheduled tasks..." -ForegroundColor Magenta

# Scout Run - 11:00 PM daily
$Trigger = New-ScheduledTaskTrigger -Daily -At 11:00PM
$Action = New-ScheduledTaskAction -Execute "PowerShell.exe" `
    -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$ScriptDir\scout-run.ps1`" -VaultPath `"$VaultPath`""
$Principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Highest
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

Register-ScheduledTask `
    -TaskName "Ruflo Night Shift - Scout Run" `
    -Description "Intake raw captures from INBOX/0-raw, classify into literature notes with frontmatter" `
    -Trigger $Trigger `
    -Action $Action `
    -Principal $Principal `
    -Settings $Settings `
    -Force

Write-Host "  ✓ Scout Run: 11:00 PM daily" -ForegroundColor Green

# Refinery Run - 3:00 AM daily
$Trigger = New-ScheduledTaskTrigger -Daily -At 3:00AM
$Action = New-ScheduledTaskAction -Execute "PowerShell.exe" `
    -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$ScriptDir\refinery-run.ps1`" -VaultPath `"$VaultPath`""
$Principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Highest
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

Register-ScheduledTask `
    -TaskName "Ruflo Night Shift - Refinery Run" `
    -Description "Extract atomic notes from literature notes in 1-desk/, save to 2-atoms/ with citations" `
    -Trigger $Trigger `
    -Action $Action `
    -Principal $Principal `
    -Settings $Settings `
    -Force

Write-Host "  ✓ Refinery Run: 3:00 AM daily" -ForegroundColor Green

# Editor Run - 6:00 AM daily
$Trigger = New-ScheduledTaskTrigger -Daily -At 6:00AM
$Action = New-ScheduledTaskAction -Execute "PowerShell.exe" `
    -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$ScriptDir\editor-run.ps1`" -VaultPath `"$VaultPath`""
$Principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Highest
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

Register-ScheduledTask `
    -TaskName "Ruflo Night Shift - Editor Run" `
    -Description "Link new atoms, detect [FRICTION] contradictions, update index.md, orphan detection" `
    -Trigger $Trigger `
    -Action $Action `
    -Principal $Principal `
    -Settings $Settings `
    -Force

Write-Host "  ✓ Editor Run: 6:00 AM daily" -ForegroundColor Green

Write-Host "`n=== Night Shift Scheduled ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "Schedule:" -ForegroundColor White
Write-Host "  11:00 PM — Scout Run (intake & classify)" -ForegroundColor Cyan
Write-Host "   3:00 AM — Refinery Run (extract atoms)" -ForegroundColor Yellow
Write-Host "   6:00 AM — Editor Run (link & index)" -ForegroundColor Magenta
Write-Host ""
Write-Host "Check status: Get-ScheduledTask 'Ruflo Night Shift*'" -ForegroundColor Gray
Write-Host "Manual trigger: schtasks /run /tn 'Ruflo Night Shift - Scout Run'" -ForegroundColor Gray
Write-Host "Uninstall: .\setup-night-shift.ps1 -Uninstall" -ForegroundColor Gray