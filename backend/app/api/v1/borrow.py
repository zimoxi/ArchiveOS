from fastapi import APIRouter

router = APIRouter()

@router.post("/borrow")
def borrow():
    return {"status": "borrow request created"}

@router.post("/return")
def return_item():
    return {"status": "return processed"}
