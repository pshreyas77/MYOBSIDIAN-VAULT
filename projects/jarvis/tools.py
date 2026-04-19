#!/usr/bin/env python3
"""
J.A.R.V.I.S. Tools
Available commands for the AI assistant
"""

import subprocess
import os
import json
from datetime import datetime
from typing import Dict, Any, List
from pathlib import Path
from config import Config


class ToolRegistry:
    """Registry of tools available to JARVIS"""

    def __init__(self, obsidian_client=None):
        self.obsidian = obsidian_client
        self._build_tools()

    def _build_tools(self):
        """Define all available tools"""
        self.tools = [
            {
                "name": "search_vault",
                "description": "Search your Obsidian vault for notes containing specific text",
                "parameters": {
                    "query": {
                        "type": "string",
                        "description": "The search query to look for in your vault"
                    }
                },
                "function": self.search_vault
            },
            {
                "name": "read_note",
                "description": "Read the contents of a specific note from your Obsidian vault",
                "parameters": {
                    "path": {
                        "type": "string",
                        "description": "The path to the note (e.g., 'projects/AI Research' or 'daily/2024-01-15')"
                    }
                },
                "function": self.read_note
            },
            {
                "name": "write_note",
                "description": "Create or update a note in your Obsidian vault",
                "parameters": {
                    "path": {
                        "type": "string",
                        "description": "Path where the note should be saved (without .md extension)"
                    },
                    "content": {
                        "type": "string",
                        "description": "The content to write to the note"
                    }
                },
                "function": self.write_note
            },
            {
                "name": "create_daily_note",
                "description": "Create a note for today's daily log with the current time",
                "parameters": {
                    "content": {
                        "type": "string",
                        "description": "The content to add to today's daily note"
                    }
                },
                "function": self.create_daily_note
            },
            {
                "name": "get_vault_stats",
                "description": "Get statistics about your Obsidian vault (total notes, size, etc.)",
                "parameters": {},
                "function": self.get_vault_stats
            },
            {
                "name": "execute_command",
                "description": "Execute a safe shell command (limited set: ls, cat, echo, date, cd, open, xdg-open)",
                "parameters": {
                    "command": {
                        "type": "string",
                        "description": "The command to execute"
                    }
                },
                "function": self.execute_command
            },
            {
                "name": "open_website",
                "description": "Open a website or URL in the default browser",
                "parameters": {
                    "url": {
                        "type": "string",
                        "description": "The URL to open"
                    }
                },
                "function": self.open_website
            },
            {
                "name": "get_current_time",
                "description": "Get the current date and time",
                "parameters": {},
                "function": self.get_current_time
            },
            {
                "name": "list_recent_notes",
                "description": "Get a list of recently modified notes in the vault",
                "parameters": {
                    "limit": {
                        "type": "integer",
                        "description": "Number of notes to return (default 10)"
                    }
                },
                "function": self.list_recent_notes
            },
            {
                "name": "find_related_notes",
                "description": "Find notes related to a given topic by searching the vault",
                "parameters": {
                    "topic": {
                        "type": "string",
                        "description": "The topic to find related notes for"
                    }
                },
                "function": self.find_related_notes
            }
        ]

        self.tool_map = {t["name"]: t for t in self.tools}

    def get_tools_for_claude(self) -> List[Dict]:
        """Get tools in Claude API format"""
        return [
            {
                "name": t["name"],
                "description": t["description"],
                "parameters": t["parameters"]
            }
            for t in self.tools
        ]

    def execute(self, name: str, **kwargs) -> str:
        """Execute a tool by name"""
        if name not in self.tool_map:
            return f"Error: Tool '{name}' not found"

        try:
            return self.tool_map[name]["function"](**kwargs)
        except Exception as e:
            return f"Error executing {name}: {str(e)}"

    def search_vault(self, query: str) -> str:
        """Search vault for notes"""
        if not self.obsidian:
            return "Error: Obsidian client not available"

        results = self.obsidian.search_in_vault(query)
        if not results:
            return f"No notes found matching '{query}'"

        formatted = f"Found {len(results)} note(s) matching '{query}':\n\n"
        for result in results[:10]:
            formatted += f"- {result}\n"

        return formatted

    def read_note(self, path: str) -> str:
        """Read a note from vault"""
        if not self.obsidian:
            return "Error: Obsidian client not available"

        content = self.obsidian.read_note(path)
        if content is None:
            return f"Note '{path}' not found in vault"

        # Truncate if too long
        if len(content) > 4000:
            content = content[:4000] + "\n\n[Note truncated due to length]"

        return f"Content of '{path}':\n\n{content}"

    def write_note(self, path: str, content: str) -> str:
        """Write a note to vault"""
        if not self.obsidian:
            return "Error: Obsidian client not available"

        # Add metadata header
        header = f"""---
created: {datetime.now().isoformat()}
---

"""
        full_content = header + content

        result = self.obsidian.write_note(path, full_content)

        if "error" in result:
            return f"Error: {result['error']}"

        return f"Successfully created note at '{path}'"

    def create_daily_note(self, content: str) -> str:
        """Create a note in the daily folder"""
        today = datetime.now().strftime("%Y-%m-%d")
        path = f"daily/{today}"

        # Try to append to existing
        existing = self.obsidian.read_note(path)
        if existing:
            time_str = datetime.now().strftime("%H:%M")
            new_content = existing + f"\n\n## {time_str}\n\n{content}"
            result = self.obsidian.write_note(path, new_content, overwrite=True)
        else:
            result = self.obsidian.write_note(path, content)

        if "error" in result:
            return f"Error: {result['error']}"

        return f"Added to daily note for {today}"

    def get_vault_stats(self) -> str:
        """Get vault statistics"""
        if not self.obsidian:
            return "Error: Obsidian client not available"

        stats = self.obsidian.get_stats()
        return f"""Vault Statistics:
- Total notes: {stats['total_notes']}
- Total size: {stats['total_size_mb']} MB
- Folders: {stats['folders']}
- Location: {stats['vault_path']}"""

    def execute_command(self, command: str) -> str:
        """Execute a safe shell command"""
        # Whitelist of safe commands
        safe_prefixes = ('ls', 'cat', 'echo', 'date', 'pwd', 'which', 'whoami', 'who', 'df', 'free')

        if not any(command.strip().startswith(p) for p in safe_prefixes):
            return f"Command rejected for security. Only these prefixes allowed: {safe_prefixes}"

        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=10
            )

            output = result.stdout
            if result.stderr:
                output += f"\n\n[STDERR]: {result.stderr}"

            if result.returncode != 0:
                return f"Command failed (exit {result.returncode}):\n{output}"

            return f"Command output:\n{output}"

        except subprocess.TimeoutExpired:
            return "Command timed out after 10 seconds"
        except Exception as e:
            return f"Command error: {str(e)}"

    def open_website(self, url: str) -> str:
        """Open a website"""
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        try:
            subprocess.Popen(['xdg-open', url],
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
            return f"Opening {url} in browser"
        except Exception as e:
            return f"Error opening website: {str(e)}"

    def get_current_time(self) -> str:
        """Get current time"""
        now = datetime.now()
        return now.strftime("Current date and time: %A, %B %d, %Y at %I:%M %p")

    def list_recent_notes(self, limit: int = 10) -> str:
        """List recently modified notes"""
        if not self.obsidian:
            return "Error: Obsidian client not available"

        notes = self.obsidian.get_recent_notes(limit)
        if not notes:
            return "No recent notes found"

        formatted = f"Last {len(notes)} modified notes:\n\n"
        for note in notes:
            mod_time = datetime.fromtimestamp(note['modified']).strftime('%Y-%m-%d %H:%M')
            formatted += f"- {note['path']} (modified {mod_time})\n"

        return formatted

    def find_related_notes(self, topic: str) -> str:
        """Find notes related to a topic"""
        if not self.obsidian:
            return "Error: Obsidian client not available"

        # Search in vault
        results = self.obsidian.query_content(topic)

        if not results:
            return f"No notes found related to '{topic}'"

        formatted = f"Notes related to '{topic}':\n\n"
        for result in results[:5]:
            formatted += f"## {result['title']}\n"
            formatted += f"**Path:** {result['path']}\n"
            formatted += f"**Preview:**\n{result['preview'][:500]}...\n\n"

        return formatted