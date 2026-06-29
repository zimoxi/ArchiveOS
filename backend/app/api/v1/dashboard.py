from fastapi import APIRouter
from app.services.lifecycle_service import lifecycle

router = APIRouter()

@router.get("/dashboard")
def dashboard():
    return {
        "system": "OpenFDAMS",
        "lifecycle": lifecycle(),
        "stats": {
            "users": 1,
            "archives": 0,
            "borrows": 0
        }
    }
