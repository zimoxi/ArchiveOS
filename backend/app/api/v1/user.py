from fastapi import APIRouter

router = APIRouter()

@router.get("/me")
def me():
    return {
        "username": "demo",
        "role": "admin"
    }
