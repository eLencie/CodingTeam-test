from django.db import models


class Food(models.Model):
	category = models.ForeignKey('FoodCategory', related_name='foods', on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=150)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	is_special = models.BooleanField()
	is_vegan = models.BooleanField()
	is_publish = models.BooleanField()
	toppings = models.ManyToManyField('Topping')

	def __str__(self):
		return self.name


class FoodCategory(models.Model):
	name = models.CharField(max_length=50)
	is_publish = models.BooleanField()

	def __str__(self):
		return self.name


class Topping(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name
