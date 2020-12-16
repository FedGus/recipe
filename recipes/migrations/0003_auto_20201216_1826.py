# Generated by Django 3.1.4 on 2020-12-16 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_assessment_comments_country_favorites_kitchen_recipe_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to='media/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='carbohydrates',
            field=models.FloatField(default=0, verbose_name='Углеводы'),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='fats',
            field=models.FloatField(default=0, verbose_name='Жиры'),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='proteins',
            field=models.FloatField(default=0, verbose_name='Белки'),
        ),
    ]
