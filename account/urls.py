from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', UserProfileUpdateView.as_view(), name='user-profile'),
    
]