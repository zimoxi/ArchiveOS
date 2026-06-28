"""Application configuration — skeleton only."""

import os


class Settings:
    PROJECT_NAME: str = "OpenFDAMS"
    VERSION: str = "0.0.4"
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"

    # Database (SQLite for local dev)
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///./openfdams.db",
    )

    # CORS
    CORS_ORIGINS: list[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]


settings = Settings()
