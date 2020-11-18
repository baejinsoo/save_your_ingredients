from django.db import models
from ingredient.models import Ingredient
from django.contrib.auth.models import User


class Stock(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    expiration_date = models.DateField(auto_now_add=True)
    amount = models.CharField(max_length=2)
    expiration_date = models.DateField()