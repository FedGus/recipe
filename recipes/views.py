from django.shortcuts import render
from django.views.generic.base import View

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Recipe, Ingredients
from .serializers import RecipeListSerializer, RecipeDetailSerializer, CommentCreateSerializer


class RecipesView(View):
    def get(self, request):
        recipes = Recipe.objects.all()
        return render(request, "recipe_list.html", {"recipe_list": recipes})


class RecipeListAPIView(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeListSerializer(recipes, many=True)
        return Response(serializer.data)


class RecipeDetailView(View):
    def get(self, request, pk):
        recipe = Recipe.objects.get(id=pk)
        return render(request, "recipe_detail.html", {"recipe": recipe})


class RecipeDetailAPIView(APIView):
    def get(self, request, pk):
        recipe = Recipe.objects.get(id=pk)
        serializer = RecipeDetailSerializer(recipe)
        return Response(serializer.data)


class CommentCreateView(APIView):
    def post(self, request):
        comment = CommentCreateSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
        return Response(status=201)
