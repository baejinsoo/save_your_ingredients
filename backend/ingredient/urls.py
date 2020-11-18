from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import IngredientView

ingredient_list = IngredientView.as_view({
    'post': 'create',
    'get': 'list'
})

ingredient_detail = IngredientView.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('ingredient/', ingredient_list, name='ingredient_list'),
    path('ingredient/<int:pk>/', ingredient_detail, name='ingredient_detail'),
])