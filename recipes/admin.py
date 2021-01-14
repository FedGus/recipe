from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.utils.safestring import mark_safe
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from .models import Ingredients, Country, Section, Kitchen, Recipe, Favorites, Comments, Assessment


class CommentsInline(admin.TabularInline):
    model = Comments
    extra = 1
    readonly_fields = ("id_recipe", "comment", "parent", "id_user")
    save_on_top = True


@admin.register(Ingredients)
class IngredientsAdmin(ImportExportModelAdmin):
    list_display = ("ingredient_name", "proteins", "fats", "carbohydrates")
    search_fields = ("ingredient_name",)
    pass


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ("country_name",)
    search_fields = ("country_name",)
    pass


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("name_section", "description")


@admin.register(Kitchen)
class KitchenAdmin(admin.ModelAdmin):
    list_display = ("name_kitchen", "id_country", )


@admin.register(Recipe)
class RecipeAdmin(ImportExportModelAdmin):
    list_display = ("title", "get_image", "id_section", "id_kitchen", "description", "status")
    list_display_links = ("title",)
    list_filter = ("id_section", "id_kitchen")
    search_fields = ("title", "description")
    actions = ["publish", "unpublish"]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    def unpublish(self, request, queryset):
        row_update = queryset.update(status=False)
        if row_update == 1:
            message_bit = "1 запись обновлена"
        else:
            message_bit = f"{row_update} записей обновлено"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        row_update = queryset.update(status=True)
        if row_update == 1:
            message_bit = "1 запись обновлена"
        else:
            message_bit = f"{row_update} записей обновлено"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ("change",)

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ("change",)

    get_image.short_description = "Изображение"

    inlines = [CommentsInline]
    pass


@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    list_display = ("id_recipe", "id_user")


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("id_recipe", "comment", "id_user")
    list_display_links = ("comment",)


@admin.register(Assessment)
class AssessmentAdmin(ImportExportModelAdmin):
    list_display = ("id_recipe", "assessment", "id_user", "date")
    list_filter = (
        'assessment',
        ('date', DateRangeFilter),
    )
