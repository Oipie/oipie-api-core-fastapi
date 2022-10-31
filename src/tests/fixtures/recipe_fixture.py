"""
Recipe Fixture
"""
from src.core.recipes.domain.recipe import RecipeAttributes

PANCAKE: RecipeAttributes = {
    "uuid": "84d4430d-eddc-47fe-84af-556d3f0f3e25",
    "name": "Pancakes",
    "favourite_amount": 10,
    "preparation_time": 10000,
    "cover": "https://an-url.com/a/picture.png",
}

STRAWBERRY_SMOOTHIE: RecipeAttributes = {
    "uuid": "b8f590de-8f73-45cb-bef8-0f5d6082546d",
    "name": "Strawberry smoothie",
    "favourite_amount": 20,
    "preparation_time": 8500,
    "cover": "https://an-url.com/a/smoothie.png",
}
