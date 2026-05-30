import requests
from bs4 import BeautifulSoup
import time
import os


class JobSearcher:
    """Search jobs from multiple free sources"""

    def __init__(self, api_key: str = None):
        self.jina_api_key = api_key or os.getenv("JINA_API_KEY", "")  # Free tier available

    def search_jina(self, query: str, limit: int = 15):
        """
        Use Jina AI Reader - FREE job search API
        Get key at: https://jina.ai/reader
        """
        if not self.jina_api_key:
            return []

        url = "https://r.jina.ai/" + query
        headers = {"Accept": "application/json", "X-Return-Format": "json"}
        if self.jina_api_key:
            headers["Authorization"] = f"Bearer {self.jina_api_key}"

        try:
            resp = requests.get(url, headers=headers, timeout=30)
            data = resp.json()

            jobs = []
            for item in data.get("data", [])[:limit]:
                job = {
                    "title": item.get("title", "N/A"),
                    "company": item.get("organization_name", "N/A"),
                    "location": item.get("location", "Remote"),
                    "description": item.get("description", "")[:500],
                    "url": item.get("link", ""),
                    "source": "Jina AI"
                }
                jobs.append(job)
            return jobs
        except Exception as e:
            print(f"[!] Jina search failed: {e}")
            return []

    def search_remotive(self, query: str, limit: int = 10):
        """Search remote jobs from Remotive (free, no API key needed)"""
        url = "https://remotive.com/api/remote-jobs"
        try:
            resp = requests.get(url, timeout=30)
            data = resp.json().get("jobs", [])

            jobs = []
            for job in data:
                title_lower = job.get("title", "").lower()
                if any(kw.lower() in title_lower for kw in query.split()):
                    jobs.append({
                        "title": job.get("title"),
                        "company": job.get("company_name"),
                        "location": job.get("candidate_required_location", "Remote"),
                        "description": job.get("description", "")[:300],
                        "url": job.get("url"),
                        "source": "Remotive"
                    })
                    if len(jobs) >= limit:
                        break
            time.sleep(1)
            return jobs
        except Exception as e:
            print(f"[!] Remotive search failed: {e}")
            return []

    def search_all(self, query: str, limit: int = 15):
        """Combine all search sources"""
        all_jobs = []

        print("🔍 Searching Jina AI Reader...")
        all_jobs.extend(self.search_jina(query, limit))

        print("🔍 Searching Remotive...")
        all_jobs.extend(self.search_remotive(query, limit))

        # Deduplicate by title
        seen = set()
        unique_jobs = []
        for job in all_jobs:
            key = job["title"].lower()
            if key not in seen:
                seen.add(key)
                unique_jobs.append(job)

        return unique_jobs[:limit]