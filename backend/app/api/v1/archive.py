from fastapi import APIRouter, UploadFile, File
from app.services.upload_service import save_file

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    path = save_file(file.filename, content)
    return {"file_path": path}
