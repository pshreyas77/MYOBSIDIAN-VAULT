#!/usr/bin/env python3
"""
🤖 AI Resume Job Matcher Agent
Upload your PDF resume → AI analyzes it → Finds best matching jobs
"""

import os
import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from resume_analyzer import ResumeAnalyzer
from job_searcher import JobSearcher
from job_matcher import JobMatcher
from openai import OpenAI

console = Console()


def print_banner():
    banner = """
    ╔══════════════════════════════════════════╗
    ║   🤖 AI RESUME JOB MATCHER AGENT        ║
    ║   Upload PDF → AI Analyzes → Find Jobs   ║
    ╚══════════════════════════════════════════╝
    """
    console.print(Panel(banner, style="bold cyan"))


def print_resume_analysis(data: dict):
    console.print("\n[bold green]📄 RESUME ANALYSIS[/bold green]\n")

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="white")

    table.add_row("🎯 Target Role", data.get("job_title_preference", "N/A"))
    table.add_row("📅 Experience", f"{data.get('years_of_experience', 0)} years")
    table.add_row("📝 Summary", data.get("summary", "N/A")[:100] + "...")
    table.add_row("🛠️ Skills", ", ".join(data.get("skills", [])[:8]))

    console.print(table)


def print_jobs(scored_jobs: list):
    if not scored_jobs:
        console.print("\n[bold red]❌ No jobs found. Try different keywords or add Jina API key.[/bold red]")
        return

    console.print(f"\n[bold green]🎯 FOUND {len(scored_jobs)} MATCHING JOBS[/bold green]\n")

    table = Table(show_header=True, header_style="bold yellow")
    table.add_column("#", style="dim", width=4)
    table.add_column("Job Title", style="bold cyan", width=35)
    table.add_column("Company", style="magenta", width=25)
    table.add_column("Location", style="green", width=15)
    table.add_column("Match %", style="bold white", width=10)
    table.add_column("Source", style="dim", width=12)

    for i, job in enumerate(scored_jobs, 1):
        score = job.get("match_score", 0)
        color = "bold green" if score >= 70 else "yellow" if score >= 40 else "red"
        match_str = f"[{color}]{score:.0f}%[/{color}]"

        table.add_row(
            str(i),
            job.get("title", "N/A")[:33],
            job.get("company", "N/A")[:23],
            job.get("location", "N/A")[:13],
            match_str,
            job.get("source", "N/A")
        )

    console.print(table)

    # Print top 3 detailed
    console.print("\n[bold cyan]📋 TOP 3 RECOMMENDED JOBS:[/bold cyan]\n")
    for i, job in enumerate(scored_jobs[:3], 1):
        console.print(Panel(
            f"[bold]{job['title']}[/bold]\n"
            f"🏢 {job['company']} | 📍 {job['location']}\n"
            f"🔗 {job['url']}\n\n"
            f"{job.get('description', '')[:200]}...",
            title=f"#{i} — Match: {job.get('match_score', 0):.0f}%",
            border_style="green"
        ))


def main():
    print_banner()

    # Get resume path
    if len(sys.argv) > 1:
        resume_path = sys.argv[1]
    else:
        resume_path = console.input("\n📎 Enter path to your resume PDF: ").strip()

    if not os.path.exists(resume_path):
        console.print(f"[bold red]❌ File not found: {resume_path}[/bold red]")
        return

    # Step 1: Analyze Resume
    console.print("\n[bold yellow]📄 Step 1: Analyzing Resume...[/bold yellow]")
    analyzer = ResumeAnalyzer(resume_path)
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold cyan]{task.description}"),
        console=console
    ) as progress:
        task = progress.add_task("[cyan]Extracting text from PDF...", total=None)
        analyzer.extract_text()
        progress.update(task, completed=True)

        task = progress.add_task("[cyan]AI analyzing resume with GPT-4o-mini...", total=None)
        resume_data = analyzer.analyze()
        progress.update(task, completed=True)

    print_resume_analysis(resume_data)

    # Step 2: Search Jobs
    console.print("\n[bold yellow]🔍 Step 2: Searching for matching jobs...[/bold yellow]")
    searcher = JobSearcher()

    query = f"{resume_data.get('job_title_preference', 'software engineer')} " \
            f"{' '.join(resume_data.get('skills', [])[:5])}"

    with Progress(
        SpinnerColumn(),
        TextColumn("[bold cyan]{task.description}"),
        console=console
    ) as progress:
        task = progress.add_task("[cyan]Searching job boards...", total=None)
        jobs = searcher.search_all(query, limit=20)
        progress.update(task, completed=True)

    # Step 3: Match & Score
    console.print("\n[bold yellow]🤖 Step 3: AI matching jobs to your profile...[/bold yellow]")
    matcher = JobMatcher(resume_data, jobs)

    with Progress(
        SpinnerColumn(),
        TextColumn("[bold cyan]{task.description}"),
        console=console
    ) as progress:
        task = progress.add_task("[cyan]Scoring each job with GPT...", total=None)
        scored_jobs = matcher.match()
        progress.update(task, completed=True)

    # Step 4: Display Results
    print_jobs(scored_jobs)

    # Save results
    output_file = "matched_jobs.txt"
    with open(output_file, "w") as f:
        for job in scored_jobs:
            f.write(f"{'='*60}\n")
            f.write(f"{job['title']} — {job['company']}\n")
            f.write(f"Match: {job['match_score']:.0f}% | {job['location']}\n")
            f.write(f"URL: {job['url']}\n")
            f.write(f"{job.get('description', '')[:300]}\n")
    console.print(f"\n[dim]✅ Results saved to {output_file}[/dim]")


if __name__ == "__main__":
    main()