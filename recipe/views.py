from django.views.generic import ListView, DetailView

from .models import Recipe, RecipeIngredients

from decimal import Decimal


class RecipesList(ListView):
    """Lists all recipes"""

    queryset = Recipe.objects.all()


class RecipeDetail(DetailView):

    model = Recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = context.get('recipe')
        recipe_ingredients = RecipeIngredients.objects.filter(
            recipe_id=recipe.id)

        total_price = Decimal('0.0')
        for ingredient in recipe_ingredients:
            total_price += round(ingredient.price, 2)

        context['ingredients'] = recipe_ingredients
        context['total_price'] = round(total_price, 2)

        return context
