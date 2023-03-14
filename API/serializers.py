from rest_framework import serializers
from restaurant.models import Food, FoodCategory, Topping


class FoodSerializer(serializers.ModelSerializer):
    toppings = serializers.StringRelatedField(many=True)

    class Meta:
        model = Food
        fields = ['name', 'description', 'price', 'is_vegan', 'is_special', 'toppings']


class FoodCategorySerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True, read_only=True)

    class Meta:
        model = FoodCategory
        fields = ['id', 'name', 'foods']

