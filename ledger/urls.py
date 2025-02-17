from django.urls import path

from .views import index, recipe_list

urlpatterns = [
    path('', index, name='index'),
    path('recipe/list', recipe_list, name='recipe_list'),
]

app_name = "ledger"