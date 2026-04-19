import faiss
from app.router.embeddings import get_embedding
from app.router.personas import BOTS

bot_ids = list(BOTS.keys())
bot_texts = list(BOTS.values())

embeddings = get_embedding(bot_texts)
dimension = embeddings.shape[1]

faiss.normalize_L2(embeddings)
index = faiss.IndexFlatIP(dimension)
index.add(embeddings)

def query_vector_store(query_text, top_k=3):
    query_embedding = get_embedding([query_text])
    faiss.normalize_L2(query_embedding)

    scores, indices = index.search(query_embedding, top_k)
    return scores[0], indices[0]