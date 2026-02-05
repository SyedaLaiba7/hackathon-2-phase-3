"""Configuration settings for the application."""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    # OpenRouter API key (replaces OpenAI)
    OPENROUTER_API_KEY: Optional[str] = None
    # LLM model to use (default: Mistral free model)
    LLM_MODEL: str = "mistralai/mistral-small-3.1-24b-instruct:free"
    # Optional: Your app name for OpenRouter tracking
    APP_NAME: Optional[str] = "Todo Chatbot"
    # Optional: Your app URL for OpenRouter tracking
    APP_URL: Optional[str] = None
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Global settings instance
settings = Settings()

