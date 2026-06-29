import os
from datetime import datetime
from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from app.db.session import get_db
from app.models.archive import Archive
from app.models.user import User
from app.core.security import get_current_user

router = APIRouter()

UPLOAD_DIR = "uploads"


def _serialize(r: Archive) -> dict:
    return {
        "id": r.id,
        "title": r.title,
        "description": r.description or "",
        "category": r.category or "",
        "file_path": r.file_path,
        "created_by": r.created_by,
        "created_at": str(r.created_at),
    }


@router.post("/upload")
async def upload(
    file: UploadFile = File(...),
    title: Optional[str] = Form(None),
    description: Optional[str] = Form(""),
    category: Optional[str] = Form(""),
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    ts = datetime.utcnow().timestamp()
    safe_name = f"{ts}_{file.filename}"
    path = os.path.join(UPLOAD_DIR, safe_name)
    content = await file.read()
    with open(path, "wb") as f:
        f.write(content)

    record = Archive(
        title=title or file.filename,
        description=description or "",
        category=category or "",
        file_path=path,
        created_by=user.id,
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return _serialize(record)


@router.get("/archive/list")
def archive_list(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    rows = db.query(Archive).order_by(Archive.created_at.desc()).all()
    return [_serialize(r) for r in rows]


@router.get("/archive/{archive_id}")
def archive_detail(
    archive_id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    r = db.query(Archive).filter(Archive.id == archive_id).first()
    if not r:
        raise HTTPException(status_code=404, detail="Archive not found")
    return _serialize(r)
