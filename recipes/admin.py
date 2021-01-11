from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.utils.safestring import mark_safe
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
    list_display = ("id_section", "id_kitchen", "title", "description", "steps", "get_image")

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="120"')

    get_image.short_description = "Изображение"
    pass

admin.site.register(Favorites)
admin.site.register(Comments)
admin.site.register(Assessment)
