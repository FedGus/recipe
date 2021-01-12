from rest_framework import serializers

from .models import Recipe, Comments


class RecipeListSerializer(serializers.ModelSerializer):
    #Вывод списка рецептов#
    class Meta:
        model = Recipe
        fields = ("title", "description", "image")

class FilterCommentsSerializer(serializers.ListSerializer):
    #Фильтр родительских комментариев#

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)

class RecursiveSerializer(serializers.ModelSerializer):
    #Рекурсивный вывод дочерних комментариев#

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class CommentCreateSerializer(serializers.ModelSerializer):
    #Вывод комментариев к рецептам#
    children = RecursiveSerializer(many=True)
    class Meta:
        list_serializer_class = FilterCommentsSerializer
        model = Comments
        fields = ("comment", "children")

class RecipeDetailSerializer(serializers.ModelSerializer):
    #Вывод детальной информации о рецепте#
    ingredients = serializers.SlugRelatedField(slug_field="ingredient_name", read_only=True, many=True)
    comments = CommentCreateSerializer(many=True)

    class Meta:
        model = Recipe
        exclude = ("")