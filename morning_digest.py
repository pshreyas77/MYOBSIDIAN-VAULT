#!/usr/bin/env python3
import os
from datetime import datetime, timedelta

VAULT_PATH = "/home/sunny77/Documents/Obsidian Vault"

def read_claude_md():
    claude_path = os.path.join(VAULT_PATH, "CLAUDE.md")
    if os.path.exists(claude_path):
        with open(claude_path, 'r') as f:
            content = f.read()
        # Extract active projects section
        lines = content.split('\n')
        in_active = False
        projects = []
        for line in lines:
            if line.startswith('# Active Projects'):
                in_active = True
                continue
            if in_active and line.startswith('#'):
                break
            if in_active and line.strip().startswith('-'):
                projects.append(line.strip())
        return projects
    return []

def list_recent_files(directory, hours=24):
    cutoff = datetime.now() - timedelta(hours=hours)
    recent_files = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            path = os.path.join(root, f)
            mtime = datetime.fromtimestamp(os.path.getmtime(path))
            if mtime >= cutoff:
                recent_files.append(path)
    return recent_files

def main():
    print(f"=== Morning Digest for {datetime.now().strftime('%Y-%m-%d')} ===\n")

    # 1. Active projects from CLAUDE.md
    print("## Active Projects")
    projects = read_claude_md()
    if projects:
        for p in projects:
            print(p)
    else:
        print("No active projects found.")
    print()

    # 2. Files in raw-sources/ added in last 24 hours
    raw_sources_path = os.path.join(VAULT_PATH, "raw-sources")
    print("## New in raw-sources/ (last 24h)")
    if os.path.exists(raw_sources_path):
        raw_new = list_recent_files(raw_sources_path)
        if raw_new:
            for f in raw_new:
                print(f)
        else:
            print("No new files.")
    else:
        print("Directory does not exist.")
    print()

    # 3. Files in inbox/ added in last 24 hours
    inbox_path = os.path.join(VAULT_PATH, "inbox")
    print("## New in inbox/ (last 24h)")
    if os.path.exists(inbox_path):
        inbox_new = list_recent_files(inbox_path)
        if inbox_new:
            for f in inbox_new:
                print(f)
        else:
            print("No new files.")
    else:
        print("Directory does not exist.")
    print()

if __name__ == "__main__":
    main()