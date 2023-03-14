import django_filters
from restaurant.models import Food, FoodCategory, Topping


class FoodFilter(django_filters.FilterSet):
    class Meta:
        model = Food
        fields = ['is_vegan', 'is_special', 'toppings']
