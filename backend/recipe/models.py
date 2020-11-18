from django.db import models


# Create your models here.
class Recipe(models.Model):
    reci_id = models.CharField(max_length=100)
    ingredient_ids = models.CharField(max_length=255)

    def __str__(self):
        return str(self.reci_id)
