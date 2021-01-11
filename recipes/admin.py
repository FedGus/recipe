from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Ingredients, Country, Section, Kitchen, Recipe, Favorites, Comments, Assessment

@admin.register(Ingredients)
class PracticeAdmin(ImportExportModelAdmin):
    list_display = ("ingredient_name", "proteins", "fats", "carbohydrates")
    pass

@admin.register(Country)
class PracticeAdmin(ImportExportModelAdmin):
    list_display = ("country_name",)
    pass

admin.site.register(Section)
admin.site.register(Kitchen)

@admin.register(Recipe)
class PracticeAdmin(ImportExportModelAdmin):
    list_display = ("id_section", "id_kitchen", "title", "description", "steps", "image")
    pass

admin.site.register(Favorites)
admin.site.register(Comments)
admin.site.register(Assessment)
