"""
E2E tests setup
"""
# pylint: disable=redefined-outer-name, unused-argument

from typing import Iterable
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.engine import Connection
from sqlalchemy.orm import sessionmaker, Session
from src.dependencies.database import (
    database_connection,
    get_database,
    testing_database_connection,
)
from src.main import app
from src.tests.utils.api_client import ApiClient


@pytest.fixture(scope="session")
def connection() -> Iterable[Connection]:
    """
    Manages database connection
    """
    _engine = create_engine(testing_database_connection())
    _connection = _engine.connect()

    yield _connection

    _connection.close()


@pytest.fixture()
def transaction(connection) -> Iterable[None]:
    """
    Wraps the test in a transaction
    """
    _transaction = connection.begin()

    yield

    _transaction.rollback()


@pytest.fixture()
def session_handler(connection: Connection, transaction) -> Iterable[Session]:
    """
    Creates a session handler
    """
    session_local = sessionmaker(bind=connection)
    database = session_local()

    yield database

    database.close()


@pytest.fixture()
def test_client(session_handler: Session) -> Iterable[TestClient]:
    """
    Returns an instance of TestClient based in main's app
    """
    app.dependency_overrides[database_connection] = testing_database_connection
    app.dependency_overrides[get_database] = lambda: session_handler
    client = TestClient(app)

    yield client

    app.dependency_overrides = {}


@pytest.fixture()
def api_client(test_client: TestClient) -> Iterable[ApiClient]:
    """
    Generates an API Client
    """
    return ApiClient(test_client)


# pylint: enable=redefined-outer-name, unused-argument
