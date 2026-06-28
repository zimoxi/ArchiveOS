"""Health check endpoints."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok", "service": "openfdams-backend"}


@router.get("/health/db")
def health_db():
    """Placeholder — will check DB connectivity in future."""
    return {"status": "ok", "db": "not_configured"}
