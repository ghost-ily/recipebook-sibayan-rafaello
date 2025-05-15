from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Recipe, Ingredient, RecipeIngredient, Profile, RecipeImage
from .forms import NewRecipeForm, IngredientFormSet, ImageForm


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipe_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'


@login_required
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
            
            for form in ingredientform:
                ingredientName = form.cleaned_data.get('name')
                ingredientCount = form.cleaned_data.get('quantity')
                if (ingredientName == None) or (ingredientCount == None):
                    continue
                ingredientName = ingredientName.lower()
                obj, created = Ingredient.objects.get_or_create(name=ingredientName)
                
                ri = RecipeIngredient()
                ri.quantity = form.cleaned_data.get('quantity')
                ri.ingredient = Ingredient.objects.get(name=ingredientName)
                ri.recipe = Recipe.objects.get(name=recipeName)
                ri.save()
        
    return render(request, 'recipe_form.html', ctx)


class AddImageView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = ImageForm
    template_name = "image_upload.html"
    success_url = "recipe/{pk}"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ImageForm()
        self.pk = self.kwargs['pk']
        return context
    
    def form_valid(self, form):
        pk = self.kwargs['pk']
        form.instance.recipe = Recipe.objects.get(pk=pk)
        form.save()
        success_url = reverse_lazy("ledger:recipe_detail", kwargs={'pk': pk})
        return redirect(success_url)


def add_image(request, pk):
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST)
        
        if form.is_valid():
            img = RecipeImage()
            img.file = form.FILES.get('image')
            img.description = form.cleaned_data.get('alt')
            id = self.kwargs['pk']
            img.recipe = Recipe.objects.get(id)
        
    return render(request, 'image_upload.html', {"image_form": form})