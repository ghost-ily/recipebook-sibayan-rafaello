from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, RecipeIngredient
from .forms import AddRecipeForm


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipe_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'

class AddRecipeForm(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = AddRecipeForm
    template_name = 'recipe_form.html'