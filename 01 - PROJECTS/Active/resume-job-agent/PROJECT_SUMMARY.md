# AI Resume Job Matcher Agent - Project Summary

## Overview
This project is an AI-powered agent that analyzes PDF resumes and finds the best matching job listings using OpenRouter/OpenAI GPT models.

## Location
`/home/sunny77/Documents/Obsidian Vault/01 - PROJECTS/Active/resume-job-agent/`

## Key Features
- PDF resume text extraction
- AI-powered resume analysis (skills, experience, education, target role)
- Multi-source job search (Remotive + Jina AI Reader)
- AI job matching and scoring (0-100%)
- Color-coded results display
- Downloadable results (JSON/TXT)
- OpenRouter integration for cost-effective AI usage

## Files
- `app.py` - Streamlit web interface
- `main.py` - Command-line version
- `resume_analyzer.py` - Resume analysis module
- `job_searcher.py` - Job search module
- `job_matcher.py` - Job matching module
- `requirements.txt` - Dependencies
- `.env` - Environment variables (OpenRouter API key configured)
- `README.md` - Detailed documentation
- `resume/` - Directory for resume PDFs

## Usage
### Command Line:
```bash
python main.py resume/your_resume.pdf
```

### Web Interface:
```bash
streamlit run app.py
# Visit http://localhost:8501
```

## Configuration
- OpenRouter API Key: Pre-configured in `.env`
- Default Model: openai/gpt-4o-mini
- Optional: Add Jina AI Reader API key for enhanced job search

## Status
✅ All files saved and ready for use
⏹️ Background processes stopped
📁 Project preserved in designated location