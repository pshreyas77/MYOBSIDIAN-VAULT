"""
🤖 AI RESUME JOB MATCHER — WEB VERSION (OpenRouter)
Upload PDF → AI Analyzes → Finds Best Jobs
Run with: streamlit run app.py
"""

import streamlit as st
import os
import json
import tempfile
from pathlib import Path
from dotenv import load_dotenv

# ── Our Modules ──
from resume_analyzer import ResumeAnalyzer
from job_searcher import JobSearcher
from job_matcher import JobMatcher

# ── Load Env ──
load_dotenv()

# ── Page Config ──
st.set_page_config(
    page_title="🤖 AI Job Matcher",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS ──
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #00d2ff, #7b2ff7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 1rem 0;
    }
    .match-high { color: #00ff88; font-weight: bold; font-size: 1.3rem; }
    .match-med { color: #ffcc00; font-weight: bold; font-size: 1.2rem; }
    .match-low { color: #ff4444; font-weight: bold; font-size: 1.2rem; }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #00d2ff, #7b2ff7);
        color: white;
        font-weight: bold;
        font-size: 1.1rem;
        border-radius: 12px;
        padding: 0.6rem;
    }
    .job-card {
        background: #1e1e2e;
        border-radius: 12px;
        padding: 1rem;
        margin: 0.5rem 0;
        border-left: 4px solid #7b2ff7;
    }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ──
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/robot.png", width=80)
    st.title("🤖 AI Job Agent")
    st.markdown("---")
    st.markdown("""
    ### 📋 How it works:
    1. 📎 Upload your **PDF resume**
    2. 🧠 AI **analyzes** your skills & experience
    3. 🔍 **Searches** job boards automatically
    4. 🎯 **Ranks** jobs by match score
    """)
    st.markdown("---")

    # ✅ OpenRouter API Key input
    api_key = st.text_input(
        "🔑 OpenRouter API Key",
        type="password",
        help="Get yours at openrouter.ai (supports GPT-4o-mini, Claude, etc.)"
    )

    st.markdown(f"""
    <small>
    💡 <b>Tip:</b> Uses GPT-4o-mini via OpenRouter (super cheap ~$0.15/1000 calls).<br>
    Supports 100+ models — switch anytime!
    </small>
    """, unsafe_allow_html=True)

    # Model selector
    selected_model = st.selectbox(
        "🧠 AI Model",
        [
            "openai/gpt-4o-mini",      # ✅ Cheapest & fastest
            "openai/gpt-4o",           # Most accurate
            "anthropic/claude-3.5-sonnet",  # Great alternative
            "google/gemini-2.0-flash",     # Fast & cheap
            "meta-llama/llama-3.1-70b",     # Open source
        ],
        index=0
    )

    jina_key = st.text_input(
        "🔑 Jina AI Key (Optional)",
        type="password",
        help="Free at jina.ai/reader — improves job search"
    )

# ── Main Header ──
st.markdown('<p class="main-header">🤖 AI RESUME JOB MATCHER</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Upload your PDF → AI finds your dream job (Powered by OpenRouter)</p>", unsafe_allow_html=True)

# ── File Uploader ──
st.markdown("---")
col1, col2 = st.columns([2, 1])

with col1:
    uploaded_file = st.file_uploader(
        "📎 Upload Your Resume (PDF)",
        type=["pdf"],
        help="Upload your resume in PDF format"
    )

with col2:
    st.metric("🧠 Model", selected_model)
    st.metric("🔑 Provider", "OpenRouter")

# ── MAIN LOGIC ──
if uploaded_file is not None and api_key:

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name

    try:
        # ── STEP 1: ANALYZE RESUME ──
        st.markdown("---")
        st.subheader("📄 Step 1: Analyzing Your Resume...")

        with st.spinner("🤖 AI is reading your resume..."):
            analyzer = ResumeAnalyzer(tmp_path)
            analyzer.extract_text()
            resume_data = analyzer.analyze()

        # Display analysis
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("🎯 Target Role", resume_data.get("job_title_preference", "N/A")[:20])
        with col2:
            st.metric("📅 Experience", f"{resume_data.get('years_of_experience', 0)} yrs")
        with col3:
            st.metric("🛠️ Skills", f"{len(resume_data.get('skills', []))} found")
        with col4:
            st.metric("🔑 Keywords", ", ".join(resume_data.get("keywords", [])[:3]))

        with st.expander("📋 View Full Resume Analysis"):
            st.json(resume_data)

        st.success("✅ Resume analyzed successfully!")

        # ── STEP 2: SEARCH JOBS ──
        st.markdown("---")
        st.subheader("🔍 Step 2: Searching for Matching Jobs...")

        with st.spinner("🌍 Searching job boards..."):
            searcher = JobSearcher()

            query = f"{resume_data.get('job_title_preference', 'software engineer')} " \
                    f"{' '.join(resume_data.get('skills', [])[:5])}"

            jobs = searcher.search_all(query, limit=20)

        st.info(f"🔍 Found {len(jobs)} jobs from Remotive + Jina AI")

        # ── STEP 3: MATCH & SCORE ──
        st.markdown("---")
        st.subheader("🤖 Step 3: AI Matching Jobs to Your Profile...")

        with st.spinner("🎯 Scoring each job with AI..."):
            matcher = JobMatcher(resume_data, jobs)
            scored_jobs = matcher.match()

        st.success(f"✅ Matched {len(scored_jobs)} jobs!")

        # ── STEP 4: DISPLAY RESULTS ──
        st.markdown("---")
        st.subheader("🎯 Your Top Matching Jobs")

        if scored_jobs:
            for i, job in enumerate(scored_jobs[:10], 1):
                score = job.get("match_score", 0)

                # Color coding
                if score >= 70:
                    color = "🟢"
                    label = "Excellent Match"
                elif score >= 40:
                    color = "🟡"
                    label = "Good Match"
                else:
                    color = "🔴"
                    label = "Low Match"

                with st.container():
                    st.markdown(f"""
                    <div class="job-card">
                        <h3>{color} #{i} — {job['title']} <span style="color:gray; font-size:0.9rem">({label} — {score:.0f}%)</span></h3>
                        <p>🏢 <b>{job['company']}</b> | 📍 {job['location']} | 🔗 <a href="{job['url']}" target="_blank">Apply Here</a></p>
                        <p style="color:#aaa; font-size:0.85rem;">{job.get('description', '')[:250]}...</p>
                        <p style="color:#666; font-size:0.8rem;">Source: {job['source']}</p>
                    </div>
                    """, unsafe_allow_html=True)

            # ── DOWNLOAD RESULTS ──
            st.markdown("---")
            st.subheader("💾 Download Results")

            results_json = json.dumps(scored_jobs, indent=2)
            st.download_button(
                label="📥 Download JSON Results",
                data=results_json,
                file_name="matched_jobs.json",
                mime="application/json"
            )

            # Text version
            results_text = "\n".join([
                f"{'='*60}\n"
                f"{job['title']} — {job['company']}\n"
                f"Match: {job['match_score']:.0f}% | {job['location']}\n"
                f"URL: {job['url']}\n"
                f"{job.get('description', '')[:300]}\n"
                for job in scored_jobs
            ])
            st.download_button(
                label="📥 Download Text Results",
                data=results_text,
                file_name="matched_jobs.txt",
                mime="text/plain"
            )

        else:
            st.warning("⚠️ No jobs found. Try uploading a different resume or check your API keys.")

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        st.exception(e)

    finally:
        # Cleanup temp file
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

else:
    st.info("👆 Please upload your PDF resume and enter your OpenRouter API key to get started!")

    # Show example
    with st.expander("! How to get an OpenRouter API Key?"):
        st.markdown("""
        1. Go to **[openrouter.ai](https://openrouter.ai)**
        2. Sign up (free, no credit card needed)
        3. Go to **Keys** → Create a new key
        4. Copy the key (starts with `sk-or-v1-...`)
        5. Paste it in the sidebar 👆

        💰 **Pricing:**
        | Model | Cost per 1M tokens |
        |-------|-------------------|
        | GPT-4o-mini | ~$0.15 |
        | GPT-4o | ~$2.50 |
        | Claude 3.5 Sonnet | ~$3.00 |
        | Llama 3.1 70B | ~$0.40 |

        This app uses **GPT-4o-mini** → ~$0.15 per 1000 resumes analyzed! 🎉
        """)