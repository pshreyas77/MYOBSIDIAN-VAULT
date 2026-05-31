#!/usr/bin/env python3
"""
J.A.R.V.I.S. - Just A Rather Very Intelligent System

A personal AI assistant that supports multiple FREE backends:
- Ollama (local, completely free)
- Anthropic Claude (optional - paid API)
- OpenAI-compatible (optional - free tiers)

Usage:
    python main.py                  # Start interactive mode
    python main.py --backend ollama # Force Ollama backend
    python main.py "query"          # Single command mode
"""

import sys
import argparse
import signal
import traceback
from pathlib import Path

project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from config import Config
from obsidian_client import ObsidianClient
from llm_client import LLMClient
from audio_handler import AudioHandler
from tools import ToolRegistry


class JARVIS:
    """J.A.R.V.I.S. Main Controller - FREE VERSION"""

    def __init__(self, voice_mode: bool = False, backend: str = "auto"):
        print("=" * 60)
        print("Initializing J.A.R.V.I.S. systems...")
        print("=" * 60)

        self.voice_mode = voice_mode and Config.VOICE_ENABLED
        self.running = True
        self.backend = backend

        try:
            # Obsidian client
            print("\n[1/4] Connecting to Obsidian vault...")
            self.obsidian = ObsidianClient()
            vault_stats = self.obsidian.get_stats()
            print(f"      ✓ Vault loaded: {vault_stats['total_notes']:,} notes")
            print(f"      ✓ Size: {vault_stats['total_size_mb']} MB")

            # LLM Client (tries Ollama first - FREE)
            print("\n[2/4] Initializing AI backend...")
            Config.validate()
            self.llm = LLMClient(backend=backend)
            print(f"      ✓ Using: {Config.get_llm_info()}")

            # Tools
            print("\n[3/4] Loading tools...")
            self.tools = ToolRegistry(self.obsidian)

            for tool in self.tools.tools:
                self.llm.add_tool(
                    name=tool["name"],
                    description=tool["description"],
                    parameters=tool["parameters"],
                    handler=tool["function"]
                )
            print(f"      ✓ {len(self.tools.tools)} tools registered")

            # Audio handler
            print("\n[4/4] Initializing audio systems...")
            self.audio = AudioHandler()
            audio_status = "Enabled" if self.voice_mode else "Text only"
            print(f"      ✓ Audio: {audio_status}")
            if not Config.VOICE_ENABLED:
                print(f"        (Enable in .env: VOICE_ENABLED=true)")

            print("\n" + "=" * 60)
            self.greet()
            print("=" * 60 + "\n")

        except Exception as e:
            print(f"\n[ERROR] Initialization failed: {e}")
            if Config.DEBUG_MODE:
                traceback.print_exc()
            sys.exit(1)

    def greet(self):
        """Welcome message"""
        import random
        greetings = [
            f"Good day, {Config.USER_NAME}. J.A.R.V.I.S. is at your service.",
            f"Online and ready, {Config.USER_NAME}.",
            f"Systems operational. How may I assist you, {Config.USER_NAME}?",
        ]
        if Config.OLLAMA_ENABLED:
            greetings.append(f"Running locally with Ollama. Ready to assist you, {Config.USER_NAME}.")

        greeting = random.choice(greetings)
        print(f"  {Config.JARVIS_NAME}: {greeting}")

        if self.voice_mode and Config.TEXT_TO_SPEECH_ENABLED:
            self.audio.speak(greeting)

    def process_command(self, user_input: str) -> str:
        """Process user input"""
        cmd = user_input.strip().lower()

        # Special commands
        if cmd in ['exit', 'quit', 'shutdown', 'goodbye']:
            return self.shutdown()
        if cmd == 'help':
            return self.show_help()
        if cmd == 'clear':
            print("\n" * 50)
            return "Screen cleared."
        if cmd == 'status':
            return self.show_status()
        if cmd == 'voice on':
            self.voice_mode = Config.VOICE_ENABLED
            return f"Voice mode {'enabled' if self.voice_mode else 'unavailable. Check .env settings.'}."
        if cmd == 'voice off':
            self.voice_mode = False
            return "Voice mode disabled."

        # Quick vault commands
        if any(cmd.startswith(x) for x in ['read ', 'show ', 'open ']):
            words = user_input.split()
            if len(words) > 1:
                note_path = ' '.join(words[1:])
                content = self.obsidian.read_note(note_path)
                if content:
                    return f"**{note_path}**\n\n{content[:2000]}"
                return f"Note '{note_path}' not found."

        if cmd.startswith('search '):
            query = user_input[7:].strip()
            return self.tools.search_vault(query)

        # Send to LLM
        try:
            return self.llm.chat(user_input, use_tools=True)
        except Exception as e:
            if Config.DEBUG_MODE:
                traceback.print_exc()
            return f"Error: {str(e)}. Please check your backend configuration."

    def shutdown(self) -> str:
        """Shutdown"""
        self.running = False
        farewell = f"Shutting down. Goodbye, {Config.USER_NAME}."
        print(f"  {Config.JARVIS_NAME}: {farewell}")

        if self.voice_mode:
            self.audio.speak(farewell, block=True)
        return ""

    def show_help(self) -> str:
        return """📚 J.A.R.V.I.S. Commands

Navigation:
  help              Show this help
  status            System status
  exit/quit         Shutdown
  clear             Clear screen

Vault Commands:
  read <note>       Read a note by path
  search <query>    Search vault
  show <note>       Display note

Settings:
  voice on/off      Toggle voice

You can ask anything naturally!
Examples:
  "What do I know about Buddhism?"
  "Create a note about meditation"
  "What was I working on last week?"
"""

    def show_status(self) -> str:
        stats = self.obsidian.get_stats()
        llm_info = Config.get_llm_info()

        return f"""🔧 System Status:

AI Backend: {llm_info}

📓 Vault: {stats['vault_path']}
   Notes: {stats['total_notes']:,}
   Size: {stats['total_size_mb']} MB

🔊 Voice: {'Enabled' if self.voice_mode else 'Disabled'}
   TTS: {'Enabled' if Config.TEXT_TO_SPEECH_ENABLED else 'Disabled'}
"""

    def interactive_loop(self):
        """Main interaction loop"""
        print("Type 'help' for commands, 'exit' to quit.\n")

        while self.running:
            try:
                if self.voice_mode:
                    print("🎤 Listening...")
                    user_input = self.audio.listen()
                    if not user_input:
                        print("⚠ Could not understand.\n")
                        continue
                    print(f"You: {user_input}")
                else:
                    user_input = input("You: ").strip()

                if not user_input:
                    continue

                response = self.process_command(user_input)

                if not self.running:
                    break

                print(f"{Config.JARVIS_NAME}: {response}\n")

                if self.voice_mode and response:
                    self.audio.speak(response[:400])

            except KeyboardInterrupt:
                print("\n")
                self.shutdown()
                break
            except EOFError:
                break
            except Exception as e:
                print(f"Error: {e}")
                if Config.DEBUG_MODE:
                    traceback.print_exc()

    def run_single(self, query: str):
        """Single query mode"""
        response = self.process_command(query)
        print(response)
        self.running = False


def main():
    parser = argparse.ArgumentParser(
        description="J.A.R.V.I.S. - Personal AI Assistant (FREE VERSION)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                          # Start with Ollama (FREE)
  %(prog)s --voice                  # Voice mode
  %(prog)s --backend ollama         # Force Ollama
  %(prog)s "Search vault Buddhism"  # Single command

Free Backends:
  Ollama  - Local, completely free (ollama.com)
  NVIDIA  - Free tier API (build.nvidia.com)
  DeepSeek - Free tier available

See .env.example for configuration.
        """
    )
    parser.add_argument('--voice', '-v', action='store_true',
                       help='Enable voice input/output')
    parser.add_argument('--backend', '-b', default='auto',
                       choices=['auto', 'ollama', 'anthropic', 'openai'],
                       help='LLM backend to use (default: auto)')
    parser.add_argument('query', nargs='?',
                       help='Single query to process')

    args = parser.parse_args()

    signal.signal(signal.SIGINT, lambda s, f: sys.exit(0))

    try:
        jarvis = JARVIS(voice_mode=args.voice, backend=args.backend)

        if args.query:
            jarvis.run_single(args.query)
        else:
            jarvis.interactive_loop()

    except ValueError as e:
        print(f"\n❌ Configuration Error:\n{e}\n")
        print("Quick Setup (FREE - Ollama):")
        print("1. Install Ollama: curl -fsSL https://ollama.com/install.sh | sh")
        print("2. Pull model: ollama pull llama3.2")
        print("3. Start Ollama: ollama serve")
        print("4. Run JARVIS: python main.py")
        print("\nOr use .env to configure API-based models.")
        sys.exit(1)


if __name__ == "__main__":
    main()