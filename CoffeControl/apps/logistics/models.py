from django.db import models
from django.core.validators import MinValueValidator
from django.apps import apps

# Create your models here.
class CoffeType(models.Model):
    name = models.CharField(max_length=30)
    current_price = models.FloatField(validators=[MinValueValidator(0)])

class CoffeeStock(models.Model):
    current_units = models.IntegerField(validators=[MinValueValidator(0)])
    coffe_type = models.ForeignKey(CoffeType, on_delete=models.CASCADE)
    department = models.ForeignKey('business.Department', on_delete=models.CASCADE)

class CoffeeOrder(models.Model):
    unit_price = models.FloatField(validators=[MinValueValidator(0)])
    units = models.IntegerField(validators=[MinValueValidator(0)])
    status = models.CharField(max_length=8, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted')] , default='Pending')
    coffee_stock = models.ForeignKey(CoffeeStock, on_delete=models.CASCADE)
