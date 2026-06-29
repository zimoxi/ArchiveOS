from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.audit_log import AuditLog
from app.models.user import User
from app.core.security import get_current_user

router = APIRouter()


@router.get("/logs")
def get_logs(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    rows = db.query(AuditLog).order_by(AuditLog.created_at.desc()).limit(100).all()
    return [
        {
            "id": r.id,
            "user_id": r.user_id,
            "action": r.action,
            "target": r.target,
            "created_at": str(r.created_at),
        }
        for r in rows
    ]
