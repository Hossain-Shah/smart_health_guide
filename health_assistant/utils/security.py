from fastapi import Header, HTTPException
from core.config import API_KEY

def check_api_key(x_api_key: str = Header(...)):
    """Validate API key."""
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
