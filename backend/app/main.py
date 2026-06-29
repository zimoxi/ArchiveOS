from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.auth import router as auth_router
from app.api.v1.user import router as user_router
from app.api.v1.archive import router as archive_router
from app.api.v1.borrow import router as borrow_router
from app.api.v1.approval import router as approval_router
from app.api.v1.dashboard import router as dashboard_router
from app.api.v1.search import router as search_router
from app.api.v1.logs import router as logs_router
from app.api.v1.preview import router as preview_router
from app.db.session import init_db

app = FastAPI(title="OpenFDAMS", version="2.2")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api/v1")
app.include_router(user_router, prefix="/api/v1")
app.include_router(archive_router, prefix="/api/v1")
app.include_router(borrow_router, prefix="/api/v1")
app.include_router(approval_router, prefix="/api/v1")
app.include_router(dashboard_router, prefix="/api/v1")
app.include_router(search_router, prefix="/api/v1")
app.include_router(logs_router, prefix="/api/v1")
app.include_router(preview_router, prefix="/api/v1")


@app.on_event("startup")
def startup():
    init_db()


@app.get("/health")
def health():
    return {"status": "ok", "version": "2.2"}
