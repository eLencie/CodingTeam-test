from django.urls import path, include
from .views import FoodCategoryList, FoodList

urlpatterns = [
    path('categories/', FoodCategoryList.as_view(), name='foodcategory-list'),
    path('food-filter/', FoodList.as_view(), name='food-list'),
]
