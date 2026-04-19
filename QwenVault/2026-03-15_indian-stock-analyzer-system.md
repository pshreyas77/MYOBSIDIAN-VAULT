---
title: "Indian Stock Analyzer System"
date: 2026-03-15
tags:
  - python
  - sql
  - machine-learning
  - llm-ai
  - linux
  - geopolitics
  - stock-market
  - research
  - finance
  - web-dev
source: qwen-export
model: qwen3.5-plus
---

# Indian Stock Analyzer System

**Date:** 2026-03-15  
**Model:** `qwen3.5-plus`  
**Topics:** [[Python]] · [[SQL]] · [[Machine-Learning]] · [[LLM-AI]] · [[Linux]] · [[Geopolitics]] · [[Stock-Market]] · [[Research]] · [[Finance]] · [[Web-Dev]]

---

### 🧑 You

Create a complete Indian stock analyzer system with these files:

1. config.py
2. data_fetcher.py
3. feature_engineering.py
4. model_training.py
5. daily_analyzer.py
6. email_sender.py
7. main.py
8. test.py
9. requirements.txt
10. .env.template
11. README.md

Requirements:
- Analyze NIFTY 50 stocks (RELIANCE.NS, TCS.NS, HDFCBANK.NS, INFY.NS, ICICIBANK.NS, HINDUNILVR.NS, ITC.NS, KOTAKBANK.NS, SBIN.NS, BHARTIARTL.NS, LM.NS, ASIANPAINT.NS, MARUTI.NS, TITAN.NS, SUNPHARMA.NS, ONGC.NS, NTPC.NS, M&M.NS, POWERGRID.NS, ULTRACEMCO.NS, BAJFINANCE.NS, ADANIPORTS.NS, TATAMOTORS.NS, JSWSTEEL.NS, TECHM.NS, INDUSINDBK.NS, NESTLEIND.NS, HCLTECH.NS, WIPRO.NS, AXISBANK.NS, BAJAJFINSV.NS, DRREDDY.NS, GRASIM.NS, HEROMOTOCO.NS, HINDALCO.NS, BPCL.NS, BRITANNIA.NS, CIPLA.NS, DIVISLAB.NS, EICHERMOT.NS, SBILIFE.NS, SHREECEM.NS, TATACONSUM.NS, TATASTEEL.NS, UPL.NS, HDFCLIFE.NS, COALINDIA.NS, IOC.NS, GAIL.NS, HINDZINC.NS)
- Use yfinance for data
- Technical indicators: RSI, MACD, SMA20, SMA50, Bollinger Bands, OBV
- Random Forest classifier to predict next-day direction
- Features must be lagged (no look-ahead bias)
- Store data in SQLite
- Daily analysis: generate buy scores (0-1), rank stocks
- Apply filters: volume > 100000, price > 10
- Top 5 stocks = Buy, rest = Hold
- Send HTML email with:
  - Market summary (NIFTY 50 change)
  - Top 5 buys with mini charts (30-day price)
  - Hold list table
- Email via SMTP (Gmail)
- Include backtesting in test.py
- Add proper error handling and logging
- Include disclaimer: "Not financial advice"

Make all code production-ready with clear comments.

---

### 🧑 You

Step 1: Save All Files

Create a new folder on your computer and save each file Claude provides:
bash

mkdir stock-analyzer
cd stock-analyzer

Then create each file (copy-paste from Claude's response):

    config.py

    data_fetcher.py

    feature_engineering.py

    model_training.py

    daily_analyzer.py

    email_sender.py

    main.py

    test.py

    requirements.txt

    .env.template

    README.md

Step 2: Set Up Environment
bash

# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Download NLTK data for sentiment analysis
python -c "import nltk; nltk.download('vader_lexicon')"

Step 3: Configure Environment Variables
bash

# Copy template to .env
cp .env.template .env

# Edit .env with your credentials
nano .env  # or use any text editor

Add your:

    Gmail address and App Password (not regular password)

    NewsAPI key (optional)

    Receiver email

Step 4: Initialize Database & Train Model
bash

# This will fetch historical data and train the model
python model_training.py

Step 5: Test It
bash

# Run a test with historical data
python test.py

# Run a manual analysis for today
python main.py

Step 6: Set Up Automation

For Linux/Mac (cron):
bash

crontab -e
# Add this line (runs at 6 PM weekdays):
0 18 * * 1-5 cd /path/to/stock-analyzer && /path/to/venv/bin/python main.py >> /path/to/stock-analyzer/cron.log 2>&1

For Windows (Task Scheduler):

    Open Task Scheduler

    Create Basic Task

    Trigger: Daily at 6 PM, weekdays only

    Action: Start program python, arguments: main.py, start in: C:\path\to\stock-analyzer

Step 7: Monitor

Check the logs to ensure it's working:
bash

tail -f analyzer.log

---

### 🧑 You

check and fix

---

### 🧑 You

No HTML, CSS, or JavaScript content found.

---
