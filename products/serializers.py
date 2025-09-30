from rest_framework import serializers
from .models import Item, MenuItem

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
