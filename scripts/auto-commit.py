"""Auto-commit & push Obsidian vault to GitHub.

Designed to be run by Hermes cron at 10 PM IST daily.

Steps:
1. Run git add -A in vault
2. If staged changes exist, commit with timestamped message
3. Pull --rebase if remote diverged (safe-net)
4. Push to origin/<current-branch>

Exits silently (0) when nothing changed. Exits 1 on git errors so cron can log.
"""
import os
import subprocess
import sys
from datetime import datetime

VAULT = "E:\\_Knowledge\ObsidianVault"


def run(args, check=True):
    """Run a command in vault directory."""
    return subprocess.run(
        args,
        cwd=VAULT,
        capture_output=True,
        text=True,
        shell=False,
        check=check,
    )


def main():
    if not os.path.isdir(VAULT):
        print(f"Vault not found: {VAULT}", file=sys.stderr)
        return 1

    # Get current branch
    try:
        branch_proc = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=VAULT,
            capture_output=True,
            text=True,
        )
        branch = branch_proc.stdout.strip() or "windows"
    except Exception as e:
        print(f"Could not determine branch: {e}", file=sys.stderr)
        branch = "windows"

    # Status check — exclude submodules from "nothing to do" check
    # (submodules have their own git history; we treat their state as opaque)
    status_proc = run(["git", "status", "--porcelain", "--ignore-submodules"], check=False)
    if status_proc.returncode != 0:
        print(f"git status failed: {status_proc.stderr}", file=sys.stderr)
        return 1

    if not status_proc.stdout.strip():
        # Silent — no changes
        return 0

    # Add everything (submodules will be added as references, not their contents)
    add_proc = run(["git", "add", "-A"], check=False)
    if add_proc.returncode != 0:
        print(f"git add failed: {add_proc.stderr}", file=sys.stderr)
        return 1

    # Commit with timestamp
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    commit_msg = f"vault sync {now}"
    commit_body = "Auto-commit (10 PM IST cron)"
    commit_proc = run(
        ["git", "commit", "-m", commit_msg, "-m", commit_body],
        check=False,
    )

    # If nothing to commit after add (race), exit
    if commit_proc.returncode != 0:
        if "nothing to commit" in (commit_proc.stdout + commit_proc.stderr).lower():
            return 0
        print(f"git commit failed: {commit_proc.stderr}", file=sys.stderr)
        return 1

    # Pull rebase (safe-net)
    pull_proc = run(
        ["git", "pull", "--rebase", "--autostash", "origin", branch],
        check=False,
    )
    if pull_proc.returncode != 0:
        # Try to abort rebase and continue anyway? Actually skip push.
        print(f"git pull --rebase failed: {pull_proc.stderr}", file=sys.stderr)
        return 1

    # Push
    push_proc = run(["git", "push", "origin", branch], check=False)
    if push_proc.returncode != 0:
        print(f"git push failed: {push_proc.stderr}", file=sys.stderr)
        return 1

    print(f"Committed and pushed to origin/{branch} at {now}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
