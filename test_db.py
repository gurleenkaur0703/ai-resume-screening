from utils.db_utils import insert_resume, insert_skills

# 1️⃣ Insert a resume first
resume_id = insert_resume(
    "Test Candidate",
    "test@email.com",
    "Python developer with SQL and Machine Learning experience"
)

print("Inserted resume ID:", resume_id)

# 2️⃣ Insert skills using the SAME resume_id
insert_skills(resume_id, ["python", "sql", "machine learning"])

print("Skills inserted successfully")
