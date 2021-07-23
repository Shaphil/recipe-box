from django.urls import path

from .views import (AddIngredients, EditIngredient, IngredientsList,
                    RecipeDetail, RecipesList)

urlpatterns = [
    path('', RecipesList.as_view(), name='recipes-list'),
    path('<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
    path('ingredients/', IngredientsList.as_view(), name='ingredients-list'),
    path('ingredients/add/', AddIngredients.as_view(), name='add-ingredient'),
    path('ingredients/<int:pk>/edit/',
         EditIngredient.as_view(), name='edit-ingredient'),
]
