"""Application configuration loaded from environment variables."""

from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    APP_ENV: str = "development"
    APP_NAME: str = "Real Estate Lead Bot"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = True

    SECRET_KEY: str = "change-me"
    JWT_SECRET: str = "change-me"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60

    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/real_estate_leads"

    CORS_ORIGINS: str = "http://localhost:3000,http://localhost:5173"

    N8N_WEBHOOK_URL: str = "http://localhost:5678/webhook"
    N8N_WEBHOOK_SECRET: str = ""
    N8N_BASE_URL: str = "http://localhost:5678"

    AI_PROVIDER: str = "openai"
    AI_API_KEY: str = ""
    AI_MODEL: str = "gpt-4o-mini"
    AI_TIMEOUT_SECONDS: int = 30

    @property
    def cors_origins_list(self) -> List[str]:
        return [o.strip() for o in self.CORS_ORIGINS.split(",") if o.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
