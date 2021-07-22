from django.db import models


class TimeStampMixin:
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


class Unit(models.Model, TimeStampMixin):
    """Represents a metric unit of measurement.

    Base units are:
        mass -> grams
        volume -> liter
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

    def __str__(self):
        return self.symbol
