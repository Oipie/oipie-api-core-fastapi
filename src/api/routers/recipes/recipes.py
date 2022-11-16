"""
Routes file for Recipes
"""
from fastapi import APIRouter, Depends

from src.api.routers.get_user_token import get_user_token
from src.api.routers.recipes.models.recipe_create_dto import RecipeCreateDto
from src.api.routers.recipes.models.recipe_response_dto import RecipeResponseDto
from src.core.recipes.application.recipes_creator import (
    RecipesCreator,
    RecipesCreatorParams,
)
from src.core.recipes.application.recipes_lister import RecipesLister
from src.core.recipes.infrastructure.dependencies import recipes_creator, recipes_lister
from src.shared.models.paginated_model import PaginatedModel
from src.shared.models.user_token_data import UserTokenData

router = APIRouter(prefix="/recipes", tags=["recipes"])


@router.get("", response_model=PaginatedModel[RecipeResponseDto])
async def index(
    recipes_lister_use_case: RecipesLister = Depends(recipes_lister),
):
    """
    Returns a list of recipes
    """
    [recipes, total_recipes] = recipes_lister_use_case.execute(0, 100)

    return PaginatedModel[RecipeResponseDto].serialize(
        list(map(RecipeResponseDto.from_domain_object, recipes)),
        total_recipes,
    )


@router.post("", status_code=201)
async def create(
    recipe_create_dto: RecipeCreateDto,
    # user_token: UserTokenData = Depends(get_user_token),
    recipes_creator_use_case: RecipesCreator = Depends(recipes_creator),
):
    """
    Creates a recipe
    """

    created_recipe = recipes_creator_use_case.execute(
        RecipesCreatorParams(**recipe_create_dto.dict())
    )

    return RecipeResponseDto.from_domain_object(created_recipe)
