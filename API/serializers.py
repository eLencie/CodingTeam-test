from rest_framework import serializers
from restaurant.models import Food, FoodCategory, Topping


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ['name']


class FoodSerializer(serializers.ModelSerializer):
    toppings = serializers.SerializerMethodField()

    def get_toppings(self, obj):
        return list(topping.name for topping in obj.toppings.all())

    class Meta:
        model = Food
        fields = ['name', 'description', 'price', 'is_vegan', 'is_special', 'toppings']


class FoodCategorySerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True, read_only=True)

    class Meta:
        model = FoodCategory
        fields = ['id', 'name', 'foods']

