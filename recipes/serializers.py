from rest_framework import serializers

from .models import Recipe

class RecipeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ("title", "description")