from django.shortcuts import render
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import UserUpdateSerializer

class UserProfileView(RetrieveUpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

# Create your views here.
