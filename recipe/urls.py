from django.urls import path

from .views import RecipesList


urlpatterns = [
    path('', RecipesList.as_view(), name='recipes-list'),
]
