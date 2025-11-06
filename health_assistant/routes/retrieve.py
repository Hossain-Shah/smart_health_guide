from fastapi import APIRouter, Form, Header, HTTPException
from core.embeddings import embed_text_cached as embed_text, index
from core.faiss_store import documents
from utils.security import check_api_key

router = APIRouter()

@router.post("/retrieve")
async def retrieve(query: str = Form(...), x_api_key: str = Header(...)):
    check_api_key(x_api_key)
    if index.ntotal == 0:
        raise HTTPException(status_code=400, detail="No documents in index.")

    q_emb = embed_text(query)
    D, I = index.search(q_emb, 3)

    results = [
        {"doc": documents[i], "score": float(D[0][n])}
        for n, i in enumerate(I[0])
    ]
    return {"query": query, "results": results}
