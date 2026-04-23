#!/usr/bin/env python3
"""
LLM Wiki Command Line Interface
Easy-to-use commands for managing your LLM Wiki second brain system.
"""

import subprocess
import sys
import os

def run_command(cmd):
    """Run a command and return the result"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)

def main():
    if len(sys.argv) < 2:
        print("LLM Wiki CLI - Manage your Obsidian second brain")
        print("")
        print("Usage: wiki.py <command> [args]")
        print("")
        print("Commands:")
        print("  init                    - Initialize the LLM Wiki system")
        print("  source <file> [title]   - Create source summary from file")
        print("  query <question> '<answer>' [related...] - Save query answer to wiki")
        print("  lint [full|orphans|stale|missing] - Run wiki health checks")
        print("  index                   - Update wiki index and statistics")
        print("  log <type> <desc>       - Log custom operation")
        print("  help                    - Show this help")
        print("")
        print("Examples:")
        print("  wiki.py init")
        print("  wiki.py source '04 - RESOURCES/Inbox/article.pdf' 'Article Title'")
        print("  wiki.py query 'What is AI?' 'Artificial Intelligence is...' [[LLM]] [[Machine Learning]]")
        print("  wiki.py lint full")
        return

    command = sys.argv[1].lower()
    vault_path = "/home/sunny77/Documents/Obsidian Vault"

    if command == "init":
        code, out, err = run_command(f"cd '{vault_path}' && python3 wiki_ingest_helper.py init")
        print(out)
        if err:
            print("Errors:", err)
        sys.exit(code)

    elif command == "source":
        if len(sys.argv) < 3:
            print("Error: Please provide a source file path")
            print("Usage: wiki.py source <file> [title]")
            sys.exit(1)
        file_path = sys.argv[2]
        title = sys.argv[3] if len(sys.argv) > 3 else ""
        if title:
            code, out, err = run_command(f"cd '{vault_path}' && python3 wiki_ingest_helper.py source '{file_path}' '{title}'")
        else:
            code, out, err = run_command(f"cd '{vault_path}' && python3 wiki_ingest_helper.py source '{file_path}'")
        print(out)
        if err:
            print("Errors:", err)
        sys.exit(code)

    elif command == "query":
        if len(sys.argv) < 4:
            print("Error: Please provide question and answer")
            print("Usage: wiki.py query <question> '<answer>' [related_pages...]")
            sys.exit(1)
        question = sys.argv[2]
        answer = sys.argv[3]
        related = sys.argv[4:] if len(sys.argv) > 4 else []
        related_str = " ".join(related)
        if related_str:
            code, out, err = run_command(f"cd '{vault_path}' && python3 wiki_query_helper.py '{question}' '{answer}' {related_str}")
        else:
            code, out, err = run_command(f"cd '{vault_path}' && python3 wiki_query_helper.py '{question}' '{answer}'")
        print(out)
        if err:
            print("Errors:", err)
        sys.exit(code)

    elif command == "lint":
        subcommand = sys.argv[2] if len(sys.argv) > 2 else "full"
        code, out, err = run_command(f"cd '{vault_path}' && python3 wiki_lint_helper.py {subcommand}")
        print(out)
        if err:
            print("Errors:", err)
        sys.exit(code)

    elif command == "index":
        code, out, err = run_command(f"cd '{vault_path}' && python3 wiki_ingest_helper.py index")
        print(out)
        if err:
            print("Errors:", err)
        sys.exit(code)

    elif command == "log":
        if len(sys.argv) < 4:
            print("Error: Please provide log type and description")
            print("Usage: wiki.py log <type> <description>")
            sys.exit(1)
        log_type = sys.argv[2]
        desc = sys.argv[3]
        code, out, err = run_command(f"cd '{vault_path}' && python3 wiki_ingest_helper.py log '{log_type}' '{desc}'")
        print(out)
        if err:
            print("Errors:", err)
        sys.exit(code)

    elif command == "help":
        main()  # Recursive call to show help
        return

    else:
        print(f"Unknown command: {command}")
        print("Run 'wiki.py help' for usage information")
        sys.exit(1)

if __name__ == "__main__":
    main()