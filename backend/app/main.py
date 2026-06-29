from fastapi import FastAPI
from app.api.v1.auth import router as auth_router
from app.api.v1.user import router as user_router
from app.api.v1.archive import router as archive_router

app = FastAPI(title="OpenFDAMS")

app.include_router(auth_router, prefix="/api/v1")
app.include_router(user_router, prefix="/api/v1")
app.include_router(archive_router, prefix="/api/v1")

@app.get("/health")
def health():
    return {"status": "ok"}
