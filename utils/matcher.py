def calculate_match_score(resume_skills, job_skills):
    if not job_skills:
        return 0.0

    matched = set(resume_skills).intersection(set(job_skills))
    score = (len(matched) / len(job_skills)) * 100

    return round(score, 2), list(matched)
