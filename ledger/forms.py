from django import forms
from django.forms import formset_factory
from .models import Recipe, Ingredient


class NewRecipeForm(forms.Form):
    name = forms.CharField(label='Recipe Name', max_length=100)

  
class IngredientForm(forms.Form):
    name = forms.CharField(label='Ingredient', max_length=100)
    quantity = forms.CharField(label='Quantity', max_length=10)

IngredientFormSet = formset_factory(IngredientForm, extra=4)