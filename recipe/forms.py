from django.forms import ModelForm

from .models import Recipe, RecipeIngredients


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'description',)


class RecipeIngredientsForm(ModelForm):
    class Meta:
        model = RecipeIngredients
        fields = ('ingredient', 'amount', 'unit',)
