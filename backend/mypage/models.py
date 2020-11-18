from django.db import models
from recipe.models import Recipe
from django.contrib.auth.models import User

# Create your models here.


class UserDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wish_recipes = models.ManyToManyField(Recipe)
    total_time = models.IntegerField()
    # ExperienceRecipe가 One To Many로 들어가있음


class ExperienceRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    user_detail = models.ForeignKey(
        UserDetail, related_name='experiencerecipe', on_delete=models.CASCADE)
