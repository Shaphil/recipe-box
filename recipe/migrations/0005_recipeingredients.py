# Generated by Django 3.2.5 on 2021-07-22 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(blank=True, null=True)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.ingredients')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipe.unit')),
            ],
        ),
    ]
