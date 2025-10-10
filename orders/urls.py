from django.urls import path
from .views import *

urlpatterns = [
    path("orders/history/", OrderHistoryView(), name="order-history"),
    path("<int:id>/", OrderDetailView.as_view(), name='order-detail'),
    
]