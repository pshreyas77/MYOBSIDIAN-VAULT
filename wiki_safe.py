#!/usr/bin/env python3
"""
LLM Wiki Safe - Safety-enhanced CLI for managing your LLM Wiki second brain system.
This version adds extra protection layers to prevent accidental data loss.
"""

import subprocess
import sys
import os
from pathlib import Path

# Import safety wrapper
sys.path.append(str(Path(__file__).parent))
try:
    from wiki_safety_wrapper import safe_execute, show_recovery_instructions, get_vault_path
    SAFETY_AVAILABLE = True
except ImportError:
    SAFETY_AVAILABLE = False
    print("⚠️  Warning: Safety wrapper not available - running in basic mode")

def run_command(cmd):
    """Run a command and return the result"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)

def wiki_init():
    """Initialize the LLM Wiki system"""
    return run_command(f"cd '{get_vault_path()}' && python3 wiki_ingest_helper.py init")

def wiki_source(file_path, title=""):
    """Create source summary from file"""
    if title:
        return run_command(f"cd '{get_vault_path()}' && python3 wiki_ingest_helper.py source '{file_path}' '{title}'")
    else:
        return run_command(f"cd '{get_vault_path()}' && python3 wiki_ingest_helper.py source '{file_path}'")

def wiki_query(question, answer, related_pages=None):
    """Save query answer to wiki"""
    if related_pages is None:
        related_pages = []
    related_str = " ".join(related_pages)
    if related_str:
        return run_command(f"cd '{get_vault_path()}' && python3 wiki_query_helper.py '{question}' '{answer}' {related_str}")
    else:
        return run_command(f"cd '{get_vault_path()}' && python3 wiki_query_helper.py '{question}' '{answer}'")

def wiki_lint(subcommand="full"):
    """Run wiki health checks"""
    return run_command(f"cd '{get_vault_path()}' && python3 wiki_lint_helper.py {subcommand}")

def wiki_index():
    """Update wiki index and statistics"""
    return run_command(f"cd '{get_vault_path()}' && python3 wiki_ingest_helper.py index")

def wiki_log(log_type, description):
    """Log custom operation"""
    return run_command(f"cd '{get_vault_path()}' && python3 wiki_ingest_helper.py log '{log_type}' '{description}'")

def show_help():
    """Show help information"""
    print("LLM Wiki Safe CLI - Manage your Obsidian second brain with extra protections")
    print("")
    print("Usage: wiki_safe.py <command> [args]")
    print("")
    print("Commands:")
    print("  init                    - Initialize the LLM Wiki system")
    print("  source <file> [title]   - Create source summary from file")
    print("  query <question> '<answer>' [related...] - Save query answer to wiki")
    print("  lint [full|orphans|stale|missing] - Run wiki health checks")
    print("  index                   - Update wiki index and statistics")
    print("  log <type> <desc>       - Log custom operation")
    print("  safety                  - Show safety and recovery information")
    print("  help                    - Show this help")
    print("")
    print("Examples:")
    print("  wiki_safe.py init")
    print("  wiki_safe.py source '04 - RESOURCES/Inbox/article.pdf' 'Article Title'")
    print("  wiki_safe.py query 'What is AI?' 'Artificial Intelligence is...' [[LLM]] [[Machine Learning]]")
    print("  wiki_safe.py lint full")
    print("")
    if SAFETY_AVAILABLE:
        print("🛡️  SAFETY FEATURES ENABLED:")
        print("   • Pre-operation git backup")
        print("   • Uncommitted changes warning")
        print("   • Additive-only operations")
        print("   • Clear recovery instructions")
    else:
        print("⚠️  SAFETY WRAPPER NOT AVAILABLE - running basic mode")
    print("")

def show_safety_info():
    """Show safety and recovery information"""
    if SAFETY_AVAILABLE:
        show_recovery_instructions()
    else:
        print("Safety wrapper not available.")
        print("Basic safety principles still apply:")
        print("  • All operations are additive-only (create new files only)")
        print("  • No existing files are modified or deleted")
        print("  • Work happens in wiki/ directory and subdirectories")
        print("  • Use git status/diff to review changes")
        print("  • Use git checkout -- . to revert if needed")

def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1].lower()
    vault_path = get_vault_path() if SAFETY_AVAILABLE else Path("/home/sunny77/Documents/Obsidian Vault")

    # Safety-enabled command functions
    def safe_init():
        if SAFETY_AVAILABLE:
            return safe_execute(wiki_init, "LLM Wiki initialization")
        else:
            return wiki_init()

    def safe_source(file_path, title=""):
        if SAFETY_AVAILABLE:
            return safe_execute(lambda: wiki_source(file_path, title), f"Source ingestion: {file_path}")
        else:
            return wiki_source(file_path, title)

    def safe_query(question, answer, related_pages=None):
        if SAFETY_AVAILABLE:
            return safe_execute(lambda: wiki_query(question, answer, related_pages), f"Query processing: {question[:50]}...")
        else:
            return wiki_query(question, answer, related_pages)

    def safe_lint(subcommand="full"):
        if SAFETY_AVAILABLE:
            return safe_execute(lambda: wiki_lint(subcommand), f"Wiki lint: {subcommand}")
        else:
            return wiki_lint(subcommand)

    def safe_index():
        if SAFETY_AVAILABLE:
            return safe_execute(wiki_index, "Wiki index update")
        else:
            return wiki_index()

    def safe_log(log_type, description):
        if SAFETY_AVAILABLE:
            return safe_execute(lambda: wiki_log(log_type, description), f"Log operation: {log_type}")
        else:
            return wiki_log(log_type, description)

    # Execute commands
    if command == "init":
        code, out, err = safe_init()
        print(out)
        if err:
            print("Errors:", err)
        sys.exit(code)

    elif command == "source":
        if len(sys.argv) < 3:
            print("Error: Please provide a source file path")
            print("Usage: wiki_safe.py source <file> [title]")
            sys.exit(1)
        file_path = sys.argv[2]
        title = sys.argv[3] if len(sys.argv) > 3 else ""
        code, out, err = safe_source(file_path, title)
        print(out)
        if err:
            print("Errors:", err)
        sys.exit(code)

    elif command == "query":
        if len(sys.argv) < 4:
            print("Error: Please provide question and answer")
            print("Usage: wiki_safe.py query <question> '<answer>' [related_pages...]")
            sys.exit(1)
        question = sys.argv[2]
        answer = sys.argv[3]
        related = sys.argv[4:] if len(sys.argv) > 4 else []
        code, out, err = safe_query(question, answer, related)
        print(out)
        if err:
            print("Errors:", err)
        sys.exit(code)

    elif command == "lint":
        subcommand = sys.argv[2] if len(sys.argv) > 2 else "full"
        code, out, err = safe_lint(subcommand)
        print(out)
        if err:
            print("Errors:", err)
        sys.exit(code)

    elif command == "index":
        code, out, err = safe_index()
        print(out)
        if err:
            print("Errors:", err)
        sys.exit(code)

    elif command == "log":
        if len(sys.argv) < 4:
            print("Error: Please provide log type and description")
            print("Usage: wiki_safe.py log <type> <description>")
            sys.exit(1)
        log_type = sys.argv[2]
        desc = sys.argv[3]
        code, out, err = safe_log(log_type, desc)
        print(out)
        if err:
            print("Errors:", err)
        sys.exit(code)

    elif command == "safety":
        show_safety_info()
        return

    elif command == "help":
        show_help()
        return

    else:
        print(f"Unknown command: {command}")
        print("Run 'wiki_safe.py help' for usage information")
        sys.exit(1)

if __name__ == "__main__":
    main()