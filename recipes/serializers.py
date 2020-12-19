from rest_framework import serializers

from .models import Recipe

class RecipeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ("title", "description", "image")

class RecipeDetailSerializer(serializers.ModelSerializer):
    ingredients = serializers.SlugRelatedField(slug_field="ingredient_name", read_only=True, many=True)
    class Meta:
        model = Recipe
        exclude = ("")