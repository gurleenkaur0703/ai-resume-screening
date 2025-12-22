def hybrid_score(skill_score, semantic_score, w_skill=0.6, w_semantic=0.4):
    final = (w_skill * skill_score) + (w_semantic * semantic_score)
    return round(final, 2)
