from django.urls import path

from .views import (AddIngredients, CreateRecipe, EditIngredient,
                    IngredientsList, RecipeDetail, RecipesList, UpdateRecipe)

urlpatterns = [
    path('', RecipesList.as_view(), name='recipes-list'),
    path('<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
    path('add/', CreateRecipe.as_view(), name='create-recipe'),
    path('<int:pk>/edit/', UpdateRecipe.as_view(), name='update-recipe'),
    path('ingredients/', IngredientsList.as_view(), name='ingredients-list'),
    path('ingredients/add/', AddIngredients.as_view(), name='add-ingredient'),
    path('ingredients/<int:pk>/edit/',
         EditIngredient.as_view(), name='edit-ingredient'),
]
