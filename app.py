import streamlit as st

from utils.pdf_parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.db_utils import (
    insert_resume,
    insert_skills,
    insert_job,
    fetch_all_resumes_with_skills
)
from utils.ranker import rank_candidates

st.set_page_config(page_title="AI Resume Screening", layout="wide")
st.title("🤖 AI Resume Screening & Job Matching System")

tabs = st.tabs(["📄 Upload Resume", "🧾 Add Job & Rank Candidates"])

# -------------------- TAB 1: Upload Resume --------------------
with tabs[0]:
    st.header("Upload Resume")

    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
    name = st.text_input("Candidate Name")
    email = st.text_input("Candidate Email")

    if uploaded_file and name and email:
        if st.button("Process Resume"):
            resume_text = extract_text_from_pdf(uploaded_file)

            if len(resume_text) < 100:
                st.error("Unable to extract sufficient text.")
            else:
                resume_id = insert_resume(name, email, resume_text)
                skills = extract_skills(resume_text)
                insert_skills(resume_id, skills)

                st.success("Resume processed successfully!")
                st.write("**Extracted Skills:**", skills)

# -------------------- TAB 2: Add Job & Rank --------------------
with tabs[1]:
    st.header("Add Job Description")

    job_title = st.text_input("Job Title")
    job_description = st.text_area("Job Description", height=200)

    if job_title and job_description:
        if st.button("Match Candidates"):
            job_skills = extract_skills(job_description)
            insert_job(job_title, job_description, job_skills)

            resumes = fetch_all_resumes_with_skills()
            ranked = rank_candidates(resumes, job_skills, job_description)

            st.subheader("📊 Ranked Candidates")

            for r in ranked:
                st.markdown(
                    f"""
                    **{r['name']}** ({r['email']})  
                    🟢 **Final Score:** {r['final_score']}%  
                    🔹 Skill Match: {r['skill_score']}%  
                    🔹 Semantic Match: {r['semantic_score']}%  
                    🔹 Matched Skills: {', '.join(r['matched_skills']) if r['matched_skills'] else 'None'}
                    ---
                    """
                )
