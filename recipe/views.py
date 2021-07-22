from django.views.generic import ListView

from .models import Recipe


class RecipesList(ListView):
    """Lists all recipes"""

    queryset = Recipe.objects.all()
