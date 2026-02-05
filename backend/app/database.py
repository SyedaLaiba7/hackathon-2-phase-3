"""Database connection and session management."""
import os
from sqlmodel import SQLModel, create_engine, Session
from app.config import settings

# Create database engine
# For serverless (Vercel), use connection pooling with smaller pool size
is_serverless = os.getenv("VERCEL") == "1" or os.getenv("SERVERLESS", "false").lower() == "true"
pool_size = 1 if is_serverless else 5  # Smaller pool for serverless

engine = create_engine(
    settings.DATABASE_URL,
    echo=os.getenv("ENVIRONMENT", "development") == "development",  # Log SQL queries only in development
    pool_pre_ping=True,  # Verify connections before using
    pool_size=pool_size,
    max_overflow=0 if is_serverless else 10,  # No overflow for serverless
    pool_recycle=300,  # Recycle connections after 5 minutes
)


def init_db():
    """Initialize database tables."""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Get database session."""
    with Session(engine) as session:
        yield session

