from django.contrib import admin
from .models import Food, FoodCategory, Topping


admin.site.register(Food)
admin.site.register(FoodCategory)
admin.site.register(Topping)