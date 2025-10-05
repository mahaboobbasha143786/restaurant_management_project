import string
import secrets
from . models import Coupon
def generate_coupon_code(length = 10):
    characters = ftring.ascii_uppercase + string.digits

    while True:
        code = ''.join(secrets.choice(characters)for _ in range())
        if not Coupon.objects.filter(code=code).exist():
            return code

from datetime import date
from django.db.models import Sum
from .models import Order

def get_daily_sales_total(specific_date):
    orders = Order.objects.filter(created_at__date=specific_date)

    total = orders.aggregate(total_sum=Sum('total_prince'))['total_sum']

    return total or 0