#!/usr/bin/env python3
"""
Migrate remaining files from old structure to new PARA structure.
"""

import os
import shutil
from pathlib import Path

VAULT_ROOT = Path("/home/sunny77/Documents/Obsidian Vault")

MIGRATION_PLAN = [
    # Old path -> New location
    (
        "02 - Areas/Ancient Civilizations",
        "02 - AREAS/03 Ancient Civilizations/Ancient Civilizations Areas"
    ),
    (
        "02 - Areas/Buddhism & Hinduism",
        "02 - AREAS/01 Philosophy & Religion/Buddhism & Hinduism Areas"
    ),
    (
        "02 - Areas/graphify-out",
        "02 - AREAS/05 Knowledge Management/graphify-out-areas"
    ),
    (
        "01 - Projects/Obsidian RAG System",
        "02 - AREAS/02 AI & Technology/Obsidian RAG System"
    ),
]


def migrate_directory(src_rel, dst_rel):
    """Migrate a directory from old to new location."""
    src = VAULT_ROOT / src_rel
    dst = VAULT_ROOT / dst_rel

    if not src.exists():
        print(f"⚠️ Source doesn't exist: {src_rel}")
        return False

    if dst.exists():
        print(f"⚠️ Destination already exists: {dst_rel}")
        # Merge contents
        print(f"   Merging contents...")
        for item in src.iterdir():
            dest_item = dst / item.name
            if item.is_file():
                if not dest_item.exists():
                    shutil.copy2(item, dest_item)
                    print(f"     Copied: {item.name}")
                else:
                    print(f"     Skipped (exists): {item.name}")
            elif item.is_dir():
                if not dest_item.exists():
                    shutil.copytree(item, dest_item, dirs_exist_ok=True)
                    print(f"     Copied dir: {item.name}")
        return True
    else:
        # Just move it
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(src, dst)
        print(f"✅ Migrated: {src_rel} → {dst_rel}")
        return True


def update_links_in_file(filepath, old_path, new_path):
    """Update wiki links in a file."""
    try:
        content = filepath.read_text(encoding='utf-8')
        # Simple replacement - this is basic
        updated = content.replace(f"[[{old_path}", f"[[{new_path}")
        if updated != content:
            filepath.write_text(updated, encoding='utf-8')
            return True
    except:
        pass
    return False


def main():
    print("=" * 80)
    print("MIGRATING REMAINING FILES TO NEW STRUCTURE")
    print("=" * 80)
    print()

    success_count = 0
    for src, dst in MIGRATION_PLAN:
        if migrate_directory(src, dst):
            success_count += 1

    print()
    print("=" * 80)
    print(f"Migrated {success_count}/{len(MIGRATION_PLAN)} directories")
    print()

    # Check remaining files that might need migration
    print("Checking for other un-migrated content...")

    # Check ClaudeVault
    claudevault = VAULT_ROOT / "ClaudeVault"
    if claudevault.exists():
        files = list(claudevault.iterdir())
        if files:
            print(f"\n❗ ClaudeVault has {len(files)} files that may need migration")
            for f in files:
                print(f"   - {f.name}")

    # Check DeepseekVault
    deepseek = VAULT_ROOT / "DeepseekVault"
    if deepseek.exists():
        files = list(deepseek.iterdir())
        if files:
            print(f"\n❗ DeepseekVault has {len(files)} files that may need migration")
            for f in files:
                print(f"   - {f.name}")

    print()
    print("=" * 80)


if __name__ == "__main__":
    main()
