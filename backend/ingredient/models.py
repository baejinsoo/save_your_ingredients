from django.db import models

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    trim = models.CharField(max_length=255)
