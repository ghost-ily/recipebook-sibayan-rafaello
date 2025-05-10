from django.urls import path

from .views import RecipeListView, RecipeDetailView, AddRecipeForm

urlpatterns = [
    path('recipe/list', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/add', AddRecipeForm.as_view(), name='recipe_add')
]

app_name = "ledger"
