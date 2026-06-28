from fastapi import APIRouter
from app.services.health_service import get_health

router = APIRouter()

@router.get("/health")
def health():
    return get_health()
