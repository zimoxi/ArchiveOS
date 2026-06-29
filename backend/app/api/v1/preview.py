import os
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.archive import Archive
from app.models.user import User
from app.core.security import get_current_user

router = APIRouter()

PREVIEWABLE_IMAGES = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp", ".svg"}
PREVIEWABLE_DOCS = {".pdf", ".txt", ".md", ".csv", ".json"}


@router.get("/preview/{archive_id}")
def preview_file(
    archive_id: int,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    record = db.query(Archive).filter(Archive.id == archive_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Archive not found")

    file_path = record.file_path
    if not file_path or not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found on disk")

    ext = os.path.splitext(file_path)[1].lower()
    if ext in PREVIEWABLE_IMAGES:
        media_map = {
            ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
            ".gif": "image/gif", ".bmp": "image/bmp", ".webp": "image/webp",
            ".svg": "image/svg+xml",
        }
        return FileResponse(file_path, media_type=media_map.get(ext, "application/octet-stream"))
    elif ext == ".pdf":
        return FileResponse(file_path, media_type="application/pdf")
    elif ext in {".txt", ".md", ".csv", ".json"}:
        return FileResponse(file_path, media_type="text/plain")
    else:
        return FileResponse(file_path, media_type="application/octet-stream")
