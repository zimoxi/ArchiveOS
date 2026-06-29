from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from app.db.session import get_db
from app.models.user import User
from app.models.archive import Archive
from app.models.borrow import BorrowRecord
from app.models.audit_log import AuditLog
from app.core.security import get_current_user

router = APIRouter()


def log_action(db: Session, user_id: int, action: str, target: str):
    db.add(AuditLog(user_id=user_id, action=action, target=target))
    db.commit()


@router.get("/dashboard")
def dashboard(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    user_count = db.query(func.count(User.id)).scalar() or 0
    archive_count = db.query(func.count(Archive.id)).scalar() or 0
    borrow_active = (
        db.query(func.count(BorrowRecord.id))
        .filter(BorrowRecord.status != "returned")
        .scalar()
    ) or 0
    borrow_total = db.query(func.count(BorrowRecord.id)).scalar() or 0
    log_count = db.query(func.count(AuditLog.id)).scalar() or 0

    today = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    uploads_today = (
        db.query(func.count(Archive.id))
        .filter(Archive.created_at >= today)
        .scalar()
    ) or 0

    return {
        "system": "OpenFDAMS",
        "version": "v2.2",
        "stats": {
            "users": user_count,
            "archives": archive_count,
            "borrows_active": borrow_active,
            "borrows_total": borrow_total,
            "uploads_today": uploads_today,
            "logs": log_count,
        },
        "user": {
            "id": user.id,
            "username": user.username,
            "role": user.role,
        },
    }


@router.get("/stats/dashboard")
def stats_dashboard(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return dashboard(user=user, db=db)
