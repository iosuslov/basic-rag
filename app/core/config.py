"""Application configuration management."""

from pydantic_settings import BaseSettings
from pydantic import ConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings."""

    APP_NAME: str = "Basic Web Service"
    DEBUG: bool = False
    API_V1_STR: str = "/api/v1"

    model_config = ConfigDict(case_sensitive=True, env_file=".env")


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings."""
    return Settings()
