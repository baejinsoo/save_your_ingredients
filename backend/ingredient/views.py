from rest_framework import viewsets
from .serializers import IngredientSerializer
from .models import Ingredient
from rest_framework import permissions


class IngredientView(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permisson_classes = (permissions.IsAuthenticated, )

    def ingredient_create(self, serializer):
        serializer.save(user=self.request.user)