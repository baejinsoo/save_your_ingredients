from django.urls import path, include
from .views import StockView, StockDetailView

urlpatterns = [
    path('stock/', StockView.as_view(), name='stock_list'),
    path('stock/<int:stock_id>/', StockDetailView.as_view(), name='stock_detail')
    # path('stock/<int:pk>/', stock_detail, name='stock_detail'),
]
