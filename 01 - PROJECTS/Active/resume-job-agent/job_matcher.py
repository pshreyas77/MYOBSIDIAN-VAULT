import openai
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


class JobMatcher:
    def __init__(self, resume_data: dict, jobs: list):
        self.resume_data = resume_data
        self.jobs = jobs
        self.scored_jobs = []

    def match(self):
        """Score each job against resume using GPT"""
        for job in self.jobs:
            score = self._score_job(job)
            self.scored_jobs.append({**job, "match_score": score})

        # Sort by score descending
        self.scored_jobs.sort(key=lambda x: x["match_score"], reverse=True)
        return self.scored_jobs

    def _score_job(self, job: dict) -> float:
        """Use GPT to score how well a job matches the resume (0-100)"""

        prompt = f"""
        Rate how well this job matches the candidate's resume on a scale of 0-100.

        RESUME:
        - Skills: {', '.join(self.resume_data.get('skills', []))}
        - Experience: {', '.join(self.resume_data.get('experience', []))}
        - Education: {', '.join(self.resume_data.get('education', []))}
        - Target Role: {self.resume_data.get('job_title_preference', 'N/A')}
        - Years of Experience: {self.resume_data.get('years_of_experience', 0)}
        - Keywords: {', '.join(self.resume_data.get('keywords', []))}

        JOB:
        - Title: {job.get('title', 'N/A')}
        - Company: {job.get('company', 'N/A')}
        - Description: {job.get('description', 'N/A')}

        Consider: skill match, experience level match, role relevance.
        Respond with ONLY a number between 0 and 100.
        """

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Respond with only a number 0-100."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
                max_tokens=10
            )
            score = float(response.choices[0].message.content.strip())
            return min(max(score, 0), 100)
        except Exception:
            return 50.0  # Fallback score