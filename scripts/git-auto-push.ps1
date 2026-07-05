# Git Auto-Push Script for Obsidian Vault
# Runs daily at 22:00 via Windows Task Scheduler
# Commits and pushes all changes to origin/windows branch

param(
    [string]$VaultPath = "E:\_Knowledge\ObsidianVault",
    [string]$CommitMessage = "auto: nightly sync $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
)

$ErrorActionPreference = "Stop"

Write-Host "========================================"
Write-Host "Git Auto-Push: Obsidian Vault Sync"
Write-Host "========================================"
Write-Host "Vault: $VaultPath"
Write-Host "Date:  $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
Write-Host ""

# Navigate to vault
Set-Location $VaultPath

# Check git status
Write-Host "Checking repository status..."
$status = git status --porcelain 2>&1

if ([string]::IsNullOrWhiteSpace($status)) {
    Write-Host "[INFO] No changes to commit. Repository is clean."
    Write-Host ""
    Write-Host "Repository up to date. Nothing to push."
    exit 0
}

Write-Host "Changes detected:"
git status --short
Write-Host ""

# Stage all changes
Write-Host "Staging all changes..."
git add -A
Write-Host "[OK] Staged."

# Commit
Write-Host "Committing changes..."
$actualMessage = $CommitMessage -replace '\$\((Get-Date -Format ''yyyy-MM-dd HH:mm'')\)', (Get-Date -Format 'yyyy-MM-dd HH:mm')
git commit -m $actualMessage
if ($LASTEXITCODE -ne 0) {
    Write-Host "[WARN] Commit may have partially failed (possibly nothing new to commit after git add)."
}
Write-Host "[OK] Committed: $actualMessage"

# Pull latest changes (rebase strategy)
Write-Host ""
Write-Host "Pulling remote changes (rebase)..."
git pull --rebase origin windows
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Pull/rebase failed. Aborting push."
    Write-Host "Resolve conflicts manually and run: git push origin windows"
    exit 1
}
Write-Host "[OK] Pulled and rebased."

# Push
Write-Host ""
Write-Host "Pushing to GitHub (origin/windows)..."
git push origin windows
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Push failed. Check credentials and remote repository access."
    exit 1
}
Write-Host "[OK] Pushed successfully."

Write-Host ""
Write-Host "========================================"
Write-Host "Sync completed successfully."
Write-Host "========================================"

exit 0