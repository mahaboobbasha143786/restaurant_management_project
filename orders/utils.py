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

import logging
from django.core.mail import send_mail, BadHeaderError
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.conf import setting

logger = logging.getLogger(__name__)
def send_order_confirmation_email(order_id, customer_email, customer_name, total_amount, item_list):
    try:
        validate_email(customer_email)
        subject = f"Order Confirmation - #{order_id}"
        items_str = "\n".join(f"- {item}" for item in item_list)
        message = (
            f"Hello {customer_name}, \n\n"
            f"Thank you for your order!\n\n"
            f"Oredr ID: {order_id}\n"
            f"Items:\n{items_str}\n\n"
            f"Total Amount: ${total_amount}\n\n"
            "Your order is being processed. We'll notify you once it's shiped.\n\n"
            "Best regards, \n"
            "The Restaurant Management Team"
        )

        send_mail(
            subject,
            message,
            settings.DEFAULT_FORM_EMAIL,
            [customer_email],
            fail_silently=False,
        )
        logger.info(f"Order Confirmation email sent to {customer_email}")
        return {"seccess": True, "message": "Email sent successfully"}

    except ValidationError:
        logger.error(f"Invalid email: {customer_email}")
        return {"success": False, "message": "Inavlid email address"}

    except BadHeaderError:
        logger.error("Invalid header found while sending email")
        return {"success": False, "message": "Invalid email header"}

    except Exception as e:
        logger.exception(f"Error sending email: {e}")
        return {"success": False, "message": str(e)}