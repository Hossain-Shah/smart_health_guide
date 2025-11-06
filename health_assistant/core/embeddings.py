from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from functools import lru_cache

# Initialize embedding model
model = SentenceTransformer("pritamdeka/BioBERT-mnli-snli-scinli-scitail-mednli-stsb")
dimension = model.get_sentence_embedding_dimension()

# Initialize FAISS index
index = faiss.IndexFlatL2(dimension)

@lru_cache(maxsize=128)
def embed_text_cached(text: str):
    """
    Cached embedding generator for repeated queries.
    Returns a normalized float32 NumPy array.
    """
    emb = model.encode([text], convert_to_numpy=True)
    faiss.normalize_L2(emb)
    return emb.astype("float32")

def embed_text(text: str):
    """
    Embeds a single document or query into vector space.
    """
    if not text.strip():
        return None
    emb = model.encode([text], convert_to_numpy=True)
    faiss.normalize_L2(emb)
    return emb.astype("float32")
