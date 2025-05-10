from django.db import models
from django.forms import ModelForm, CharField
from ledger.models import Recipe
from django.utils.translation import gettext_lazy as _


class AddRecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["name"]
        labels = {
            "name": _("Recipe Name"),
        }