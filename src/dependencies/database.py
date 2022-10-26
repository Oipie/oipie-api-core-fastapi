"""
Database dependencies
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from src.config.database import database_url_connection

engine = create_engine(database_url_connection())
SessionLocal = sessionmaker(bind=engine)
BaseModel = declarative_base()


def get_database() -> Session:
    """
    Returns a Session instance
    """
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()
