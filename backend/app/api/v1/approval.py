from fastapi import APIRouter

router = APIRouter()

@router.post("/approve")
def approve():
    return {"status": "approved"}

@router.post("/reject")
def reject():
    return {"status": "rejected"}
