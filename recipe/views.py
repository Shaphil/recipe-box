from decimal import Decimal

from django.db.models import Q
from django.forms import inlineformset_factory
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import RecipeForm, RecipeIngredientsForm
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


extra = 5
ingredient_fields = ('ingredient', 'amount', 'unit',)
IngredientsFormSet = inlineformset_factory(
    Recipe, RecipeIngredients, fields=ingredient_fields, extra=extra)


class CreateRecipe(CreateView):
    # fields = ('name', 'description',)
    template_name = 'recipe/recipe_form.html'

    def get(self, request, *args, **kwargs):
        recipe_form = RecipeForm()
        ingredients_formset = IngredientsFormSet()
        context = {
            'recipe_form': recipe_form,
            'ingredients_formset': ingredients_formset
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()

        i = 0
        while i < extra:
            ingredient = request.POST.get(
                f'recipeingredients_set-{i}-ingredient')
            amount = request.POST.get(f'recipeingredients_set-{i}-amount')
            unit = request.POST.get(f'recipeingredients_set-{i}-unit')

            if ingredient:
                ingredient = int(ingredient)
                amount = float(amount) if amount else 0.0
                unit = int(unit) if unit else None
                RecipeIngredients.objects.create(
                    ingredient_id=ingredient,
                    recipe=recipe,
                    unit_id=unit,
                    amount=amount
                )
            i += 1

        return HttpResponseRedirect(recipe.get_absolute_url())


class AddIngredients(CreateView):
    model = Ingredients
    fields = ('name', 'article_number', 'unit',
              'unit_amount', 'price_per_unit_amount')
    success_url = reverse_lazy('ingredients-list')


class EditIngredient(UpdateView):
    model = Ingredients
    fields = ('name', 'article_number', 'unit',
              'unit_amount', 'price_per_unit_amount')
    success_url = reverse_lazy('ingredients-list')
