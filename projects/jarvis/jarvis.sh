#!/bin/bash
# J.A.R.V.I.S. Launcher Script
# Quick launcher for the assistant

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Check if virtual environment exists
if [[ ! -d "venv" ]]; then
    echo "Virtual environment not found. Running setup..."
    bash setup.sh
fi

# Activate venv and run
source venv/bin/activate
python main.py "$@"