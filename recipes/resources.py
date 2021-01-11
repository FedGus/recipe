from import_export import resources
from recipes.models import Recipe

class RecipesResources(resources.ModelResource):
    class Meta:
        model = Recipe