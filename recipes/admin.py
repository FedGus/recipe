from django.contrib import admin

from .models import Ingredients, Country, Section, Kitchen, Recipe, Favorites, Comments, Assessment

admin.site.register(Ingredients)
admin.site.register(Country)
admin.site.register(Section)
admin.site.register(Kitchen)
admin.site.register(Recipe)
admin.site.register(Favorites)
admin.site.register(Comments)
admin.site.register(Assessment)
