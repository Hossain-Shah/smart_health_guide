import os

# Configuration
API_KEY = os.getenv("API_KEY", "PRIVATE11")

# File paths
FAISS_INDEX_PATH = "data/faiss_index.bin"
DOCS_PATH = "data/documents.json"

# Ensure data directory exists
os.makedirs("data", exist_ok=True)
