from django.urls import path

from .views import IngredientsList, RecipeDetail, RecipesList

urlpatterns = [
    path('', RecipesList.as_view(), name='recipes-list'),
    path('<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
    path('ingredients/', IngredientsList.as_view(), name='ingredients-list'),
]
