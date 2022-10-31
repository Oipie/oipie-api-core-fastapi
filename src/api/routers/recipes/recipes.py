"""
Routes file for Recipes
"""
from fastapi import APIRouter, Depends
from src.api.routers.recipes.models.recipe_out import RecipeOut
from src.core.recipes.application.recipes_lister import RecipesLister
from src.core.recipes.infrastructure.dependencies import recipes_lister
from src.shared.models.paginated_model import PaginatedModel


router = APIRouter(prefix="/recipes", tags=["recipes"])


@router.get("", response_model=PaginatedModel[RecipeOut])
# async def index(session: Session = Depends(get_database)):
async def index(
    recipes_lister_use_case: RecipesLister = Depends(recipes_lister),
):
    """
    Returns a list of recipes
    """
    [recipes, total_recipes] = recipes_lister_use_case.execute(0, 100)

    print(
        "total",
        total_recipes,
        "recipes parsed",
        list(map(RecipeOut.from_domain_object, recipes)),
    )

    return PaginatedModel[RecipeOut].serialize(
        list(map(RecipeOut.from_domain_object, recipes)),
        total_recipes,
    )
