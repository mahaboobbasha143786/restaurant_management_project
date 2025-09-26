from django.urls import path, include
from .views import *

urlpatterns = [
    path('categories/', MenuCategoryListView.as_view(), name = 'menu-categories'),
    path('api/', include('home.urls')),
]