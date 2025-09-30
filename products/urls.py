from django.urls import path
from .views import *

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path("menu-items/filter/", manu_items_by_xategory, name="menu_items_by_category"),
]