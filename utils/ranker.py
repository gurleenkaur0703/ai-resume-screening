from utils.matcher import calculate_match_score
from utils.semantic_matcher import semantic_similarity
from utils.hybrid_matcher import hybrid_score

def rank_candidates(resumes, job_skills, job_text):
    ranked = []

    for resume in resumes:
        resume_id, name, email, skills = resume
        skills = skills or []

        skill_score, matched = calculate_match_score(skills, job_skills)

        # Combine resume skills text for AI
        resume_text = " ".join(skills)
        semantic_score = semantic_similarity(resume_text, job_text)

        final_score = hybrid_score(skill_score, semantic_score)

        ranked.append({
            "resume_id": resume_id,
            "name": name,
            "email": email,
            "final_score": final_score,
            "skill_score": skill_score,
            "semantic_score": semantic_score,
            "matched_skills": matched
        })

    ranked.sort(key=lambda x: x["final_score"], reverse=True)
    return ranked
