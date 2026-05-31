#!/usr/bin/env python3
import os
import glob
from datetime import datetime, timedelta
from pathlib import Path

VAULT = Path("E:/ObsidianVault")
TODAY = datetime.now()
YESTERDAY = TODAY - timedelta(hours=24)

print(f"\n{'='*50}")
print(f"MORNING DIGEST — {TODAY.strftime('%A %d %B %Y %H:%M')}")
print(f"{'='*50}\n")

# Active projects from CLAUDE.md
claude_md = VAULT / "CLAUDE.md"
if claude_md.exists():
    lines = claude_md.read_text(encoding='utf-8').splitlines()
    in_projects = False
    print("ACTIVE PROJECTS:")
    for line in lines:
        if "## Active Projects" in line:
            in_projects = True
            continue
        if in_projects and line.startswith("## "):
            break
        if in_projects and line.strip().startswith("-"):
            print(f"  {line.strip()}")
    print()

# New raw-sources
new_sources = [f for f in glob.glob(str(VAULT / "raw-sources" / "*"))
               if datetime.fromtimestamp(os.path.getmtime(f)) > YESTERDAY]
print(f"NEW IN raw-sources/ (last 24h): {len(new_sources)}")
for f in new_sources:
    print(f"  - {Path(f).name}")
print()

# New inbox
new_inbox = [f for f in glob.glob(str(VAULT / "inbox" / "*.md"))
             if datetime.fromtimestamp(os.path.getmtime(f)) > YESTERDAY]
print(f"NEW IN inbox/ (last 24h): {len(new_inbox)}")
for f in new_inbox:
    print(f"  - {Path(f).name}")
print()

# Last session log
sessions = sorted(glob.glob(str(VAULT / "logs" / "sessions" / "*.md")))
if sessions:
    last = Path(sessions[-1])
    print(f"LAST SESSION: {last.name}")
    content = last.read_text(encoding='utf-8')[:300]
    print(f"  {content[:200]}...")
print(f"\n{'='*50}\n")