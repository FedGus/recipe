from rest_framework import serializers

from .models import Recipe, Comments


class RecipeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ("title", "description", "image")

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"

class RecipeDetailSerializer(serializers.ModelSerializer):
    ingredients = serializers.SlugRelatedField(slug_field="ingredient_name", read_only=True, many=True)
    comments = CommentCreateSerializer(many=True)

    class Meta:
        model = Recipe
        exclude = ("")