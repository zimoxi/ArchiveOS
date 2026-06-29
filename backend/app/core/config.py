import os

class Settings:
    APP_NAME = "OpenFDAMS"
    ENV = os.getenv("ENV", "dev")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dev.db")

settings = Settings()
