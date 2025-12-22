from utils.db_utils import insert_job
from utils.skill_extractor import extract_skills
from utils.matcher import calculate_match_score

# Sample job description
job_text = """
Looking for a Python developer with SQL and Machine Learning experience.
"""

job_skills = extract_skills(job_text)
job_id = insert_job("Python Developer", job_text, job_skills)

# Sample resume skills (from DB or hardcoded for test)
resume_skills = ["python", "sql", "streamlit"]

score, matched = calculate_match_score(resume_skills, job_skills)

print("Job Skills:", job_skills)
print("Matched Skills:", matched)
print("Match Score:", score)
