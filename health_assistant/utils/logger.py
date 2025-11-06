import logging
from datetime import datetime

logging.basicConfig(
    filename="api_usage.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

def log_api_usage(endpoint: str, user: str):
    logging.info(f"Endpoint: {endpoint} | User: {user}")
