import os

import databases
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Settings:
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "postgres")
    DB_HOST: str = os.getenv("DB_HOST", "fastapi_postgres_db")
    DB_PORT: str = os.getenv("DB_PORT", 5432)
    DB_NAME: str = os.getenv("DB_NAME", "postgres")
    DB_URL: str = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


settings = Settings()

SQLALCHEMY_DB_URL = settings.DB_URL

database = databases.Database(SQLALCHEMY_DB_URL)

engine = create_engine(SQLALCHEMY_DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
