from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "OpenFDAMS"
    API_PREFIX: str = "/api/v1"

settings = Settings()
