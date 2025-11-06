from fastapi import APIRouter, UploadFile, Header, BackgroundTasks
from core.embeddings import embed_text, index
from core.faiss_store import documents, save_data
from core.translator import detect_language
from utils.security import check_api_key

router = APIRouter()

@router.post("/ingest")
async def ingest(file: UploadFile, background_tasks: BackgroundTasks, x_api_key: str = Header(...)):
    check_api_key(x_api_key)
    text = (await file.read()).decode("utf-8")

    embedding = embed_text(text)
    index.add(embedding)
    lang = detect_language(text)
    documents.append({"text": text, "lang": lang})

    background_tasks.add_task(save_data)
    return {"message": "Document ingested", "language": lang, "total_docs": len(documents)}
