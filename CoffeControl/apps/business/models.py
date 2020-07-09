from django.db import models
from django.contrib.auth.models import User
from django.apps import apps

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        super(Department, self).save(*args, **kwargs)
        for coffe_type in 'logistics.CoffeType'.objects.all():
            try:
                coffe_stock = CoffeeStock(department=self, coffe_type=coffe_type)
                coffe_stock.save()
            except AssertionError:
                print('Ya existe un CoffeeStock para ese par Deparament/CoffeType')

class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)