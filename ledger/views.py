from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView
from .models import Recipe


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipe_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
   

class PasswordResetView(PasswordResetView):
    template_name = 'password_reset_form.html'