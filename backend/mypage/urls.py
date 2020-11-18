from django.urls import path, include
from .views import UserDetailView, WishRecipeView, ExperienceRecipeView

urlpatterns = [
    path('user-detail/', UserDetailView.as_view(), name='user-detail'),
    path('wish-recipe/', WishRecipeView.as_view(), name='wish-recipes'),
    path('experience-recipe/', ExperienceRecipeView.as_view(), name='experience-recipe'),
    # path('stock/<int:stock_id>/', StockDetailView.as_view(), name='stock_detail')
    # path('stock/<int:pk>/', stock_detail, name='stock_detail'),
]
