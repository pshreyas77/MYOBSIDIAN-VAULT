#!/usr/bin/env python3
"""
Obsidian Vault Integration Client
Connects to Obsidian via Local REST API plugin
"""

import json
import re
import urllib.request
import urllib.error
from pathlib import Path
from typing import List, Dict, Optional, Any
from config import Config


class ObsidianClient:
    """Client for Obsidian Local REST API"""

    def __init__(self):
        self.api_key = Config.OBSIDIAN_API_KEY
        self.api_port = Config.OBSIDIAN_API_PORT
        self.base_url = f"http://127.0.0.1:{self.api_port}"
        self.vault_path = Path(Config.OBSIDIAN_VAULT_PATH)

    def _request(self, method: str, endpoint: str, data: dict = None) -> Any:
        """Make HTTP request to Obsidian REST API"""
        url = f"{self.base_url}{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            if method == "GET":
                req = urllib.request.Request(url, headers=headers, method="GET")
            elif method in ["POST", "PUT"]:
                json_data = json.dumps(data).encode('utf-8')
                req = urllib.request.Request(url, data=json_data, headers=headers, method=method)
            else:
                req = urllib.request.Request(url, headers=headers, method=method)

            with urllib.request.urlopen(req, timeout=10) as response:
                return json.loads(response.read().decode('utf-8'))

        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8')
            return {"error": f"HTTP {e.code}: {error_body}"}
        except urllib.error.URLError as e:
            return {"error": f"Connection failed: {e.reason}"}
        except Exception as e:
            return {"error": str(e)}

    def is_available(self) -> bool:
        """Check if Obsidian API is running"""
        result = self._request("GET", "/")
        return "error" not in result

    def get_active_file(self) -> Optional[Dict]:
        """Get currently active file in Obsidian"""
        return self._request("GET", "/active/")

    def open_file(self, path: str) -> Dict:
        """Open a file in Obsidian"""
        return self._request("POST", "/open/", {"path": path})

    def read_note(self, path: str) -> Optional[str]:
        """Read the contents of a note"""
        # Normalize path
        path = self._normalize_path(path)

        # Try vault path directly
        full_path = self.vault_path / f"{path}.md"
        if full_path.exists():
            try:
                return full_path.read_text(encoding='utf-8')
            except Exception as e:
                if Config.DEBUG_MODE:
                    print(f"Error reading {full_path}: {e}")
                return None

        # Try common extensions
        for ext in ['.md', '']:
            full_path = self.vault_path / f"{path}{ext}"
            if full_path.exists():
                return full_path.read_text(encoding='utf-8')

        # Try searching
        results = self.search_in_vault(path)
        if results:
            for result in results[:3]:
                full_path = self.vault_path / result
                if full_path.exists():
                    return full_path.read_text(encoding='utf-8')

        return None

    def write_note(self, path: str, content: str, overwrite: bool = False) -> Dict:
        """Create or update a note"""
        path = self._normalize_path(path)
        full_path = self.vault_path / f"{path}.md"

        # Check if exists
        if full_path.exists() and not overwrite:
            return {"error": f"File exists. Use overwrite=true to replace.", "path": str(full_path)}

        try:
            # Ensure directory exists
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.write_text(content, encoding='utf-8')

            return {
                "success": True,
                "path": str(full_path),
                "size": len(content)
            }
        except Exception as e:
            return {"error": str(e)}

    def search_in_vault(self, query: str, limit: int = 10) -> List[str]:
        """Search for files in the vault"""
        results = []
        query_lower = query.lower()

        try:
            for file_path in self.vault_path.rglob("*.md"):
                relative_path = file_path.relative_to(self.vault_path)
                path_str = str(relative_path)

                # Check filename
                if query_lower in file_path.stem.lower():
                    results.append(path_str)
                    if len(results) >= limit:
                        break
                    continue

                # Check content (for small files)
                if file_path.stat().st_size < 100000:  # 100KB limit
                    try:
                        content = file_path.read_text(encoding='utf-8', errors='ignore')
                        if query_lower in content.lower():
                            results.append(path_str)
                            if len(results) >= limit:
                                break
                    except:
                        pass

        except Exception as e:
            if Config.DEBUG_MODE:
                print(f"Search error: {e}")

        return results

    def query_content(self, query: str) -> List[Dict]:
        """Search vault content and return matching notes with context"""
        results = []
        query_lower = query.lower()

        # Search through recent/important files first
        search_paths = [
            self.vault_path / "daily",
            self.vault_path / "notes",
            self.vault_path / "projects",
            self.vault_path / "knowledge",
            self.vault_path,
        ]

        found = set()
        for search_dir in search_paths:
            if not search_dir.exists():
                continue

            try:
                for file_path in search_dir.rglob("*.md"):
                    if len(found) >= 10:
                        break

                    if file_path in found:
                        continue

                    try:
                        content = file_path.read_text(encoding='utf-8', errors='ignore')
                        if query_lower in content.lower():
                            # Find context around match
                            lines = content.split('\n')
                            matching_context = []
                            for i, line in enumerate(lines):
                                if query_lower in line.lower():
                                    start = max(0, i - 2)
                                    end = min(len(lines), i + 3)
                                    matching_context.extend(lines[start:end])
                                    matching_context.append("...")

                            results.append({
                                "path": str(file_path.relative_to(self.vault_path)),
                                "title": file_path.stem,
                                "preview": '\n'.join(matching_context[:10]),
                                "size": len(content)
                            })
                            found.add(file_path)
                    except Exception:
                        pass
            except Exception:
                pass

        return results

    def list_notes(self, folder: str = ".", limit: int = 50) -> List[str]:
        """List notes in a folder"""
        notes = []
        folder_path = self.vault_path / folder

        if not folder_path.exists():
            return []

        try:
            for file_path in folder_path.glob("*.md"):
                notes.append(str(file_path.relative_to(self.vault_path)))
                if len(notes) >= limit:
                    break
        except Exception as e:
            if Config.DEBUG_MODE:
                print(f"List error: {e}")

        return notes

    def get_recent_notes(self, limit: int = 10) -> List[Dict]:
        """Get recently modified notes"""
        notes = []

        try:
            for file_path in self.vault_path.rglob("*.md"):
                try:
                    stat = file_path.stat()
                    notes.append({
                        "path": str(file_path.relative_to(self.vault_path)),
                        "title": file_path.stem,
                        "modified": stat.st_mtime
                    })
                except:
                    pass

            notes.sort(key=lambda x: x["modified"], reverse=True)
        except Exception as e:
            if Config.DEBUG_MODE:
                print(f"Recent error: {e}")

        return notes[:limit]

    def _normalize_path(self, path: str) -> str:
        """Normalize a path for the vault"""
        path = path.strip()
        path = path.replace("\\", "/")
        path = path.lstrip("/")

        # Remove .md extension if present
        if path.endswith(".md"):
            path = path[:-3]

        return path

    def get_stats(self) -> Dict:
        """Get statistics about the vault"""
        total_notes = 0
        total_size = 0
        folders = set()

        try:
            for file_path in self.vault_path.rglob("*.md"):
                total_notes += 1
                total_size += file_path.stat().st_size
                folders.add(file_path.parent.relative_to(self.vault_path))
        except Exception:
            pass

        return {
            "total_notes": total_notes,
            "total_size_mb": round(total_size / (1024 * 1024), 2),
            "folders": len(folders),
            "vault_path": str(self.vault_path)
        }


# Test if run directly
if __name__ == "__main__":
    client = ObsidianClient()
    print(f"Vault: {client.vault_path}")
    print(f"API available: {client.is_available()}")
    print(f"Stats: {client.get_stats()}")