import os

from dotenv import load_dotenv

load_dotenv()
MOCK_MODE = os.getenv("MOCK_MODE", "false").lower() == "true"
BUCKET_NAME = os.getenv("BUCKET_NAME")
SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")
