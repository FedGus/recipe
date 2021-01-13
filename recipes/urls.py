from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.RecipesView.as_view()),
    path("<int:pk>/", views.RecipeDetailView.as_view()),
    path("recipe/", views.RecipeListAPIView.as_view()),
    path("recipe/<int:pk>", views.RecipeDetailAPIView.as_view()),
    path("comment/", views.CommentCreateView.as_view()),
    path("assessment/", views.AddAssessmentView.as_view()),
    path("assessment/<int:pk>", views.DeleteAssessmentView.as_view()),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)