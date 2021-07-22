from django.db import models


class TimeStampMixin:
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


class Unit(models.Model, TimeStampMixin):
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
