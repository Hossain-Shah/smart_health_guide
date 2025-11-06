# Health Assistant — README
Project Overview

This project implements a bilingual (English/Japanese) Retrieval-Augmented Generation (RAG) assistant for healthcare guidelines. It provides:

Document ingestion, retrieval, and generation endpoints

FAISS for vector search

SentenceTransformers / BioClinicalBERT for embeddings

Google Translator for bilingual support

Logging and caching for performance and compliance

The system is modular, scalable, and designed for extension into production-grade deployments.

# Setup Instructions
Clone Repo
git clone <your-repo-url>
cd health_assistant

Install Python Dependencies
pip install -r requirements.txt

Run FastAPI Server (Local)
uvicorn main:app --reload

Run via Docker
docker build -t health_assistant .
docker run -p 8000:8000 -e API_KEY=PRIVATE11 health_assistant


Tip: Mount a local data/ folder to persist FAISS index and documents:

docker run -p 8000:8000 -v $(pwd)/data:/app/data -e API_KEY=PRIVATE11 health_assistant

# Authentication

All endpoints require the header:

X-API-Key: PRIVATE11


Requests without the correct API key will return 401 Unauthorized.

# API Endpoints
Endpoint	Method	Description
/ingest	POST	Upload a .txt document (English/Japanese)
/retrieve	POST	Query FAISS index; returns top 3 documents
/generate	POST	Generate an LLM-based answer (bilingual, cached, with context)
Example curl
curl -X POST "http://localhost:8000/generate" \
  -H "X-API-Key: PRIVATE11" \
  -F "query=What are the latest guidelines for type 2 diabetes?" \
  -F "output_language=en"

# Environment Variables
Variable	Description	Default
API_KEY	Authentication key	PRIVATE11
HF_HOME	Hugging Face cache path	/root/.cache/huggingface
TRANSFORMERS_CACHE	Transformers cache path	/root/.cache/transformers
# Design Notes — Scalability, Modularity & Future Improvements
Scalability

Vector Search: FAISS is used for local indexing; for production, a distributed vector DB (e.g., Pinecone, Qdrant, Weaviate) can replace it.

Document Ingestion: Can be handled asynchronously with message queues (RabbitMQ / Kafka) to handle large-scale ingestion.

Modularity

Endpoints are separated in routes/

Core logic in core/

Utilities like logging, caching, security in utils/

Easy to test, swap, and extend components independently (e.g., replace translation or LLM models).

Performance Improvements

Domain-Specific Embeddings: BioClinicalBERT improves relevance on medical content.

Caching: LRU caching for repeated queries (functools.lru_cache).

Logging: API usage logging for compliance (utils/logger.py).

Future Improvements

Integrate persistent document DB (PostgreSQL + metadata)

Replace mock LLM with real model API (OpenAI, Hugging Face Inference API)

Implement user roles and RBAC

Advanced distributed caching or vector search for large-scale deployment