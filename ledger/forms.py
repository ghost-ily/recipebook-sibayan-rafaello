from django import forms, formset_factory
from .models import Recipe, Ingredient


class NewRecipeForm(forms.Form):
    name = forms.CharField(label='Recipe Name', max_length=100)

  
class IngredientForm(forms.Form):
    quantity = forms.CharField(label='Quantity', max_length=10)
    ingredient = forms.CharField(label='Ingredient', max_length=100)


IngredientFormSet = formset_factory(IngredientForm)