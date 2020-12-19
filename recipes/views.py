from django.shortcuts import render
from django.views.generic.base import View

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Recipe
from .serializers import RecipeListSerializer


class RecipesView(View):
    def get(self, request):
        recipes = Recipe.objects.all()
        return render(request, "recipe_list.html", {"recipe_list": recipes})

class RecipeListView(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeListSerializer(recipes, many=True)
        return Response(serializer.data)

class RecipeDetailView(View):
    def get(self, request, pk):
        recipe = Recipe.objects.get(id=pk)
        return render(request, "recipe_detail.html", {"recipe": recipe})

