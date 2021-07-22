from decimal import Decimal

from django.db import models


class Unit(models.Model):
    """Represents a unit of measurement.

    Default units are:
        mass -> grams
        volume -> centiliter

    If Ingredient and RecipeIngredient have the same `unit_type`
        1. and have the same symbol then price can be calculated directly
        2. but have different symbol, then the units are converted to the
           default unit
        then the price = amount / unit_amount * price_per_unit_amount
    else, there is a unit_type mismatch and price cannot be calculated. An
    error is displayed.
    """

    unit_choices = (
        ('solid', 'Solid'),
        ('liquid', 'Liquid'),
        ('solid_and_liquid', 'Solid and Liquid')
    )

    name = models.CharField(max_length=32)
    unit_type = models.CharField(max_length=32, choices=unit_choices)
    multiplier = models.FloatField(null=True)
    symbol = models.CharField(max_length=16)
    is_default = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.symbol


class Ingredients(models.Model):

    class Meta:
        verbose_name_plural = 'Ingredients'

    name = models.CharField(max_length=128, blank=False, null=False)
    article_number = models.CharField(max_length=16, blank=True, null=True)
    unit = models.ForeignKey(
        Unit, null=True, blank=True, on_delete=models.SET_NULL)
    unit_amount = models.FloatField(blank=True, null=True)
    price_per_unit_amount = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name[:16]}...'


class RecipeIngredients(models.Model):

    class Meta:
        verbose_name_plural = 'Recipe Ingredients'

    recipe = models.ForeignKey(
        Recipe, null=False, blank=False, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(
        Ingredients, null=False, blank=False, on_delete=models.CASCADE)
    unit = models.ForeignKey(
        Unit, null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.FloatField(blank=True, null=True)

    @property
    def price(self):
        _price = None
        if self.ingredient.unit.unit_type == self.unit.unit_type:
            _amount = self.amount
            _unit_amount = self.ingredient.unit_amount
            if self.ingredient.unit.symbol != self.unit.symbol:
                default_unit = Unit.objects.filter(
                    unit_type=self.unit.unit_type).filter(is_default=True)[0]

                if not self.ingredient.unit.is_default:
                    _unit_amount = self.ingredient.unit_amount * default_unit.multiplier

                if not self.unit.is_default:
                    _amount = self.amount * default_unit.multiplier

            _price = Decimal(str(_amount / _unit_amount)) * \
                self.ingredient.price_per_unit_amount

        return _price

    def __str__(self):
        return f'{self.ingredient.name} for {self.recipe.name[:16]}...'
