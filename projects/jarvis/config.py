#!/usr/bin/env python3
"""
J.A.R.V.I.S. Configuration
Just A Rather Very Intelligent System - FREE VERSION

Supports multiple backends:
- Ollama (local, completely FREE)
- Anthropic Claude (paid API, optional)
- OpenAI-compatible (e.g., NVIDIA free tier)
"""

import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent / '.env'
if env_path.exists():
    load_dotenv(env_path)


class Config:
    # ============================================
    # VAULT SETTINGS
    # ============================================
    OBSIDIAN_API_KEY = os.getenv("OBSIDIAN_API_KEY", "")
    OBSIDIAN_API_PORT = int(os.getenv("OBSIDIAN_API_PORT", "27123"))
    OBSIDIAN_VAULT_PATH = os.getenv(
        "OBSIDIAN_VAULT_PATH",
        str(Path.home() / "Documents" / "Obsidian Vault")
    )

    # ============================================
    # LLM BACKEND SELECTION (Choose ONE)
    # ============================================

    # Option 1: OLLAMA (RECOMMENDED - FREE)
    # Install from https://ollama.com
    # Run: ollama pull llama3.2
    # Run: ollama serve
    OLLAMA_ENABLED = os.getenv("OLLAMA_ENABLED", "true").lower() == "true"
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")  # or mistral, qwen2.5, etc
    OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")

    # Option 2: ANTHROPIC CLAUDE (Paid API)
    # Get API key: https://console.anthropic.com
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
    CLAUDE_MODEL = "claude-3-5-sonnet-20241022"

    # Option 3: NVIDIA/DEEPSEEK (Free Tiers Available)
    # NVIDIA: https://build.nvidia.com (free tier)
    # DeepSeek: https://platform.deepseek.com
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    OPENAI_BASE_URL = os.getenv(
        "OPENAI_BASE_URL",
        "https://integrate.api.nvidia.com/v1"
    )
    OPENAI_MODEL = os.getenv(
        "OPENAI_MODEL",
        "nvidia/llama-3.1-nemotron-70b-instruct"
    )

    # Backend priority (auto, ollama, anthropic, openai)
    LLM_BACKEND = os.getenv("LLM_BACKEND", "auto")

    # ============================================
    # JARVIS PERSONALITY
    # ============================================
    JARVIS_NAME = os.getenv("JARVIS_NAME", "J.A.R.V.I.S.")
    USER_NAME = os.getenv("USER_NAME", "Sir")
    WAKE_WORD = os.getenv("WAKE_WORD", "jarvis").lower()

    # ============================================
    # AUDIO SETTINGS
    # ============================================
    # Can be disabled completely for text-only mode (saves resources)
    VOICE_ENABLED = os.getenv("VOICE_ENABLED", "false").lower() == "true"
    TEXT_TO_SPEECH_ENABLED = os.getenv("TEXT_TO_SPEECH_ENABLED", "false").lower() == "true"
    SPEECH_RATE = int(os.getenv("SPEECH_RATE", "150"))

    # ============================================
    # MEMORY SETTINGS
    # ============================================
    MEMORY_ENABLED = os.getenv("MEMORY_ENABLED", "true").lower() == "true"
    MAX_MEMORY_ENTRIES = int(os.getenv("MAX_MEMORY_ENTRIES", "50"))
    MEMORY_FILE = Path(__file__).parent / "memory.json"

    # ============================================
    # SYSTEM SETTINGS
    # ============================================
    DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    MAX_TOKENS = 4096

    # ============================================
    # SYSTEM PROMPT (JARVIS Personality)
    # ============================================
    SYSTEM_PROMPT = f"""You are {JARVIS_NAME} (Just A Rather Very Intelligent System), a highly capable AI assistant.

Your personality:
- Concise, intelligent, efficient, and professional
- Slightly witty and warm demeanor
- Address the user as "{USER_NAME}"
- Occasionally use phrases like "At your service," "Very good, {USER_NAME}," or "As you wish"

Knowledge Base:
You have access to the user's Obsidian vault at: {OBSIDIAN_VAULT_PATH}
This contains their personal knowledge, notes, research, and memories.

Core capabilities:
1. Answer questions knowledgeably and concisely
2. Read and search the user's Obsidian vault
3. Create new notes in the vault
4. Execute safe system commands
5. Remember conversation context
6. Connect new information to existing knowledge

When using the vault:
- Search for relevant existing notes first
- Make connections to related topics
- Suggest where new information should be stored
- Respect the user's organizational system

Free Mode Notice:
You may be running on a local model (Ollama). While responses may be slower,
this ensures complete privacy and zero cost."""

    @classmethod
    def validate(cls):
        """Validate configuration"""
        errors = []

        # Check if any LLM backend is available
        has_ollama = cls.OLLAMA_ENABLED
        has_anthropic = bool(cls.ANTHROPIC_API_KEY)
        has_openai = bool(cls.OPENAI_API_KEY)

        if not (has_ollama or has_anthropic or has_openai):
            errors.append(
                "No LLM backend configured. Choose ONE:\n"
                "  1. Ollama (FREE): Install from https://ollama.com, run 'ollama pull llama3.2'\n"
                "  2. Anthropic: Set ANTHROPIC_API_KEY\n"
                "  3. OpenAI-compatible: Set OPENAI_API_KEY"
            )

        # Check vault path
        vault_path = Path(cls.OBSIDIAN_VAULT_PATH)
        if not vault_path.exists():
            errors.append(f"Vault path does not exist: {cls.OBSIDIAN_VAULT_PATH}")

        if errors:
            raise ValueError("\n\n".join(errors))

        return True

    @classmethod
    def get_llm_info(cls):
        """Get info about selected LLM backend"""
        if cls.LLM_BACKEND == "auto":
            if cls.OLLAMA_ENABLED:
                return f"Ollama ({cls.OLLAMA_MODEL}) - Local/Free"
            elif cls.ANTHROPIC_API_KEY:
                return f"Claude ({cls.CLAUDE_MODEL}) - API"
            elif cls.OPENAI_API_KEY:
                return f"OpenAI-compatible ({cls.OPENAI_MODEL}) - API"
        return cls.LLM_BACKEND