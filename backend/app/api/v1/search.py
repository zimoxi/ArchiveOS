from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.db.session import get_db
from app.models.archive import Archive
from app.models.borrow import BorrowRecord
from app.models.user import User
from app.core.security import get_current_user

router = APIRouter()


@router.get("/search/archive")
def search_archive(
    q: str = Query("", description="搜索关键词"),
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    query = db.query(Archive)
    if q:
        query = query.filter(
            or_(
                Archive.title.contains(q),
                Archive.description.contains(q),
            )
        )
    rows = query.order_by(Archive.created_at.desc()).limit(50).all()
    return [
        {
            "id": r.id,
            "title": r.title,
            "description": r.description,
            "file_path": r.file_path,
            "created_by": r.created_by,
            "created_at": str(r.created_at),
        }
        for r in rows
    ]


@router.get("/search/borrow")
def search_borrow(
    q: str = Query("", description="搜索关键词"),
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    query = db.query(BorrowRecord)
    if q:
        query = query.filter(BorrowRecord.archive_id.cast(str).contains(q))
    rows = query.order_by(BorrowRecord.created_at.desc()).limit(50).all()
    return [
        {
            "id": r.id,
            "archive_id": r.archive_id,
            "user_id": r.user_id,
            "status": r.status,
            "created_at": str(r.created_at),
            "returned_at": str(r.returned_at) if r.returned_at else None,
        }
        for r in rows
    ]
