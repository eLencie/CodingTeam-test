from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from restaurant.models import Food, FoodCategory, Topping
import json


class APITests(TestCase):
	def setUp(self):
		self.category1 = FoodCategory.objects.create(name='Горячие блюда', is_publish=True)
		self.topping1 = Topping.objects.create(name='Сыр')
		self.food1 = Food.objects.create(
			category=self.category1,
			name='Суп',
			description='Вкусный сырный суп',
			price=180,
			is_special=True,
			is_vegan=False,
			is_publish=True,
		)
		self.food1.toppings.add(self.topping1)

		self.category2 = FoodCategory.objects.create(name='Салаты', is_publish=True)
		self.topping2 = Topping.objects.create(name='Майонез')
		self.food2 = Food.objects.create(
			category=self.category2,
			name='Оливье',
			description='Вкусное майонезное оливье',
			price=140,
			is_special=False,
			is_vegan=True,
			is_publish=False,
		)
		self.food2.toppings.add(self.topping2)

	def test_categories_list(self):
		response = self.client.get(reverse('foodcategory-list'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 2)  # Т.к. фильтрация по опубликованности в категориях блюд - отсутствует

	def test_food_list(self):
		response = self.client.get(reverse('food-list'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 1)  # Т.к. по умолчанию кверисет содержит только опубликованные блюда

	def test_is_publish_categories(self):
		response = self.client.get(reverse('foodcategory-list'))
		content = json.loads(response.content)[0]
		food_object = Food.objects.get(id=content['id'])
		self.assertEqual(len(content['foods']), 1)
		self.assertEqual(food_object.is_publish, True)

	def test_is_not_publish_categories(self):
		response = self.client.get(reverse('foodcategory-list'))
		content = json.loads(response.content)[1]
		food_object = Food.objects.get(category=content['id'])
		self.assertEqual(len(content['foods']), 0)
		self.assertEqual(food_object.is_publish, False)

	def test_vegan_filtering(self):
		response = self.client.get('/api/food-filter/', {'is_vegan': False})
		vegan_food = Food.objects.filter(is_vegan=False)
		self.assertEqual(len(response.data), len(vegan_food))

	def test_is_special_filtering(self):
		response = self.client.get('/api/food-filter/', {'is_special': True})
		vegan_food = Food.objects.filter(is_special=True)
		self.assertEqual(len(response.data), len(vegan_food))
