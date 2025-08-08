from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
import os

# Allow overriding the full database URL. If not provided, fall back to a
# PostgreSQL URL assembled from individual environment variables. Finally, if the
# connection fails (e.g. PostgreSQL is not running in a local environment), use a
# local SQLite database so that the application can still start.

DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    DB_USER = os.environ.get("DB_USER", "postgres")
    DB_PASSWORD = os.environ.get("DB_PASSWORD", "admin123")
    DB_HOST = os.environ.get("DB_HOST", "localhost")
    DB_NAME = os.environ.get("DB_NAME", "appdb")
    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

try:
    engine = create_engine(DATABASE_URL)
    # Attempt to connect to verify the database is reachable
    engine.connect()
except OperationalError:
    # Fallback to SQLite for local development when PostgreSQL is not available
    DATABASE_URL = "sqlite:///./app.db"
    engine = create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
