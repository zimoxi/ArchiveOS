import os

def preview_file(path: str):
    if not os.path.exists(path):
        return {"error": "not found"}
    return {"file": path, "preview": "enabled"}
