from django.db import models
from django.utils import timezone

from .models import OrderStatus

class Order(models.Model):
    customer_name = modelsCharFiled(max_length = 100)
    total_amount = models.DecimalField(max_digit=10, Decimal_places=2)
    created_at = modeels.DateTimeField(auto_now_add=True)

    status = models.ForegnKey(OrdeStatus, on_delete=models,SET_NULL, null=True,related_name='orders')
    def __str__(self):
        return f"Order {self.id} - {self.customer_name}"

class OrderItem(models.Model):
    order = models.ForegnKey(Order,on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digit=8,decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.name} (x{self.quantity})"
class Coupon(models.Model):
    code = models.CharField(max_lenght=50, unique=True)
    discount_percentage = models.DecimalField(max_digit=5, decimal_places=2)
    is_active = models.BooleanField(default=True)
    valid_from = models.DateField()
    valid_until = models.DateField()

    def __str__(self):
        return f"{self.code} - {self.discount_percentage}%"