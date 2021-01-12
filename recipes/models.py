from multiprocessing.reduction import register

from django.db import models
from django.conf import settings

class Ingredients(models.Model):
    ingredient_name = models.CharField("Ингредиент", max_length=150)
    proteins = models.FloatField("Белки", default=0)
    fats = models.FloatField("Жиры", default=0)
    carbohydrates = models.FloatField("Углеводы", default=0)

    def __str__(self):
        return self.ingredient_name

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"

class Country(models.Model):
    country_name = models.CharField("Страна", max_length=150)

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

class Section(models.Model):
    name_section = models.CharField("Название раздела", max_length=150)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name_section

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"

class Kitchen(models.Model):
    id_country = models.ForeignKey(Country, verbose_name="страны", on_delete=models.SET_NULL, null=True)
    name_kitchen = models.CharField("Название кухни", max_length=150)

    def __str__(self):
        return self.name_kitchen

    class Meta:
        verbose_name = "Кухня"
        verbose_name_plural = "Кухни"

class Recipe(models.Model): 
    id_section = models.ForeignKey(Section, verbose_name="раздел", on_delete=models.SET_NULL, null=True)
    id_kitchen = models.ForeignKey(Kitchen, verbose_name="кухня", on_delete=models.SET_NULL, null=True)
    ingredients = models.ManyToManyField(Ingredients, verbose_name="ингредиенты", related_name="ingredients_recipe")
    title = models.CharField("Название рецепта", max_length=150)
    description = models.TextField("Описание")
    steps = models.TextField("Шаги приготовления")
    image = models.ImageField("Изображение", upload_to="media/", null=True)

    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="пользователь автор", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

class Favorites(models.Model):
    id_recipe = models.ForeignKey(Recipe, verbose_name="рецепт", on_delete=models.SET_NULL, null=True)

    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="пользователь избранное", on_delete=models.SET_NULL, null=True)
  
    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные рецепты"

class Comments(models.Model):
    id_recipe = models.ForeignKey(Recipe, verbose_name="рецепт", on_delete=models.SET_NULL, null=True, related_name="comments")
    comment = models.TextField("Комментарий")

    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="пользователь комментарий", on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Коментарии"

class Assessment(models.Model):
    id_recipe = models.ForeignKey(Recipe, verbose_name="рецепт", on_delete=models.SET_NULL, null=True)
    assessment = models.PositiveSmallIntegerField("Оценка", default=0)

    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="пользователь оценка", on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"
