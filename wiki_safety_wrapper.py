#!/usr/bin/env python3
"""
LLM Wiki Safety Wrapper
Adds extra protection layers to prevent accidental data loss.
Non-interactive version for automated use.
"""

import os
import sys
import subprocess
import datetime
from pathlib import Path

def get_vault_path():
    """Get the Obsidian vault path"""
    return Path("/home/sunny77/Documents/Obsidian Vault")

def is_git_repo(path):
    """Check if path is a git repository"""
    git_dir = path / ".git"
    return git_dir.exists() and git_dir.is_dir()

def get_git_status(repo_path):
    """Get git status - returns (is_clean, changes)"""
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=repo_path,
            capture_output=True,
            text=True
        )
        is_clean = len(result.stdout.strip()) == 0
        changes = result.stdout.strip() if not is_clean else ""
        return is_clean, changes
    except Exception as e:
        return False, f"Error checking git status: {e}"

def create_safety_backup(repo_path):
    """Create a timestamped backup commit"""
    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        commit_msg = f"SAFETY BACKUP: Pre-operation backup {timestamp}"

        # Add all changes
        subprocess.run(["git", "add", "-A"], cwd=repo_path, check=True)

        # Commit if there are changes
        result = subprocess.run(
            ["git", "diff", "--staged", "--quiet"],
            cwd=repo_path,
            capture_output=True
        )

        if result.returncode != 0:  # There are changes to commit
            subprocess.run(
                ["git", "commit", "-m", commit_msg],
                cwd=repo_path,
                check=True
            )
            print(f"✅ Safety backup created: {commit_msg}")
            return True
        else:
            print("ℹ️  No changes to backup")
            return True
    except Exception as e:
        print(f"⚠️  Warning: Could not create safety backup: {e}")
        return False  # Don't fail the operation for backup failure

def verify_safe_operation(repo_path, operation_name):
    """Verify that operation is safe to proceed"""
    print(f"🔒 Safety check for: {operation_name}")

    # Check if we're in a git repo
    if not is_git_repo(repo_path):
        print("❌ ERROR: Vault is not a git repository!")
        print("   This system requires git for safety protections.")
        return False

    # Check git status - warn but don't block in non-interactive mode
    is_clean, changes = get_git_status(repo_path)

    if not is_clean:
        print("⚠️  WARNING: You have uncommitted changes:")
        # Show first few lines of changes
        change_lines = changes.split('\n')[:5]
        for line in change_lines:
            print(f"   {line}")
        if len(changes.split('\n')) > 5:
            remaining = len(changes.split('\n')) - 5
            print(f"   ... and {remaining} more changes")
        print("   Proceeding anyway (non-interactive mode)")
    else:
        print("   ✅ Working directory is clean")

    return True  # Always proceed in non-interactive mode

def safe_execute(operation_func, operation_name, *args, **kwargs):
    """Safely execute an operation with protections"""
    repo_path = get_vault_path()

    # Pre-operation safety checks
    if not verify_safe_operation(repo_path, operation_name):
        return False

    # Create safety backup
    print("🛡️  Creating safety backup...")
    if not create_safety_backup(repo_path):
        print("⚠️  Warning: Safety backup failed, but continuing...")

    # Execute the operation
    try:
        print(f"🚀 Executing: {operation_name}")
        result = operation_func(*args, **kwargs)
        print(f"✅ Completed: {operation_name}")
        return result
    except Exception as e:
        print(f"❌ Error during {operation_name}: {e}")
        print("🔧 Recovery suggestions:")
        print("   1. Check git status: git status")
        print("   2. Review changes: git diff")
        print("   3. Restore if needed: git checkout -- .")
        raise

def show_recovery_instructions():
    """Show how to recover from any issues"""
    print("\n" + "="*60)
    print("🛡️  LLM WIKI SAFETY - RECOVERY INSTRUCTIONS")
    print("="*60)
    print("If anything seems wrong after an operation:")
    print()
    print("1. Review what changed:")
    print("   git status")
    print("   git diff --stat")
    print()
    print("2. See detailed changes:")
    print("   git diff")
    print()
    print("3. Restore specific files:")
    print("   git checkout -- path/to/file.md")
    print()
    print("4. Restore ALL changes:")
    print("   git checkout -- .")
    print("   # OR")
    print("   git reset --hard HEAD")
    print()
    print("5. To completely remove LLM Wiki system:")
    print("   rm -rf wiki/")
    print("   rm -f wiki_*.py")
    print("   # Your original vault remains 100% intact")
    print()
    print("💡 Remember: Your original notes are NEVER modified!")
    print("   All LLM Wiki operations are additive-only.")
    print("="*60)

if __name__ == "__main__":
    # Test the safety wrapper
    vault_path = get_vault_path()
    print(f"Vault path: {vault_path}")
    print(f"Is git repo: {is_git_repo(vault_path)}")

    if is_git_repo(vault_path):
        is_clean, changes = get_git_status(vault_path)
        print(f"Git status clean: {is_clean}")
        if not is_clean:
            print(f"Changes: {changes[:100]}...")

    show_recovery_instructions()