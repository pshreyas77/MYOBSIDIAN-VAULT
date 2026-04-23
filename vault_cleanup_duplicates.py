#!/usr/bin/env python3
"""
Vault Cleanup Script - Remove duplicate old directories after migration.
Backs up old structures to 04 - ARCHIVE before removal.
"""

import os
import shutil
import json
from datetime import datetime
from pathlib import Path

VAULT_ROOT = "/home/sunny77/Documents/Obsidian Vault"

# Directories to check and potentially clean up (old structures superseded by new PARA)
OLD_DIRECTORIES = [
    "02 - Areas",          # Superseded by "02 - AREAS"
    "01 - Projects",       # Superseded by "01 - PROJECTS"
    "02 - Areas/AI Research & Agents",
    "02 - Areas/Ancient Civilizations",
    "02 - Areas/Buddhism & Hinduism",
    "02 - Areas/Political Analysis",
    "02 - Areas/Religion & Cosmology",
    "02 - Areas/graphify-out",
    "ClaudeVault",
    "DeepseekVault",
    "07 - Topics",
]

# Other known directories to preserve
PRESERVE_DIRS = [
    "00 - SYSTEM",
    "01 - PROJECTS",
    "02 - AREAS",
    "03 - RESOURCES",
    "04 - ARCHIVE",
    "Attachments",
    "BUDDHA",  # Has graph files
    "Daily Notes",
    "ClaudeVault/.claude-plugin",
    "genericagent",
    "graphify-repo",
]


def get_dir_size(path):
    """Get size of directory in human readable format."""
    try:
        total = 0
        for entry in os.scandir(path):
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size_bytes(entry.path)
        return total
    except (OSError, PermissionError):
        return 0


def get_dir_size_bytes(path):
    """Get size of directory in bytes."""
    total = 0
    try:
        for entry in os.scandir(path):
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size_bytes(entry.path)
    except (OSError, PermissionError):
        pass
    return total


def format_size(size):
    """Format size in human readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} TB"


def count_files(path):
    """Count files in directory."""
    count = 0
    try:
        for entry in os.scandir(path):
            if entry.is_file():
                count += 1
            elif entry.is_dir():
                count += count_files(entry.path)
    except (OSError, PermissionError):
        pass
    return count


def should_preserve(path):
    """Check if directory should be preserved."""
    rel_path = os.path.relpath(path, VAULT_ROOT)
    for preserve in PRESERVE_DIRS:
        if rel_path == preserve or rel_path.startswith(preserve + "/"):
            return True
    return False


def analyze_old_directories():
    """Analyze old directories and generate report."""
    print("=" * 80)
    print("VAULT CLEANUP ANALYSIS")
    print("=" * 80)
    print()

    analysis = []

    for old_dir in OLD_DIRECTORIES:
        full_path = os.path.join(VAULT_ROOT, old_dir)
        if os.path.exists(full_path):
            size = get_dir_size(full_path)
            file_count = count_files(full_path)

            status = "DUPLICATE" if file_count > 0 else "EMPTY"

            analysis.append({
                "path": old_dir,
                "full_path": full_path,
                "exists": True,
                "size": size,
                "file_count": file_count,
                "status": status
            })

            print(f"📁 {old_dir}")
            print(f"   Status: {status}")
            print(f"   Size: {format_size(size)}")
            print(f"   Files: {file_count}")
            print()
        else:
            analysis.append({
                "path": old_dir,
                "full_path": full_path,
                "exists": False,
                "size": 0,
                "file_count": 0,
                "status": "MISSING"
            })
            print(f"✅ {old_dir} - Already removed")

    print()
    print("=" * 80)

    return analysis


def backup_and_remove(analysis, dry_run=True):
    """Backup and remove duplicate directories."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = os.path.join(VAULT_ROOT, "04 - ARCHIVE", f"old_structures_backup_{timestamp}")

    to_remove = [a for a in analysis if a["exists"] and a["file_count"] > 0]

    if not to_remove:
        print("\n✅ No directories to remove!")
        return True

    print(f"\n{'[DRY RUN] ' if dry_run else ''}PREPARING TO REMOVE:")
    for item in to_remove:
        print(f"  • {item['path']} ({format_size(item['size'])}, {item['file_count']} files)")

    total_size = sum(item["size"] for item in to_remove)
    total_files = sum(item["file_count"] for item in to_remove)

    print(f"\nTotal to remove: {format_size(total_size)} across {total_files} files")
    print()

    if dry_run:
        print("\n⚠️  This is a DRY RUN. No files were actually moved or deleted.")
        print("    Run with dry_run=False to actually backup and remove these directories.")
        return False

    # Create backup directory
    os.makedirs(backup_dir, exist_ok=True)

    # Backup and remove
    success_count = 0
    for item in to_remove:
        try:
            dest = os.path.join(backup_dir, os.path.basename(item["full_path"]))
            print(f"📦 Backing up: {item['path']} → {dest}")
            shutil.copytree(item["full_path"], dest)

            print(f"🗑️  Removing: {item['path']}")
            shutil.rmtree(item["full_path"])
            success_count += 1
            print(f"✅ Removed successfully")
        except Exception as e:
            print(f"❌ Error: {e}")

    # Write removal log
    log_path = os.path.join(backup_dir, "_removal_log.json")
    with open(log_path, 'w') as f:
        json.dump({
            "timestamp": timestamp,
            "backed_up_to": backup_dir,
            "removed_count": success_count,
            "directories": to_remove
        }, f, indent=2)

    print(f"\n{'=' * 80}")
    print(f"BACKUP LOCATION: {backup_dir}")
    print(f"DIRECTORIES REMOVED: {success_count}")
    print(f"REMOVAL LOG: {log_path}")
    print('=' * 80)

    return True


def verify_new_structure():
    """Verify that the new structure is intact."""
    print("\n" + "=" * 80)
    print("VERIFYING NEW STRUCTURE")
    print("=" * 80)

    new_roots = ["00 - SYSTEM", "01 - PROJECTS", "02 - AREAS", "03 - RESOURCES", "04 - ARCHIVE"]

    all_ok = True
    for root in new_roots:
        path = os.path.join(VAULT_ROOT, root)
        if os.path.exists(path):
            size = get_dir_size(path)
            file_count = count_files(path)
            print(f"✅ {root}: {format_size(size)}, {file_count} files")
        else:
            print(f"⚠️  {root}: MISSING!")
            all_ok = False

    return all_ok


if __name__ == "__main__":
    import sys

    # Run analysis
    analysis = analyze_old_directories()

    # Check current state
    old_areas_size = get_dir_size(os.path.join(VAULT_ROOT, "02 - Areas"))
    new_areas_size = get_dir_size(os.path.join(VAULT_ROOT, "02 - AREAS"))
    topics_remaining = count_files(os.path.join(VAULT_ROOT, "07 - Topics"))

    print(f"\nCOMPARISON:")
    print(f"  '02 - Areas' (old): {format_size(old_areas_size)}")
    print(f"  '02 - AREAS' (new): {format_size(new_areas_size)}")
    print(f"  '07 - Topics' remaining: {topics_remaining} files")

    # Verify new structure
    if not verify_new_structure():
        print("\n❌ New structure is incomplete! Aborting.")
        sys.exit(1)

    print("\n" + "=" * 80)
    print("would you like to:")
    print("  1. Run DRY RUN (safe check, no changes)")
    print("  2. ACTUALLY BACKUP AND REMOVE (permanent)")
    print("  3. Cancel")
    print("=" * 80)

    # For safety, default to dry run
    backup_and_remove(analysis, dry_run=True)
