from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.RecipesView.as_view()),
    path("<int:pk>/", views.RecipeDetailView.as_view()),
    path("recipe/", views.RecipeListView.as_view())
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)