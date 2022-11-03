"""
Database dependencies
"""
from typing import Generator
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from src.config.database import database_url_connection

BaseModel = declarative_base()


def database_connection() -> str:
    """
    Returns a string representing the database URL connection
    """
    return database_url_connection()


def testing_database_connection() -> str:
    """
    Returns a string representing the database URL connection for testing purposes
    """
    return database_url_connection({"database_name": "oipie_tests"})


def get_database(
    connection_url=Depends(database_connection),
) -> Generator[Session, None, None]:
    """
    Returns a Session instance
    """
    engine = create_engine(connection_url)
    session_local = sessionmaker(bind=engine)
    database = session_local()
    try:
        yield database
    finally:
        database.close()
