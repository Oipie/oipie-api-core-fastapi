"""
E2E tests setup
"""
# pylint: disable=redefined-outer-name, unused-argument

import pytest
from fastapi.testclient import TestClient
from src.dependencies.database import database_connection, testing_database_connection
from src.main import app
from src.tests.utils.api_client import ApiClient


@pytest.fixture()
def test_client() -> TestClient:
    """
    Returns an instance of TestClient based in main's app
    """
    app.dependency_overrides[database_connection] = testing_database_connection
    client = TestClient(app)

    yield client

    app.dependency_overrides = {}


@pytest.fixture()
def api_client(test_client):
    """
    Generates an API Client
    """
    return ApiClient(test_client)


# pylint: enable=redefined-outer-name, unused-argument
