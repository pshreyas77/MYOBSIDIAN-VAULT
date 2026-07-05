# Run this script AS ADMINISTRATOR to register the scheduled task
# Right-click PowerShell -> "Run as Administrator" then:
# .\scripts\register-scheduled-task-admin.ps1

$taskXmlPath = "E:\_Knowledge\ObsidianVault\scripts\ObsidianVault-GitAutoPush.xml"
$taskName = "ObsidianVault-GitAutoPush"

# Check if task already exists
$existing = Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
if ($existing) {
    Write-Host "Task '$taskName' already exists. Unregistering first..."
    Unregister-ScheduledTask -TaskName $taskName -Confirm:$false
}

# Register the task
Register-ScheduledTask -TaskName $taskName -Xml (Get-Content $taskXmlPath -Raw)

Write-Host ""
Write-Host "========================================"
Write-Host "SUCCESS: Scheduled task registered!"
Write-Host "========================================"
Write-Host "Task: $taskName"
Write-Host "Schedule: Daily at 22:00"
Write-Host "Action: powershell.exe -ExecutionPolicy Bypass -File E:\_Knowledge\ObsidianVault\scripts\git-auto-push.ps1"
Write-Host ""
Write-Host "To verify: Get-ScheduledTask '$taskName' | Get-ScheduledTaskInfo"
Write-Host "To run manually now: Start-ScheduledTask '$taskName'"
Write-Host "To unregister: Unregister-ScheduledTask '$taskName'"