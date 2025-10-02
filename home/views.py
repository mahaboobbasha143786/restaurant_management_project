from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination 
from .models import MenuItem
from rest_framework import viewset, status
from rest_framework,reponse import Response
from .serializers import MenuItemSerializer

# Create your views here.
class MenuCategoryList view(ListAPIView):
    queyset = MenuCategory.objects.all()
    serializer_c;ass = MenuCategorySerializer
    
class MenuItemSearchPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page = 50

class MenuItemSearchViewSet(viewsets.ViewSet):
    pagination_class = MenuItemSearchPagination
    def list(self, request):
        query = request.query_params.get("q", "")
        items = MenuItem.objects.all()

        if query:
            items = items.filter(name__icontains=query)

        paginatior = self.pagination_class()
        page = paginatior.paginate_queryset(items, request)
        serializer = MenuItemSerializer(page, many=True)

        return paginatior.get_paginated_response(serializer.data)