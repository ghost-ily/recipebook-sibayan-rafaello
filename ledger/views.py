from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe, RecipeIngredient
from .forms import NewRecipeForm, IngredientFormSet


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipe_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'


@login_required
def add_recipe(request):
    if request.method == 'POST':
        recipeform = NewRecipeForm(request.POST)
        ingredientform = IngredientFormSet(request.POST)
        
        if recipeform.is_valid():
            r = Recipe()
            r.name = recipeform.cleaned_data.get('name')