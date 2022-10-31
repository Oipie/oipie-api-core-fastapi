"""
E2E tests for recipes index
"""


def test_index_recipes_works(api_client):
    """
    This test checks if /recipes endpoint is up
    """

    response = api_client.get_recipes()

    print("response", response)

    assert response["items"] == []
    assert response["total_items"] == 0
