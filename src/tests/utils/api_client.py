"""
ApiClient
"""
from http import HTTPStatus


class ApiClient:
    """
    Class to provide each endpoint interaction for testing purposes
    """

    def __init__(self, client) -> None:
        self._client = client

    def get_recipes(self):
        """
        GET /recipes endpoint
        """
        response = self._client.get("/recipes")

        assert response.status_code == HTTPStatus.OK

        return response.json()
