import os
from datetime import datetime

UPLOAD_DIR = "uploads"

def save_file(file_name: str, content: bytes):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    path = os.path.join(UPLOAD_DIR, f"{datetime.utcnow().timestamp()}_{file_name}")
    with open(path, "wb") as f:
        f.write(content)
    return path
