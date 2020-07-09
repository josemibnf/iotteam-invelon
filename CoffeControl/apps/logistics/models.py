from django.db import models
from django.core.validators import MinValueValidator
from django.apps import apps

# Create your models here.
class CoffeType(models.Model):
    name = models.CharField(max_length=30)
    current_price = models.FloatField(validators=[MinValueValidator(0)])

    def save(self, *args, **kwargs):
        super(CoffeType, self).save(*args, **kwargs)
        for department in 'business.Department'.objects.all():
            try:
                coffe_stock = CoffeeStock(department=department, coffe_type=self)
                coffe_stock.save()
            except AssertionError:
                print('Ya existe un CoffeeStock para ese par Deparament/CoffeType')

class CoffeeStock(models.Model):
    current_units = models.IntegerField(validators=[MinValueValidator(0)])
    coffe_type = models.ForeignKey(CoffeType, on_delete=models.CASCADE)
    department = models.ForeignKey('business.Department', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.pk == None: # Solo si es un objeto nuevo.
            assert(  )
        super(CoffeeStock, self).save(*args, **kwargs)
        

class CoffeeOrder(models.Model):
    unit_price = models.FloatField(validators=[MinValueValidator(0)])
    units = models.IntegerField(validators=[MinValueValidator(0)])
    status = models.CharField(max_length=8, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted')] , default='Pending')
    coffee_stock = models.ForeignKey(CoffeeStock, on_delete=models.CASCADE)
