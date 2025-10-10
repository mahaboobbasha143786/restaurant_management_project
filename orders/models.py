from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from home.models import Product

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

class ActiveOrderManager(models.Model):
    def get_queryset(self):
        return super().get_queryset().exclude(status='cancelled')

class Order(models.Model):
    STATUS_CHOICES =[
        ('pending', 'pending'),
        ('processing', 'processing'),
        ('completed', 'completed'),
        ('cancelled', 'canelled')

    ]

    customer_name = models.CharField(max_lenght=100)
    total_amount = models.DecimalField(max_digit=10, decimal_places=2)
    status = models.CharField(max_lenght=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ActiveOrderManager()

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name} ({self.status})"

