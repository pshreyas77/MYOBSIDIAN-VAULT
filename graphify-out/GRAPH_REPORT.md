# Graph Report - .  (2026-04-20)

## Corpus Check
- Large corpus: 1050 files · ~4,678,899 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder, or use --no-semantic to run AST-only.

## Summary
- 269 nodes · 405 edges · 33 communities detected
- Extraction: 76% EXTRACTED · 24% INFERRED · 0% AMBIGUOUS · INFERRED: 96 edges (avg confidence: 0.57)
- Token cost: 28,000 input · 4,700 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Obsidian Setup & Systems|Obsidian Setup & Systems]]
- [[_COMMUNITY_Buddhist Philosophy|Buddhist Philosophy]]
- [[_COMMUNITY_AI & Machine Learning|AI & Machine Learning]]
- [[_COMMUNITY_Ancient Civilizations|Ancient Civilizations]]
- [[_COMMUNITY_Political Analysis|Political Analysis]]
- [[_COMMUNITY_Philosophers & Thinkers|Philosophers & Thinkers]]
- [[_COMMUNITY_Code Projects|Code Projects]]
- [[_COMMUNITY_Knowledge Management|Knowledge Management]]
- [[_COMMUNITY_Religion & Cosmology|Religion & Cosmology]]
- [[_COMMUNITY_Technology & Development|Technology & Development]]
- [[_COMMUNITY_Education & Learning|Education & Learning]]
- [[_COMMUNITY_Society & Culture|Society & Culture]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]

## God Nodes (most connected - your core abstractions)
1. `Config` - 62 edges
2. `LLMClient` - 23 edges
3. `ToolRegistry` - 21 edges
4. `ObsidianClient` - 20 edges
5. `AudioHandler` - 16 edges
6. `JARVIS` - 16 edges
7. `ClaudeClient` - 11 edges
8. `main()` - 8 edges
9. `organize_by_topics()` - 8 edges
10. `WakeWordDetector` - 6 edges

## Surprising Connections (you probably didn't know these)
- `Client for Obsidian Local REST API` --uses--> `Config`  [INFERRED]
  projects/jarvis/obsidian_client.py → projects/jarvis/config.py
- `Make HTTP request to Obsidian REST API` --uses--> `Config`  [INFERRED]
  projects/jarvis/obsidian_client.py → projects/jarvis/config.py
- `Check if Obsidian API is running` --uses--> `Config`  [INFERRED]
  projects/jarvis/obsidian_client.py → projects/jarvis/config.py
- `Get currently active file in Obsidian` --uses--> `Config`  [INFERRED]
  projects/jarvis/obsidian_client.py → projects/jarvis/config.py
- `Open a file in Obsidian` --uses--> `Config`  [INFERRED]
  projects/jarvis/obsidian_client.py → projects/jarvis/config.py

## Communities

### Community 0 - "Obsidian Setup & Systems"
Cohesion: 0.1
Nodes (15): LLMClient, Clear conversation history, Add message to history, Send message and get response, Chat using Ollama (local), Universal LLM client supporting multiple backends, Initialize LLM client         backend: "ollama", "anthropic", "openai", or "auto, Chat using OpenAI-compatible API (+7 more)

### Community 1 - "Buddhist Philosophy"
Cohesion: 0.1
Nodes (13): ObsidianClient, Search for files in the vault, Search vault content and return matching notes with context, Client for Obsidian Local REST API, List notes in a folder, Normalize a path for the vault, Make HTTP request to Obsidian REST API, Check if Obsidian API is running (+5 more)

### Community 2 - "AI & Machine Learning"
Cohesion: 0.09
Nodes (12): Get recently modified notes, Get tools in Claude API format, Execute a tool by name, Search vault for notes, Registry of tools available to JARVIS, Read a note from vault, Write a note to vault, Create a note in the daily folder (+4 more)

### Community 3 - "Ancient Civilizations"
Cohesion: 0.15
Nodes (12): AudioHandler, Listen for voice input and return text, Handle voice input and output, Simple wake word detection using speech recognition, Listen for wake word and trigger callback, Initialize speech recognition, Initialize text-to-speech, Start background thread for TTS (+4 more)

### Community 4 - "Political Analysis"
Cohesion: 0.15
Nodes (19): analyze_graph(), build_graph(), create_canvas_json(), create_interactive_viz(), extract_links(), generate_graph_report(), generate_obsidian_vault(), get_category() (+11 more)

### Community 5 - "Philosophers & Thinkers"
Cohesion: 0.18
Nodes (6): Text-to-speech output, get_llm_info(), validate(), JARVIS, main(), Get statistics about the vault

### Community 6 - "Code Projects"
Cohesion: 0.13
Nodes (9): ClaudeClient, Execute tool calls and return results, Client for Anthropic Claude API, Estimate token count (approximate), Stream response from Claude, Register a tool that Claude can use, Clear conversation history, Add message to conversation history (+1 more)

### Community 7 - "Knowledge Management"
Cohesion: 0.19
Nodes (14): create_cross_topic_links(), create_file_index(), create_master_topics_index(), create_moc_file(), extract_topics_from_file(), get_all_files(), organize_by_topics(), Extract topics from file content and name (+6 more)

### Community 8 - "Religion & Cosmology"
Cohesion: 0.15
Nodes (15): Buddha Evidence, Buddha Research, Buddhism and Hinduism MOC, Critical Arguments, Critical Questions, Education and Learning MOC, Graphify Knowledge Graph, Master Link Index (+7 more)

### Community 9 - "Technology & Development"
Cohesion: 0.18
Nodes (7): Embeddings, FileSystemEventHandler, index_vault(), load_markdown_files(), SimpleHashEmbeddings, VaultHandler, watch_vault()

### Community 10 - "Education & Learning"
Cohesion: 0.18
Nodes (12): Anatman, Ashoka, Buddha, Ea-Nasir, Göbekli Tepe, Indus Valley Civilization, Mahavira, Nagarjuna (+4 more)

### Community 11 - "Society & Culture"
Cohesion: 0.43
Nodes (4): build_chain(), get_keywords(), KeywordRAG, load_and_index()

### Community 12 - "Community 12"
Cohesion: 0.38
Nodes (6): analyze_file(), organize_vault(), Safely move file with duplicate handling, Main organization function, Analyze file content and return categories, safe_move()

### Community 13 - "Community 13"
Cohesion: 0.33
Nodes (7): Claude Second Brain, Dataview Plugin, J.A.R.V.I.S., Obsidian Local REST API, Ollama, Obsidian RAG System, Templater Plugin

### Community 14 - "Community 14"
Cohesion: 0.67
Nodes (0): 

### Community 15 - "Community 15"
Cohesion: 1.0
Nodes (3): Aristotle, Plato, Socrates

### Community 16 - "Community 16"
Cohesion: 1.0
Nodes (0): 

### Community 17 - "Community 17"
Cohesion: 1.0
Nodes (0): 

### Community 18 - "Community 18"
Cohesion: 1.0
Nodes (2): Confucius, Laozi

### Community 19 - "Community 19"
Cohesion: 1.0
Nodes (2): Graphify, MemPalace

### Community 20 - "Community 20"
Cohesion: 1.0
Nodes (0): 

### Community 21 - "Community 21"
Cohesion: 1.0
Nodes (0): 

### Community 22 - "Community 22"
Cohesion: 1.0
Nodes (0): 

### Community 23 - "Community 23"
Cohesion: 1.0
Nodes (0): 

### Community 24 - "Community 24"
Cohesion: 1.0
Nodes (1): Validate configuration

### Community 25 - "Community 25"
Cohesion: 1.0
Nodes (1): Get info about selected LLM backend

### Community 26 - "Community 26"
Cohesion: 1.0
Nodes (1): Buddhism and Hinduism File Index

### Community 27 - "Community 27"
Cohesion: 1.0
Nodes (1): Education and Learning File Index

### Community 28 - "Community 28"
Cohesion: 1.0
Nodes (1): Society and Culture File Index

### Community 29 - "Community 29"
Cohesion: 1.0
Nodes (1): Technology and Development File Index

### Community 30 - "Community 30"
Cohesion: 1.0
Nodes (1): Chanakya

### Community 31 - "Community 31"
Cohesion: 1.0
Nodes (1): Caste System Origins

### Community 32 - "Community 32"
Cohesion: 1.0
Nodes (1): Dravidian vs North Indian Ancestry

## Knowledge Gaps
- **48 isolated node(s):** `Scan all markdown files in the vault`, `Determine category from folder structure`, `Extract all wikilinks [[...]] and markdown links [...](...) from files`, `Build NetworkX graph with full metadata`, `Analyze graph structure` (+43 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 16`** (2 nodes): `app.py`, `get_graph()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 17`** (2 nodes): `custom_json_dump()`, `fix_canvas.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 18`** (2 nodes): `Confucius`, `Laozi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 19`** (2 nodes): `Graphify`, `MemPalace`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 20`** (1 nodes): `add_images.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 21`** (1 nodes): `add_images_fixed.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 22`** (1 nodes): `download_images.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 23`** (1 nodes): `add_all_images.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 24`** (1 nodes): `Validate configuration`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 25`** (1 nodes): `Get info about selected LLM backend`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 26`** (1 nodes): `Buddhism and Hinduism File Index`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 27`** (1 nodes): `Education and Learning File Index`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 28`** (1 nodes): `Society and Culture File Index`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 29`** (1 nodes): `Technology and Development File Index`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 30`** (1 nodes): `Chanakya`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 31`** (1 nodes): `Caste System Origins`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 32`** (1 nodes): `Dravidian vs North Indian Ancestry`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Config` connect `Ancient Civilizations` to `Obsidian Setup & Systems`, `Buddhist Philosophy`, `AI & Machine Learning`, `Philosophers & Thinkers`, `Code Projects`?**
  _High betweenness centrality (0.245) - this node is a cross-community bridge._
- **Why does `LLMClient` connect `Obsidian Setup & Systems` to `Ancient Civilizations`, `Philosophers & Thinkers`?**
  _High betweenness centrality (0.054) - this node is a cross-community bridge._
- **Are the 61 inferred relationships involving `Config` (e.g. with `ObsidianClient` and `Client for Obsidian Local REST API`) actually correct?**
  _`Config` has 61 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `LLMClient` (e.g. with `JARVIS` and `J.A.R.V.I.S. Main Controller - FREE VERSION`) actually correct?**
  _`LLMClient` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `ToolRegistry` (e.g. with `Config` and `JARVIS`) actually correct?**
  _`ToolRegistry` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `ObsidianClient` (e.g. with `Config` and `JARVIS`) actually correct?**
  _`ObsidianClient` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `AudioHandler` (e.g. with `Config` and `JARVIS`) actually correct?**
  _`AudioHandler` has 5 INFERRED edges - model-reasoned connections that need verification._