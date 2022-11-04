"""
E2E tests for recipes index
"""


from src.tests.utils.api_client import ApiClient


def test_index_recipes_works(api_client: ApiClient):
    """
    This test checks if /recipes endpoint is up
    """

    response = api_client.get_recipes()

    print("response", response)

    assert response["items"] == []
    assert response["total_items"] == 0
