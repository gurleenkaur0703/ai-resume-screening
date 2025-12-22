from utils.semantic_matcher import semantic_similarity

resume_text = """
Python developer with experience in SQL, dashboards, and data analysis.
"""

job_text = """
Looking for a data analyst skilled in Python and SQL for analytics work.
"""

score = semantic_similarity(resume_text, job_text)
print("Semantic Similarity Score:", score)
