#!/bin/bash
# Obsidian Vault Auto-Commit & Push
# Runs daily at 10 PM IST via cron — uploads workspace changes to GitHub.
# Skips silently if no changes (so cron doesn't spam logs).

# Resolve vault path (cron has no $HOME equivalents); use absolute
VAULT="E:/_Knowledge/ObsidianVault"
cd "$VAULT" || exit 1

# Determine branch
BRANCH=$(git branch --show-current 2>/dev/null || echo "windows")

# Capture current date (cross-platform)
if date --version >/dev/null 2>&1; then
  DATE=$(date +"%Y-%m-%d %H:%M")
else
  DATE=$(date +"%Y-%m-%d %H:%M")
fi

# Check for changes
CHANGES=$(git status --porcelain 2>/dev/null)
if [ -z "$CHANGES" ]; then
  # Silent — nothing changed, exit cleanly
  exit 0
fi

# Stage all changes
git add -A

# Commit with timestamped message
git commit -m "vault sync $DATE" -m "Auto-commit (10 PM IST cron)" 2>&1

# Pull fast-forward if remote diverged (safety net)
git pull --rebase --autostash origin "$BRANCH" 2>/dev/null || true

# Push
git push origin "$BRANCH" 2>&1

exit 0
