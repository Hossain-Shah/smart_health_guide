import faiss
import json
import os
from core.config import FAISS_INDEX_PATH, DOCS_PATH
from core.embeddings import index

# In-memory documents list
documents = []

def save_data():
    """Persist FAISS index and document metadata to disk."""
    faiss.write_index(index, FAISS_INDEX_PATH)
    with open(DOCS_PATH, "w", encoding="utf-8") as f:
        json.dump(documents, f, ensure_ascii=False, indent=2)

def load_data():
    """Load FAISS index and documents from disk."""
    global documents
    if os.path.exists(FAISS_INDEX_PATH):
        loaded_index = faiss.read_index(FAISS_INDEX_PATH)
        index.add(loaded_index.reconstruct_n(0, loaded_index.ntotal))
        print("FAISS index loaded.")
    if os.path.exists(DOCS_PATH):
        with open(DOCS_PATH, "r", encoding="utf-8") as f:
            documents.extend(json.load(f))
        print(f"{len(documents)} documents loaded.")
