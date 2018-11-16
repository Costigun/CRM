from django.shortcuts import render
from .models import *
from .serializers import UserSerializer,OrderSerializer,CheckSerializer,MealSerialier
from rest_framework import generics,viewsets

"""
class UsersView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
"""
class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CheckView(generics.ListCreateAPIView):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer

class MealView(generics.ListCreateAPIView):
    queryset = Meals.objects.all()
    serializer_class = MealSerialier

class MealsToOrderView(generics.ListCreateAPIView):
    queryset = MealsToOrder.objects.all()
    serializer_class = MealsToOrder

class UserListView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer