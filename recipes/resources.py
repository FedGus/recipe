from import_export import resources
from recipes.models import Recipe, Ingredients

class RecipesResources(resources.ModelResource):
    class Meta:
        model = Recipe

class IngredientsResources(resources.ModelResource):
    class Meta:
        model = Ingredients