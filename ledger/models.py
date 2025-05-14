from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe_detail')


class Profile(models.Model):
    user = models.OneToOneField(
            User, 
            on_delete=models.CASCADE,
            primary_key=True,
        )
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=300)


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
            Profile,
            on_delete=models.CASCADE,
            null=True,
            related_name="author"
        )
    createdOn = models.DateTimeField(
            auto_now_add=True,
            null=True
        )
    updatedOn = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', kwargs={'pk':self.pk})


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)

    ingredient = models.ForeignKey(
            Ingredient,
            on_delete=models.CASCADE,
            null=True,
            related_name='recipe'
        )

    recipe = models.ForeignKey(
            Recipe,
            on_delete=models.CASCADE,
            null=True,
            related_name='ingredients'
        )


class RecipeImage(models.Model):
    file = models.ImageField(upload_to='images/', null=False)
    description = models.CharField(max_length=255)
    
    recipe = models.ForeignKey(
            Recipe,
            on_delete=models.CASCADE,
            related_name='image'
        )