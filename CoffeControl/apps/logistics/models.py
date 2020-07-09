from django.db import models
from django.core.validators import MinValueValidator
from django.apps import apps

# Create your models here.
class CoffeType(models.Model):
    name = models.CharField(max_length=30)
    current_price = models.FloatField(validators=[MinValueValidator(0)])

    def save(self, *args, **kwargs):
        from apps.business.models import Department # el modelo para el save() se importan al llamar al método para no probocar un ciclo.
        
        super(CoffeType, self).save(*args, **kwargs)
        for department in Department.objects.all():
            try:
                CoffeeStock(department=department, coffe_type=self).save()
            except AssertionError:
                print('Ya existe un CoffeeStock para ese par Deparament/CoffeType')

class CoffeeStock(models.Model):
    current_units = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    coffe_type = models.ForeignKey(CoffeType, on_delete=models.CASCADE)
    department = models.ForeignKey('business.Department', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.pk == None: # Es un objeto nuevo.
            assert( CoffeeStock.objects.filter(department=self.department, coffe_type=self.coffe_type).count() == 0 ) # Lanza la excepcion si ya existe ese CoffeStock.
        
        super(CoffeeStock, self).save(*args, **kwargs)
        
        if self.current_units == 0:
            coffe_order = CoffeeOrder(coffee_stock=self, units=100, unit_price=self.coffe_type.current_price)
            coffe_order.save()
        

class CoffeeOrder(models.Model):
    unit_price = models.FloatField(validators=[MinValueValidator(0)])
    units = models.IntegerField(validators=[MinValueValidator(0)])
    status = models.CharField(max_length=8, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted')] , default='Pending')
    coffee_stock = models.ForeignKey(CoffeeStock, on_delete=models.CASCADE)
