# 🤖 AI Resume Job Matcher Agent

An intelligent agent that analyzes your PDF resume and finds the best matching job listings using AI.

## 🚀 Features

- **PDF Resume Analysis**: Extracts and analyzes text from your resume using GPT-4o-mini
- **Skill Extraction**: Identifies technical and soft skills from your resume
- **Job Search**: Searches multiple job boards (Jina AI Reader + Remotive) for relevant positions
- **AI Matching**: Scores each job listing against your resume profile (0-100% match)
- **Ranked Results**: Shows jobs sorted by match percentage with detailed top recommendations
- **Free to Use**: Uses free job search APIs (optional Jina API key for enhanced results)

## 📁 Project Structure

```
resume-job-agent/
├── .env.example
├── requirements.txt
├── main.py
├── resume_analyzer.py
├── job_searcher.py
├── job_matcher.py
└── resume/
    └── (place your resume PDF here)
```

## 🔧 Setup Instructions

### 1. Clone/Create the Project
The project is already set up in your Obsidian Vault at:
`01 - PROJECTS/Active/resume-job-agent/`

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Keys
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Edit `.env` and add your API keys:
   - **OPENROUTER_API_KEY**: Already provided as `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` (required)
   - **JINA_API_KEY**: Optional - get free tier at [Jina AI Reader](https://jina.ai/reader) (1000 requests/month free)

### 4. Add Your Resume
Place your resume PDF in the `resume/` directory:
```bash
cp /path/to/your/resume.pdf ./resume/
```

### 5. Run the Agent
```bash
# Option 1: Interactive mode (will prompt for resume path)
python main.py

# Option 2: Direct resume path
python main.py resume/your_resume.pdf
```

## 📝 How It Works

1. **Resume Analysis**: The agent extracts text from your PDF resume and uses GPT-4o-mini to analyze it, extracting:
   - Professional summary
   - Skills (technical & soft)
   - Work experience
   - Education
   - Target job role preference
   - Years of experience
   - Top keywords for job matching

2. **Job Search**: Searches for relevant jobs using:
   - **Jina AI Reader**: Free job search API (enhanced results with API key)
   - **Remotive**: Free remote job board (no API key needed)

3. **AI Matching**: Uses GPT-4o-mini to score each job (0-100%) based on:
   - Skill match
   - Experience level relevance
   - Role suitability

4. **Results Display**: Shows ranked job matches with:
   - Match percentage color-coded (green ≥70%, yellow 40-69%, red <40%)
   - Job title, company, location
   - Direct application links
   - Top 3 detailed recommendations

## 💡 Tips for Best Results

- Use a text-based PDF resume (not scanned images) for best text extraction
- Keep your resume updated with current skills and experience
- The more specific your skills section, better the job matching
- Consider adding a Jina AI Reader API key for broader job search results
- Run the agent periodically to discover new opportunities

## 🛠️ Customization

You can customize the agent by modifying:
- `job_searcher.py`: Add more job sources or modify search queries
- `job_matcher.py`: Adjust the scoring criteria or prompt
- `main.py`: Change the number of jobs searched or displayed
- `resume_analyzer.py`: Modify what information is extracted from resumes

## 📄 Example Output

```
🤖 AI RESUME JOB MATCHER AGENT
Upload PDF → AI Analyzes → Find Jobs

📄 RESUME ANALYSIS
┌──────────────┬──────────────────────────┐
│ Field        │ Value                    │
├──────────────┼──────────────────────────┤
│ 🎯 Target Role│ Senior Python Developer  │
│ 📅 Experience│ 5 years                  │
│ 🛠️ Skills   │ Python, Django, AWS...   │
└──────────────┴──────────────────────────┘

🎯 FOUND 12 MATCHING JOBS

┌────┬──────────────────────┬──────────┬───────────┬─────────┐
│ #  │ Job Title            │ Company  │ Match %   │ Source  │
├────┼──────────────────────┼──────────┼───────────┼─────────┤
│ 1  │ Senior Python Eng    │ Google   │ 92% 🟢   │ Jina    │
│ 2  │ Backend Developer    │ Stripe   │ 85% 🟢   │ Remotive│
│ 3  │ Django Developer     │ Netflix  │ 78% 🟡   │ Jina    │
└────┴──────────────────────┴──────────┴───────────┴─────────┘
```

## 🔒 Privacy & Security

- Your resume data is processed locally and only sent to OpenAI for analysis
- No resume data is stored or shared beyond the analysis process
- API keys are stored locally in your `.env` file (never committed)
- Consider adding `.env` to your `.gitignore` if using version control

## 🤝 Contributing

Feel free to submit issues or pull requests to improve the agent!

---

**Ready to find your next job? Just point the agent at your resume PDF and let AI do the hunting!** 🎯