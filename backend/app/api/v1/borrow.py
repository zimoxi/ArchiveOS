from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.db.session import get_db
from app.models.borrow import BorrowRecord
from app.models.archive import Archive
from app.models.user import User
from app.core.security import get_current_user

router = APIRouter()


class BorrowRequest(BaseModel):
    archive_id: int


@router.post("/borrow")
def borrow(
    body: BorrowRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    archive = db.query(Archive).filter(Archive.id == body.archive_id).first()
    if not archive:
        raise HTTPException(status_code=404, detail="Archive not found")

    existing = (
        db.query(BorrowRecord)
        .filter(BorrowRecord.archive_id == body.archive_id, BorrowRecord.status != "returned")
        .first()
    )
    if existing:
        raise HTTPException(status_code=400, detail="Already borrowed")

    record = BorrowRecord(archive_id=body.archive_id, user_id=user.id, status="borrowed")
    db.add(record)
    db.commit()
    db.refresh(record)
    return {"id": record.id, "archive_id": record.archive_id, "status": record.status}


@router.post("/return")
def return_item(
    body: BorrowRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    record = (
        db.query(BorrowRecord)
        .filter(BorrowRecord.archive_id == body.archive_id, BorrowRecord.status != "returned")
        .first()
    )
    if not record:
        raise HTTPException(status_code=404, detail="No active borrow found")

    record.status = "returned"
    record.returned_at = datetime.utcnow()
    db.commit()
    return {"id": record.id, "archive_id": record.archive_id, "status": "returned"}


@router.get("/borrow/history")
def borrow_history(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    rows = (
        db.query(BorrowRecord)
        .filter(BorrowRecord.user_id == user.id)
        .order_by(BorrowRecord.created_at.desc())
        .all()
    )
    return [
        {
            "id": r.id,
            "archive_id": r.archive_id,
            "status": r.status,
            "created_at": str(r.created_at),
            "returned_at": str(r.returned_at) if r.returned_at else None,
        }
        for r in rows
    ]
