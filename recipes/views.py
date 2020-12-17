from django.shortcuts import render
from django.views.generic.base import View

from .models import Recipe


class RecipesView(View):
    def get(self, request):
        recipes = Recipe.objects.all()
        return render(request, "recipe_list.html", {"recipe_list": recipes})

class RecipeDetailView(View):
    def get(self, request, pk):
        recipe = Recipe.objects.get(id=pk)
        return render(request, "recipe_detail.html", {"recipe": recipe})

