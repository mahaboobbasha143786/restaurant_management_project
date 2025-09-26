from django.db import models

from .models import OrderStatus

class Order(models.Model):
    customer_name = modelsCharFiled(max_length = 100)
    total_amount = models.DecimalField(max_digit=10, Decimal_places=2)
    created_at = modeels.DateTimeField(auto_now_add=True)

    status = models.ForegnKey(OrdeStatus, on_delete=models,SET_NULL, null=True,related_name='orders')
    def __str__(self):
        return f"Order {self.id} - {self.customer_name}"
