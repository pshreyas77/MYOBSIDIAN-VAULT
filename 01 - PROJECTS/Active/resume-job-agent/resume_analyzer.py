import pdfplumber
import openai
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


class ResumeAnalyzer:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.raw_text = ""
        self.skills = []
        self.experience = []
        self.education = []
        self.summary = ""

    def extract_text(self):
        """Extract text from PDF"""
        text = ""
        with pdfplumber.open(self.pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        self.raw_text = text
        return text

    def analyze(self):
        """Use GPT to analyze resume and extract structured data"""
        if not self.raw_text:
            self.extract_text()

        prompt = f"""
You are an expert resume analyst. Analyze the following resume and extract:

1. **Professional Summary** (2-3 sentences)
2. **Skills** (list all technical and soft skills, max 20)
3. **Work Experience** (company, role, duration, key responsibilities)
4. **Education** (degree, institution, year)
5. **Job Title Preference** (what role they should be targeting)
6. **Years of Experience** (total)
7. **Top 5 Keywords** for job matching

Resume Text:
---
{self.raw_text[:8000]}  # Limit token usage
---

Respond in this EXACT JSON format:
{{
    "summary": "...",
    "skills": ["skill1", "skill2", ...],
    "experience": ["exp1", "exp2", ...],
    "education": ["edu1", "edu2", ...],
    "job_title_preference": "...",
    "years_of_experience": 0,
    "keywords": ["kw1", "kw2", "kw3", "kw4", "kw5"]
}}
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a resume parsing AI. Always respond with valid JSON only."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1,
            response_format={"type": "json_object"}
        )

        import json
        data = json.loads(response.choices[0].message.content)

        self.summary = data.get("summary", "")
        self.skills = data.get("skills", [])
        self.experience = data.get("experience", [])
        self.education = data.get("education", [])
        self.job_title_preference = data.get("job_title_preference", "")
        self.years_of_experience = data.get("years_of_experience", 0)
        self.keywords = data.get("keywords", [])

        return {
            "summary": self.summary,
            "skills": self.skills,
            "experience": self.experience,
            "education": self.education,
            "job_title_preference": self.job_title_preference,
            "years_of_experience": self.years_of_experience,
            "keywords": self.keywords
        }