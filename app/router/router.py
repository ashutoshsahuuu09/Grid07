from app.router.vector_store import query_vector_store, bot_ids
from app.config import SIMILARITY_THRESHOLD

def route_post_to_bots(post_content: str, threshold: float = SIMILARITY_THRESHOLD):
    scores, indices = query_vector_store(post_content)

    matched = []
    for score, idx in zip(scores, indices):
        if score >= threshold:
            matched.append(bot_ids[idx])

    return matched