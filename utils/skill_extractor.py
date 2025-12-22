import re

# Basic skill vocabulary (expandable)
SKILL_SET = [
    "python", "sql", "machine learning", "deep learning",
    "java", "c++", "excel", "power bi", "tableau",
    "streamlit", "postgresql", "mysql", "nlp"
]

def extract_skills(text):
    """
    Extract skills from resume text.
    Returns a list of normalized skills.
    """
    text = text.lower()
    found_skills = set()

    for skill in SKILL_SET:
        # Word boundary match (avoids partial matches)
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            found_skills.add(skill)

    return list(found_skills)
