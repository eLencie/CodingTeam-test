from django.shortcuts import render
from rest_framework import generics, serializers
from restaurant.models import Food, FoodCategory, Topping
from .serializers import FoodCategorySerializer, FoodSerializer
from django.db.models import Prefetch
from django_filters import rest_framework as filters
from API.filters import FoodFilter


class FoodCategoryList(generics.ListAPIView):
    queryset = FoodCategory.objects.prefetch_related(Prefetch('foods', queryset=Food.objects.filter(
        is_publish=True)), 'foods__toppings')
    serializer_class = FoodCategorySerializer


class FoodList(generics.ListAPIView):
    queryset = Food.objects.prefetch_related('toppings').filter(is_publish=True)
    serializer_class = FoodSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FoodFilter

