"""Application configuration management."""

from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""

    APP_NAME: str = "Basic Web Service"
    DEBUG: bool = False
    API_V1_STR: str = "/api/v1"

    class Config:
        case_sensitive = True
        env_file = ".env"


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings."""
    return Settings()
