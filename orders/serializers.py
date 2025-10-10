from rest_framework import serializers
from .models import Order, OrderItem
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["name", "price", "quantity"]

    class OrderSerializer(serializers.ModelSerializer):
        items = OrderItemSerializer(many=True, read_only= True)

        class Meta:
            model = Order
            fields = ["id","customer_name", "created_at", "total_price", "items"]