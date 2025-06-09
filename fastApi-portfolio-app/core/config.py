"""Configuration settings for the Kite Connect API."""
from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    """Application settings."""
    
    # Kite API settings
    KITE_API_KEY: str = ""
    KITE_API_SECRET: str = ""
    
    # Database settings
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    
    @property
    def DATABASE_URL(self) -> str:
        """Get database URL."""
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    @property
    def CREDENTIALS(self) -> dict:
        """Get Kite API credentials."""
        return {
            "api_key": self.KITE_API_KEY,
            "api_secret": self.KITE_API_SECRET
        }

    class Config:
        env_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
        case_sensitive = True

settings = Settings()
