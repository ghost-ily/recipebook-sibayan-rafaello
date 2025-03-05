from django.urls import path

from .views import RecipeListView, recipe_1, recipe_2

urlpatterns = [
    path('recipe/list', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/1', recipe_1, name='recipe_1'),
    path('recipe/2', recipe_2, name='recipe_2'),
]

app_name = "ledger"