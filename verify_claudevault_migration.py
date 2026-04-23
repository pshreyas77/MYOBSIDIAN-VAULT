#!/usr/bin/env python3
"""
Verify ClaudeVault files were properly migrated to new structure.
"""

import re
from pathlib import Path

VAULT_ROOT = Path("/home/sunny77/Documents/Obsidian Vault")
MIGRATION_REPORT = VAULT_ROOT / "VAULT_MIGRATION_REPORT.md"

def extract_claudevault_migrations():
    """Extract all ClaudeVault migrations from report."""
    content = MIGRATION_REPORT.read_text(encoding='utf-8')

    # Find all lines with ClaudeVault migrations
    pattern = r'- `ClaudeVault/(.+?)` → `(.+?)`'
    matches = re.findall(pattern, content)

    migrations = []
    for source, dest in matches:
        migrations.append({
            'source': source,
            'dest': dest,
            'dest_path': VAULT_ROOT / dest
        })

    return migrations

def verify_migrations(migrations):
    """Check if all migrated files exist."""
    found = []
    missing = []

    for mig in migrations:
        if mig['dest_path'].exists():
            found.append(mig)
        else:
            missing.append(mig)

    return found, missing

def main():
    print("=" * 80)
    print("CLAUDEVAULT MIGRATION VERIFICATION")
    print("=" * 80)
    print()

    migrations = extract_claudevault_migrations()
    print(f"Total ClaudeVault files in migration report: {len(migrations)}")
    print()

    found, missing = verify_migrations(migrations)

    print(f"✅ Found in new location: {len(found)}")
    print(f"❌ Missing: {len(missing)}")
    print()

    if missing:
        print("=" * 80)
        print("MISSING FILES:")
        print("=" * 80)
        for mig in missing[:20]:  # Show first 20
            print(f"  ❌ {mig['source']} → {mig['dest']}")
        if len(missing) > 20:
            print(f"  ... and {len(missing) - 20} more")
        print()

    # Check archive
    archive_dir = VAULT_ROOT / "04 - ARCHIVE" / "ClaudeVault_Archive"
    if archive_dir.exists():
        archived_files = list(archive_dir.glob("*.md"))
        print(f"📦 Files in ClaudeVault_Archive: {len(archived_files)}")
        for f in archived_files[:10]:
            print(f"   - {f.name}")
        print()

    # Sample verification of found files
    if found:
        print("=" * 80)
        print("SAMPLE VERIFIED FILES:")
        print("=" * 80)
        for mig in found[:10]:
            size = mig['dest_path'].stat().st_size
            print(f"  ✅ {mig['dest']} ({size} bytes)")
        print()

    print("=" * 80)
    if not missing:
        print("✅ ALL CLAUDEVAULT FILES ACCOUNTED FOR!")
    else:
        print(f"⚠️  {len(missing)} files may need restoration from archive")
    print("=" * 80)

if __name__ == "__main__":
    main()
