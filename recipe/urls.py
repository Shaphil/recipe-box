from django.urls import path

from .views import RecipeDetail, RecipesList

urlpatterns = [
    path('', RecipesList.as_view(), name='recipes-list'),
    path('<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
]
