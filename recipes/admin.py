from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.utils.safestring import mark_safe
from .models import Ingredients, Country, Section, Kitchen, Recipe, Favorites, Comments, Assessment

class CommentsInline(admin.TabularInline):
    model = Comments
    extra = 1
    readonly_fields = ("id_recipe", "comment", "id_user")
    save_on_top = True

@admin.register(Ingredients)
class IngredientsAdmin(ImportExportModelAdmin):
    list_display = ("ingredient_name", "proteins", "fats", "carbohydrates")
    search_fields = ("ingredient_name", )
    pass

@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ("country_name",)
    search_fields = ("country_name", )
    pass

admin.site.register(Section)
admin.site.register(Kitchen)

@admin.register(Recipe)
class RecipeAdmin(ImportExportModelAdmin):
    list_display = ("title", "get_image", "id_section", "id_kitchen", "description", "steps")
    list_display_links = ("title", )
    list_filter = ("id_section", "id_kitchen")
    search_fields = ("title", "description")

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Изображение"

    inlines = [CommentsInline]
    pass

admin.site.register(Favorites)
@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("id_recipe", "comment", "id_user")
    list_display_links = ("comment", )

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ("id_recipe", "assessment", "id_user")
