from fastapi import FastAPI
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "OpenFDAMS"
    debug: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
app = FastAPI(title=settings.app_name)


@app.get("/health")
async def health():
    return {"status": "ok", "service": "openfdams-backend"}


@app.get("/")
async def root():
    return {"message": "OpenFDAMS API is running"}
