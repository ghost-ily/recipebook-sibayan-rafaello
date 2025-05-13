from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from .models import Recipe, Ingredient, RecipeIngredient, Profile
from .forms import NewRecipeForm, IngredientFormSet


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipe_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'



def add_recipe(request):
    ingredientform = IngredientFormSet()
    recipeform = NewRecipeForm()
    ctx = {"ingredientform": ingredientform, "recipeform": recipeform }

    if request.method == 'POST':
        recipeform = NewRecipeForm(request.POST)
        ingredientform = IngredientFormSet(request.POST)
        
        if (recipeform.is_valid() and ingredientform.is_valid()):
            r = Recipe()
            recipeName = recipeform.cleaned_data.get('name')
            r.name = recipeName
            user = request.user.get_username()
            r.author = Profile.objects.get(name__exact=user)
            r.save()
            
            i = Ingredient()
            ingredientName = ingredientform.cleaned_data.get('name')
            i = ingredientName
            i.save()
            
            ri = RecipeIngredient()
            ri.quantity = ingredientform.cleaned_data.get('quantity')
            ri.ingredient = Ingredient.objects.get(name__exact="ingredientName")
            ri.recipe = Recipe.objects.get(name__exact="recipeName")
            ri.save()
            
    else:
        ingredientform = ()
        
    return render(request, 'recipe_form.html', ctx)