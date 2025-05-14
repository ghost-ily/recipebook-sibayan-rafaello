from django.urls import path

from .views import RecipeListView, RecipeDetailView, add_recipe, AddImageView

urlpatterns = [
    path('recipe/list', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/<int:pk>/add_image', AddImageView.as_view(), name='image_add'),
    path('recipe/add', add_recipe, name='recipe_add'),
]

app_name = "ledger"
