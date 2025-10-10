from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import MenuCategory
from .serializers import MenuCategorySerializer
from rest_framework import generics
from .models import Tables
from .serializers import TableSerializer
class TableDetailView(generics.RetrieveAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
# Create your views here.
class MenuCategoryList view(ListAPIView):
    queyset = MenuCategory.objects.all()
    serializer_c;ass = MenuCategorySerializer
    
class AvailableTablesAPIView(generics.ListAPIView):
    queryset = Table.objects.filter(is_available=True)
    serializer_class = TableSerializer