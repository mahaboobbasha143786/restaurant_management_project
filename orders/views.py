from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenicated
from .models import Order
from .serializers import OrderSerializer

class OrderHistoryView(APIView):
    permission_classes = [IsAuthenicated]
    def get(self, request):
        orders = Order.objects.filter(user=request.user).order_by('-created_at')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

# Create your views here.
class CouponValidationView(APIView):
    def post(self, request, *args, **kwargs):
        code = request.data.get("code")

        if not code:
            return Response({"error": "Coupon code is required."}, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            coupon = Coupon.objects.get(code__iexact=code)
        except Coupon.DoesNotExist:
            return Response({"error": "Invalid coupon code."}, status=status.HTTP_400_BAD_REQUEST)

        today = timezone.now().date()

        if not coupon.is_active():
            return Response({"error": "This coupon is no longeractive."}, status=status.HTTP_400_BAD_REQUEST)

        if not (coupon.valid_from <= today <= coupon.valid_until):
            return Response({"error": "This coupon is not valid for today."}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "success": True,
            "message": "Coupon is valid.",
            "discount_percentage": float(coupon.discount_percentage)
        }, status=status.HTTP_200_OK)