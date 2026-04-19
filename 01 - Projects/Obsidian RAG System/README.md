# Obsidian RAG - AI Chat for Your Vault

A beautiful RAG (Retrieval Augmented Generation) system for your Obsidian vault with 3D knowledge graph visualization.

## Features

- 💬 Chat with your Obsidian vault using local AI
- 🌐 3D animated knowledge graph visualization
- 🔍 Keyword-based search (no GPU needed)
- 🎨 Dark neural aesthetic UI

## Setup

```bash
cd "/home/sunny77/Documents/project OB _AI"
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Run

```bash
# Terminal 1 - Start Ollama
ollama serve

# Terminal 2 - Run the app
streamlit run app.py
```

## Files

- `app.py` - Streamlit UI with 3D graph
- `rag.py` - RAG chain with keyword search
- `ingest.py` - Document indexing
- `watcher.py` - Auto-reindex on changes

## Usage

1. Open http://localhost:8501
2. Ask questions about your vault
3. View the 3D knowledge graph



[[OB_AI]]
