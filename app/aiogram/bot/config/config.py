import os

from dotenv import load_dotenv

load_dotenv()

host_url = os.environ.get("HOST_URL", "http://127.0.0.1:8000")
