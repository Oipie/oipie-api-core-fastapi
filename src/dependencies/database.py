"""
Database dependencies
"""
from typing import Iterable

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

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
) -> Iterable[Session]:
    """
    Returns a Session instance
    """
    engine = create_engine(connection_url, echo=True)
    session_local = sessionmaker(bind=engine)
    session = session_local()
    _transaction = session.begin()
    try:
        yield session
        _transaction.commit()
    except:
        _transaction.rollback()
        raise
    finally:
        session.close()
