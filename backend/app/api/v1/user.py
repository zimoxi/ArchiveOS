from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User
from app.core.security import get_current_user

router = APIRouter()


@router.get("/me")
def me(user: User = Depends(get_current_user)):
    return {"id": user.id, "username": user.username, "role": user.role}


@router.get("/users")
def user_list(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    rows = db.query(User).all()
    return [{"id": u.id, "username": u.username, "role": u.role} for u in rows]
