#!/bin/bash
# J.A.R.V.I.S. FREE Setup Script - For Obsidian Vault
# Just A Rather Very Intelligent System

set -e

echo ""
echo "╔══════════════════════════════════════════════════════════════════╗"
echo "║          J.A.R.V.I.S. FREE SETUP ASSISTANT                       ║"
echo "║   Just A Rather Very Intelligent System (Ollama Edition)          ║"
echo "╚══════════════════════════════════════════════════════════════════╝"
echo ""

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Check Python
echo -e "${BLUE}[1/7] Checking Python...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}    ✗ Python 3 not found! Install it first.${NC}"
    exit 1
fi
PYTHON_VERSION=$(python3 --version 2>&1 | grep -oP '\d+\.\d+')
echo -e "${GREEN}    ✓ Python $PYTHON_VERSION found${NC}"

# Check vault location (should be in parent's parent's Obsidian Vault)
echo -e "${BLUE}[2/7] Locating Obsidian Vault...${NC}"
# We're in: /path/to/Obsidian Vault/projects/jarvis
# Vault root is: /path/to/Obsidian Vault
if [[ "$SCRIPT_DIR" == *"Obsidian Vault"* ]]; then
    VAULT_ROOT="$(cd "$SCRIPT_DIR/../../" && pwd)"
    echo -e "${GREEN}    ✓ Vault found: $VAULT_ROOT${NC}"
else
    DEFAULT_VAULT="$HOME/Documents/Obsidian Vault"
    if [[ -d "$DEFAULT_VAULT" ]]; then
        VAULT_ROOT="$DEFAULT_VAULT"
        echo -e "${GREEN}    ✓ Using default vault: $VAULT_ROOT${NC}"
    else
        echo -e "${YELLOW}    ⚠ Could not detect vault automatically${NC}"
        read -p "    Enter your Obsidian vault path: " VAULT_ROOT
    fi
fi

# Check for Ollama
echo -e "${BLUE}[3/7] Checking for Ollama...${NC}"
if command -v ollama &> /dev/null; then
    echo -e "${GREEN}    ✓ Ollama found${NC}"
    OLLAMA_INSTALLED=true
else
    echo -e "${YELLOW}    ⚠ Ollama not found${NC}"
    echo -e "    Will install automatically"
    OLLAMA_INSTALLED=false
fi

# Create virtual environment
echo -e "${BLUE}[4/7] Setting up Python environment...${NC}"
if [[ ! -d "venv" ]]; then
    python3 -m venv venv
    echo -e "${GREEN}    ✓ Virtual environment created${NC}"
else
    echo -e "${GREEN}    ✓ Virtual environment exists${NC}"
fi

# Install dependencies
echo -e "${BLUE}[5/7] Installing Python packages...${NC}"
source venv/bin/activate
pip install --upgrade pip -q
pip install -r requirements.txt -q
echo -e "${GREEN}    ✓ Packages installed${NC}"

# Install Ollama if needed
if [[ "$OLLAMA_INSTALLED" == "false" ]]; then
    echo -e "${BLUE}[6/7] Installing Ollama...${NC}"
    echo "    This will download ~2GB for the LLM model..."
    curl -fsSL https://ollama.com/install.sh | sh
    echo -e "${GREEN}    ✓ Ollama installed${NC}"
fi

# Pull recommended model
if command -v ollama &> /dev/null; then
    echo "    Checking for llama3.2 model..."
    if ! ollama list | grep -q "llama3.2"; then
        echo "    Downloading llama3.2 (this may take a few minutes)..."
        ollama pull llama3.2
    fi
    echo -e "${GREEN}    ✓ Model ready${NC}"
fi

# Configure .env
echo -e "${BLUE}[7/7] Creating configuration...${NC}"
if [[ ! -f ".env" ]]; then
    cp .env.example .env
    # Update vault path
    sed -i "s|OBSIDIAN_VAULT_PATH=.*|OBSIDIAN_VAULT_PATH=$VAULT_ROOT|g" .env
    echo -e "${GREEN}    ✓ Configuration created${NC}"
    echo -e "${YELLOW}    ⚠ Please edit .env and add your OBSIDIAN_API_KEY${NC}"
else
    echo -e "${GREEN}    ✓ Configuration exists${NC}"
fi

chmod +x main.py

echo ""
echo "═══════════════════════════════════════════════════════════════════"
echo "                🎉 SETUP COMPLETE! 🎉"
echo "═══════════════════════════════════════════════════════════════════"
echo ""
echo "✅ JARVIS is installed in your Obsidian vault"
echo ""
echo "NEXT STEPS:"
echo ""
echo "1. INSTALL Obsidian Local REST API plugin:"
echo "   - Open Obsidian → Settings → Community Plugins"
echo "   - Search: 'Local REST API' → Install & Enable"
echo "   - Copy the API key and paste in .env file"
echo ""
echo "2. RUN JARVIS:"
echo "   cd '$VAULT_ROOT/projects/jarvis'"
echo "   source venv/bin/activate"
echo "   python main.py"
echo ""
echo "3. USE QUICK COMMANDS:"
echo "   ./jarvis.sh                        # Start JARVIS"
echo "   ./jarvis.sh --voice               # With voice (if enabled)"
echo "   ./jarvis.sh 'Search Buddhism'     # Single command"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo " FREE FOREVER: Running on Ollama (local LLM)"
echo " Location: $VAULT_ROOT/projects/jarvis"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""