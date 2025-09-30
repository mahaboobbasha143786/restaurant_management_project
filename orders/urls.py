from django.urls import path
from .views import *

urlpatterns = [
    path("orders/history/", OrderHistoryView(), name="order-history"),
    
]