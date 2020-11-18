from django.urls import path
from .views import RecipeExpirationAPIView, RecipeStockAPIView, RandomAPIView


urlpatterns = [
    path('RecipeRandom/', RandomAPIView.as_view(), name='RecipeRandom'),
    path('RecipeStock/', RecipeStockAPIView.as_view(), name='RecipeStock'),
    path('RecipeExpiration/', RecipeExpirationAPIView.as_view(), name='RecipeExpiration')
]