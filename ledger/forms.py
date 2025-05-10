from django import forms
from ledger.models import Recipe

class AddRecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["name", "ingredients"]