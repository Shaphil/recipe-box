from decimal import Decimal

from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .models import Ingredients, Recipe, RecipeIngredients


class RecipesList(ListView):
    """Lists all recipes"""

    queryset = Recipe.objects.order_by('-created_at')
    paginate_by = 5


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


class IngredientsList(ListView):
    queryset = Ingredients.objects.order_by('name')
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('query', None)
        if query is None:
            return super().get_queryset()

        return Ingredients.objects.filter(
            Q(name__icontains=query) | Q(article_number__icontains=query)
        ).order_by('name')


class AddIngredients(CreateView):
    model = Ingredients
    fields = ('name', 'article_number', 'unit',
              'unit_amount', 'price_per_unit_amount')
    success_url = reverse_lazy('ingredients-list')
