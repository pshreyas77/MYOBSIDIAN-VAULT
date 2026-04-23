#!/usr/bin/env python3
"""
Professional Wiki Enhancer for Obsidian Vault
Safely adds links and connections using additive-only operations
"""

import os
import re
import subprocess
from pathlib import Path
import datetime
import sys

def get_vault_path():
    """Get the Obsidian vault path"""
    return Path("/home/sunny77/Documents/Obsidian Vault")

def get_wiki_path():
    """Get the wiki path"""
    return get_vault_path() / "wiki"

def safe_read_file(file_path):
    """Safely read a file, returning empty string on error"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}")
        return ""

def safe_write_file(file_path, content):
    """Safely write content to a file"""
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error writing to {file_path}: {e}")
        return False

def extract_links(content):
    """Extract all wiki-style links from content"""
    pattern = r'\[\[([^\]]+)\]\]'
    matches = re.findall(pattern, content)
    links = []
    for match in matches:
        clean_link = match.split('|')[0].strip()
        if clean_link:
            links.append(clean_link)
    return links

def add_see_also_section(note_path, links_to_add):
    """Add a 'See Also' section to a note with the specified links"""
    content = safe_read_file(note_path)
    if not content:
        return False

    # Check if there's already a See Also section
    see_also_pattern = r'\n## See Also\n'
    if re.search(see_also_pattern, content):
        # Add to existing See Also section
        lines = content.split('\n')
        new_lines = []
        in_see_also = False

        for line in lines:
            new_lines.append(line)
            if line.strip() == '## See Also':
                in_see_also = True
                # Add our links after the header
                for link_info in links_to_add:
                    link_text = f"- {link_info['link']}"
                    if 'description' in link_info and link_info['description']:
                        link_text += f" - {link_info['description']}"
                    new_lines.append(link_text)
            elif line.startswith('## ') and in_see_also and line != '## See Also':
                # We've moved past the See Also section
                in_see_also = False

        # If we never left the See Also section (it was at the end), add links at the end
        if in_see_also:
            for link_info in links_to_add:
                link_text = f"- {link_info['link']}"
                if 'description' in link_info and link_info['description']:
                    link_text += f" - {link_info['description']}"
                new_lines.append(link_text)

        new_content = '\n'.join(new_lines)
    else:
        # Add new See Also section at the end
        see_also_content = '\n## See Also\n'
        for link_info in links_to_add:
            link_text = f"- {link_info['link']}"
            if 'description' in link_info and link_info['description']:
                link_text += f" - {link_info['description']}"
            see_also_content += link_text + '\n'

        new_content = content.rstrip() + see_also_content

    return safe_write_file(note_path, new_content)

def add_inline_enhancement(note_path, enhancements):
    """Add inline contextual enhancements to a note"""
    content = safe_read_file(note_path)
    if not content:
        return False

    # For simplicity, we'll add enhancements at the end of the file
    # In a more sophisticated version, we could insert at specific contexts
    inline_content = '\n'
    for enhancement in enhancements:
        inline_content += enhancement['text'] + '\n'

    new_content = content.rstrip() + inline_content
    return safe_write_file(note_path, new_content)

def enhance_frontmatter(note_path, frontmatter_additions):
    """Add to existing frontmatter (never remove)"""
    content = safe_read_file(note_path)
    if not content:
        return False

    # Check if file starts with frontmatter
    if content.startswith('---'):
        # Find the end of frontmatter
        lines = content.split('\n')
        end_idx = -1
        for i, line in enumerate(lines[1:], 1):  # Start after first line
            if line.strip() == '---':
                end_idx = i
                break

        if end_idx != -1:
            # Insert our additions before the closing ---
            frontmatter_lines = []
            for key, value in frontmatter_additions.items():
                if isinstance(value, list):
                    value_str = ', '.join([f'"{v}"' if isinstance(v, str) and ':' in v else str(v) for v in value])
                else:
                    value_str = f'"{value}"' if isinstance(value, str) and ':' in value else str(value)
                frontmatter_lines.append(f"{key}: {value_str}")

            # Insert before the closing ---
            lines = lines[:end_idx] + frontmatter_lines + lines[end_idx:]
            new_content = '\n'.join(lines)
            return safe_write_file(note_path, new_content)

    # If no existing frontmatter or couldn't parse, create new frontmatter
    frontmatter_content = '---\n'
    for key, value in frontmatter_additions.items():
        if isinstance(value, list):
            value_str = ', '.join([f'"{v}"' if isinstance(v, str) and ':' in v else str(v) for v in value])
        else:
            value_str = f'"{value}"' if isinstance(value, str) and ':' in value else str(value)
        frontmatter_content += f"{key}: {value_str}\n"
    frontmatter_content += '---\n'

    new_content = frontmatter_content + content
    return safe_write_file(note_path, new_content)

def add_structural_block(note_path, block_content):
    """Add a structural connection block to a note"""
    content = safe_read_file(note_path)
    if not content:
        return False

    # Add block at the end
    new_content = content.rstrip() + '\n' + block_content.strip() + '\n'
    return safe_write_file(note_path, new_content)

def preview_change(note_path, change_func, *args, **kwargs):
    """Preview what a change would look like without applying it"""
    content = safe_read_file(note_path)
    if not content:
        return None, "Could not read file"

    # Create a copy to modify
    import tempfile
    import os
    temp_path = note_path.with_suffix('.md.preview')

    try:
        # Write current content to temp file
        with open(temp_path, 'w', encoding='utf-8') as f:
            f.write(content)

        # Apply change to temp file
        # We need to simulate the change - for now, we'll just describe what would happen
        # In a real implementation, we'd call the change function on the temp file

        # For preview, we'll read back and show diff-like output
        # Since we're not actually modifying, we'll just return what would be added
        return content, "Preview functionality would show exact diff here"
    finally:
        # Clean up temp file
        if temp_path.exists():
            temp_path.unlink()

def main():
    """Main function for command line usage"""
    import sys

    if len(sys.argv) < 2:
        print("Usage: wiki_enhancer.py <command> [args]")
        print("Commands:")
        print("  see-also <note_path> <link> [description]  - Add See Also link")
        print("  inline <note_path> <text>                  - Add inline enhancement")
        print("  frontmatter <note_path> <key>=<value> ... - Add to frontmatter")
        print("  block <note_path> <block_content>          - Add structural block")
        print("  preview <note_path> <change_type> ...     - Preview changes")
        print("  help                                       - Show this help")
        return

    command = sys.argv[1].lower()

    if command == "see-also":
        if len(sys.argv) < 4:
            print("Error: Please provide note path and link")
            print("Usage: wiki_enhancer.py see-also <note_path> <link> [description]")
            return

        note_path = get_vault_path() / sys.argv[2]
        link = sys.argv[3]
        description = sys.argv[4] if len(sys.argv) > 4 else ""

        links_to_add = [{'link': f'[[{link}]]', 'description': description}]

        print(f"Adding See Also link to {note_path}: {link}")
        if description:
            print(f"  With description: {description}")

        if add_see_also_section(note_path, links_to_add):
            print("✅ Successfully added See Also section")
        else:
            print("❌ Failed to add See Also section")

    elif command == "inline":
        if len(sys.argv) < 4:
            print("Error: Please provide note path and enhancement text")
            print("Usage: wiki_enhancer.py inline <note_path> <text>")
            return

        note_path = get_vault_path() / sys.argv[2]
        text = sys.argv[3]

        enhancements = [{'text': text}]

        print(f"Adding inline enhancement to {note_path}")
        print(f"  Text: {text}")

        if add_inline_enhancement(note_path, enhancements):
            print("✅ Successfully added inline enhancement")
        else:
            print("❌ Failed to add inline enhancement")

    elif command == "frontmatter":
        if len(sys.argv) < 4:
            print("Error: Please provide note path and at least one key=value pair")
            print("Usage: wiki_enhancer.py frontmatter <note_path> <key>=<value> ...")
            return

        note_path = get_vault_path() / sys.argv[2]
        frontmatter_additions = {}

        for arg in sys.argv[3:]:
            if '=' in arg:
                key, value = arg.split('=', 1)
                # Try to convert value to appropriate type
                if value.lower() == 'true':
                    value = True
                elif value.lower() == 'false':
                    value = False
                elif value.isdigit():
                    value = int(value)
                elif value.replace('.', '').isdigit():
                    value = float(value)
                frontmatter_additions[key] = value
            else:
                print(f"Warning: Ignoring invalid argument '{arg}' (expected key=value)")

        print(f"Adding to frontmatter of {note_path}:")
        for key, value in frontmatter_additions.items():
            print(f"  {key}: {value}")

        if enhance_frontmatter(note_path, frontmatter_additions):
            print("✅ Successfully enhanced frontmatter")
        else:
            print("❌ Failed to enhance frontmatter")

    elif command == "block":
        if len(sys.argv) < 4:
            print("Error: Please provide note path and block content")
            print("Usage: wiki_enhancer.py block <note_path> <block_content>")
            return

        note_path = get_vault_path() / sys.argv[2]
        # Join remaining args as block content
        block_content = ' '.join(sys.argv[3:])

        print(f"Adding structural block to {note_path}")
        print(f"  Content: {block_content[:100]}{'...' if len(block_content) > 100 else ''}")

        if add_structural_block(note_path, block_content):
            print("✅ Successfully added structural block")
        else:
            print("❌ Failed to add structural block")

    elif command == "preview":
        print("Preview functionality - would show exact changes before applying")
        print("To be implemented in future version")

    elif command == "help":
        main()  # Recursive call to show help
        return

    else:
        print(f"Unknown command: {command}")
        print("Run 'wiki_enhancer.py help' for usage information")

if __name__ == "__main__":
    main()