from django.contrib import admin

from .models import Recipe, Ingredient, RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    
    search_fields = ('name', )

admin.site.register(Recipe, RecipeAdmin)
# Register your models here.
