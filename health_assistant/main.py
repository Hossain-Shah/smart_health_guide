from fastapi import FastAPI
from routes import ingest, retrieve, generate
from core.faiss_store import load_data

app = FastAPI(title="Healthcare Knowledge Assistant")

# Load persisted data at startup
load_data()

# Include routes
app.include_router(ingest.router)
app.include_router(retrieve.router)
app.include_router(generate.router)
