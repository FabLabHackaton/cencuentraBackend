from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import *

class UserView(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = DefaultUserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


#ADMIN
class AdminView(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = DefaultAdminSerializer


class AdminDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = AdminSerializer

class AdminRegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = AdminRegisterSerializer
    permission_classes = [permissions.AllowAny]
