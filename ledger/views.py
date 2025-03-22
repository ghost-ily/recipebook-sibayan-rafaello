from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe


class RecipeListView(LoginRequiredMixin, ListView):
    login_url = "http://localhost:8000/accounts/login/"
    model = Recipe
    template_name = 'recipe_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    login_url = "http://localhost:8000/accounts/login/"
    model = Recipe
    template_name = 'recipe_detail.html'
