from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model once (efficient)
model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_similarity(resume_text, job_text):
    """
    Returns semantic similarity score (0–100)
    """
    embeddings = model.encode([resume_text, job_text])

    score = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return round(score * 100, 2)
