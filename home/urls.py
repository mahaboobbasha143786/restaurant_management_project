from django.urls import path, include
from .views import *

urlpatterns = [
    path('categories/', MenuCategoryListView.as_view(), name = 'menu-categories'),
    path('api/', include('home.urls')),
    path('api/tables/<int:pk>/', TableDetailView.as_view(),name='time-detail'),
    path('api/tables/available/', AvailableTablesAPIView.as_view(), name='available_tables_api'),
]