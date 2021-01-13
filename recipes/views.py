from django.shortcuts import render
from django.views.generic.base import View

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Recipe, Ingredients, Assessment
from .serializers import RecipeListSerializer, RecipeDetailSerializer, CommentCreateSerializer, \
    CreateAssessmentSerializer, DeleteAssessmentSerializer


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


class AddAssessmentView(APIView):
    def post(self, request):
        serializer = CreateAssessmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        else:
            return Response(status=400)


class DeleteAssessmentView(APIView):
    def delete(self, request, pk):
        serializer = DeleteAssessmentSerializer(data=pk)
        if serializer.is_valid():
            return Response(status=201)
        else:
            return Response(status=400)
