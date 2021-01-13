from rest_framework import serializers

from .models import Recipe, Comments, Assessment


class RecipeListSerializer(serializers.ModelSerializer):
    # Вывод списка рецептов#
    class Meta:
        model = Recipe
        fields = ("title", "description", "image")


class FilterCommentsSerializer(serializers.ListSerializer):
    # Фильтр родительских комментариев#

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.ModelSerializer):
    # Рекурсивный вывод дочерних комментариев#

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentCreateSerializer(serializers.ModelSerializer):
    # Вывод комментариев к рецептам#
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCommentsSerializer
        model = Comments
        fields = ("comment", "children")


class RecipeDetailSerializer(serializers.ModelSerializer):
    # Вывод детальной информации о рецепте#
    ingredients = serializers.SlugRelatedField(slug_field="ingredient_name", read_only=True, many=True)
    comments = CommentCreateSerializer(many=True)

    class Meta:
        model = Recipe
        exclude = ("")


class CreateAssessmentSerializer(serializers.ModelSerializer):
    # Создание или изменение новой оценки#
    class Meta:
        model = Assessment
        fields = ("id_recipe", "assessment", "date", "id_user")

    def create(self, validated_data):
        assessment = Assessment.objects.update_or_create(
            id_recipe=validated_data.get('id_recipe', None),
            id_user=validated_data.get('id_user', None),
            date=validated_data.get('date', None),
            defaults={'assessment': validated_data.get('assessment')}
        )
        return assessment


class DeleteAssessmentSerializer(serializers.ModelSerializer):
    # Создание или изменение новой оценки#
    class Meta:
        model = Assessment
        fields = ("id_recipe", "assessment", "date", "id_user")

    def delete(self, pk):
        assessment = Assessment.objects.filter(id=pk).delete()
        return assessment
