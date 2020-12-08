from django.db import models

class Ingredients(models.Model):

    ingredient_name = models.CharField("Ингредиент", max_length=150)
    proteins = models.PositiveSmallIntegerField("Белки", default=0)
    fats = models.PositiveSmallIntegerField("Жиры", default=0)
    carbohydrates = models.PositiveSmallIntegerField("Углеводы", default=0)

    def __str__(self):
        return self.ingredient_name

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"