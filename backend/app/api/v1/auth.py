from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.db.session import get_db
from app.models.user import User
from app.core.security import create_token, get_current_user

router = APIRouter()


class LoginRequest(BaseModel):
    username: str


@router.post("/login")
def login(body: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == body.username).first()
    if not user:
        user = User(username=body.username, role="admin")
        db.add(user)
        db.commit()
        db.refresh(user)
    token = create_token({"user_id": user.id, "username": user.username, "role": user.role})
    return {"access_token": token, "token_type": "bearer"}


@router.get("/me")
def me(user: User = Depends(get_current_user)):
    return {"id": user.id, "username": user.username, "role": user.role}
