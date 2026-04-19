---
title: "Complete stock analyzer prompt with news tracking"
date: 2026-03-20
tags:
  - python
  - sql
  - machine-learning
  - llm-ai
  - data-analysis
  - linux
  - obsidian
  - stock-market
  - research
  - creative
  - finance
  - web-dev
  - game-design
source: claude-export
---

# Complete stock analyzer prompt with news tracking

> **Conversation Overview**

The person asked Claude to generate a comprehensive, production-ready prompt for building an open-source AI-powered stock market analyzer application intended to be pushed to GitHub. They wanted all relevant features researched and included. Claude produced an extensive master prompt document for a project called "StockSage," covering full-stack architecture, feature specifications, code samples, and deployment guidance.

The conversation was primarily a single-turn prompt generation task. Claude created a detailed markdown document covering ten core features: a portfolio dashboard with live profit/loss tracking, a technical analysis engine implementing over twenty algorithms (RSI, MACD, Bollinger Bands, Ichimoku Cloud, VWAP, Fibonacci retracement, and others), a fundamental analysis module tracking metrics such as P/E ratio, ROE, debt-to-equity, and promoter holding percentages, an ML price prediction system using LSTM neural networks, Facebook Prophet, and Random Forest classifiers, a news aggregation and sentiment analysis pipeline using the FinBERT model, a stock screener with multi-dimensional filters, a smart recommendations engine, a portfolio health scoring system, a price and RSI alert system, and a historical market event overlay for charts.

The tech stack specified includes React 18 with TypeScript and Tailwind CSS on the frontend, Python FastAPI on the backend, yfinance for market data, the `ta` library for technical indicators, TensorFlow/Keras for LSTM modeling, HuggingFace Transformers for sentiment analysis, and SQLite or PostgreSQL for storage. The document also included full project directory structure, REST API endpoint specifications, Docker and GitHub Actions CI/CD configuration, requirements files for both frontend and backend, and a phase-two roadmap covering paper trading simulation, backtesting, options chain viewing, and a Telegram bot integration. The output was saved as a markdown file presented to the user for direct use with AI coding assistants such as Cursor or GitHub Copilot.

**Date:** 2026-03-20  
**Topics:** [[Python]] · [[SQL]] · [[Machine-Learning]] · [[LLM-AI]] · [[Data-Analysis]] · [[Linux]] · [[Obsidian]] · [[Stock-Market]] · [[Research]] · [[Creative]] · [[Finance]] · [[Web-Dev]] · [[Game-Design]]

---

### 🧑 You

can you provide me an complete prompt to build an stock analyzer . which can track news of stocks and all releated images . i will use open code to build it and push it to my github . and it should all type of features . do research and add all required features .

---

### 🤖 Claude

{'type': 'text', 'text': '     1\t---\n     2\tname: frontend-design\n     3\tdescription: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.\n     4\tlicense: Complete terms in LICENSE.txt\n     5\t---\n     6\t\n     7\tThis skill guides creation of distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. Implement real working code with exceptional attention to aesthetic details and creative choices.\n     8\t\n     9\tThe user provides frontend requirements: a component, page, application, or interface to build. They may include context about the purpose, audience, or technical constraints.\n    10\t\n    11\t## Design Thinking\n    12\t\n    13\tBefore coding, understand the context and commit to a BOLD aesthetic direction:\n    14\t- **Purpose**: What problem does this interface solve? Who uses it?\n    15\t- **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, etc. There are so many flavors to choose from. Use these for inspiration but design one that is true to the aesthetic direction.\n    16\t- **Constraints**: Technical requirements (framework, performance, accessibility).\n    17\t- **Differentiation**: What makes this UNFORGETTABLE? What\'s the one thing someone will remember?\n    18\t\n    19\t**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work - the key is intentionality, not intensity.\n    20\t\n    21\tThen implement working code (HTML/CSS/JS, React, Vue, etc.) that is:\n    22\t- Production-grade and functional\n    23\t- Visually striking and memorable\n    24\t- Cohesive with a clear aesthetic point-of-view\n    25\t- Meticulously refined in every detail\n    26\t\n    27\t## Frontend Aesthetics Guidelines\n    28\t\n    29\tFocus on:\n    30\t- **Typography**: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend\'s aesthetics; unexpected, characterful font choices. Pair a distinctive display font with a refined body font.\n    31\t- **Color & Theme**: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes.\n    32\t- **Motion**: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Use Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions. Use scroll-triggering and hover states that surprise.\n    33\t- **Spatial Composition**: Unexpected layouts. Asymmetry. Overlap. Diagonal flow. Grid-breaking elements. Generous negative space OR controlled density.\n    34\t- **Backgrounds & Visual Details**: Create atmosphere and depth rather than defaulting to solid colors. Add contextual effects and textures that match the overall aesthetic. Apply creative forms like gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, and grain overlays.\n    35\t\n    36\tNEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character.\n    37\t\n    38\tInterpret creatively and make unexpected choices that feel genuinely designed for the context. No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices (Space Grotesk, for example) across generations.\n    39\t\n    40\t**IMPORTANT**: Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate code with extensive animations and effects. Minimalist or refined designs need restraint, precision, and careful attention to spacing, typography, and subtle details. Elegance comes from executing the vision well.\n    41\t\n    42\tRemember: Claude is capable of extraordinary creative work. Don\'t hold back, show what can truly be created when thinking outside the box and committing fully to a distinctive vision.\n    43\t', 'uuid': 'd249d87e-3d83-44f1-92ae-a07fce1eae17'}
Here's a comprehensive, production-grade prompt you can use to build your full-featured AI Stock Analyzer. I've tailored it with your exact Groww portfolio data baked in.

{'type': 'text', 'text': 'File created successfully: /mnt/user-data/outputs/AI_Stock_Analyzer_Master_Prompt.md', 'uuid': '6a95baad-7bd5-45ed-bbb8-58ba7bc9ab90'}

{'type': 'local_resource', 'file_path': '/mnt/user-data/outputs/AI_Stock_Analyzer_Master_Prompt.md', 'name': 'AI Stock Analyzer Master Prompt', 'mime_type': 'text/markdown', 'uuid': '50ac3cd0-764b-4bdc-b313-0007cf128282'}
Here's your complete **StockSage** master prompt — fully tailored to your Groww portfolio. Here's a quick summary of what's packed in:

**10 Core Features built in:**
1. **Portfolio Dashboard** — your exact 11 holdings pre-loaded with live P&L tracking
2. **Technical Analysis** — 20+ algorithms: RSI, MACD, Bollinger Bands, Ichimoku, VWAP, Fibonacci, and more
3. **Fundamental Analysis** — P/E, ROE, Debt-to-Equity, Promoter holding, FII/DII activity
4. **ML Price Prediction** — LSTM neural network + Facebook Prophet + Random Forest signals
5. **News & Sentiment** — FinBERT AI model for finance-specific sentiment on each stock
6. **Stock Screener** — filter by sector, RSI, P/E, price range, and more
7. **Smart Recommendations** — engine that knows your portfolio gaps (you're missing IT, Pharma, FMCG)
8. **Portfolio Health Score** — composite score across diversification, momentum, sentiment
9. **Price/RSI Alerts** — with optional Telegram bot integration
10. **Historical Event Overlay** — COVID crash, Budget days, RBI decisions on your charts

**Portfolio-specific insights already baked in:**
- Flags **RPOWER (−47%)** and **Lemon Tree (−33%)** as exit candidates
- Notes your heavy concentration in **PSU/Power/Infrastructure** sector
- Recommends diversifying into **IT and Pharma** at similar budget levels

The file is ready to paste directly into **Cursor, GitHub Copilot, or any AI coding assistant** to start building. Just grab your free API keys from newsapi.org, finnhub.io, and alphavantage.co, and you're off!

---
