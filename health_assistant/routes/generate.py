from fastapi import APIRouter, Form, Header, HTTPException
from core.embeddings import embed_text_cached as embed_text, index
from core.faiss_store import documents
from core.translator import detect_language, translate_text, generate_answer
from utils.security import check_api_key
from utils.logger import log_api_usage

router = APIRouter()

@router.post("/generate")
async def generate(
    query: str = Form(...),
    output_language: str = Form(default="auto"),
    x_api_key: str = Header(...)
):
    check_api_key(x_api_key)
    log_api_usage("/generate", x_api_key)
    if index.ntotal == 0:
        raise HTTPException(status_code=400, detail="No documents available for generation.")

    query_lang = detect_language(query)
    q_emb = embed_text(query)
    D, I = index.search(q_emb, 3)

    context = "\n\n".join([documents[i]["text"] for i in I[0]])
    prompt = f"Answer in {query_lang} language.\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"

    response = generate_answer(prompt)

    if output_language == "auto":
        output_language = query_lang
    if output_language in ["en", "ja"] and output_language != query_lang:
        response = translate_text(response, output_language)

    return {
        "query": query,
        "query_language": query_lang,
        "output_language": output_language,
        "answer": response
    }
