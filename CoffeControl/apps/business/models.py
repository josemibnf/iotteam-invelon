from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        from apps.logistics.models import CoffeType, CoffeeStock # el modelo para el save() se importan al llamar al método para no probocar un ciclo.
        
        super(Department, self).save(*args, **kwargs)
        for coffe_type in CoffeType.objects.all():
            try:
                CoffeeStock(department=self, coffe_type=coffe_type).save()
            except AssertionError:
                print('Ya existe un CoffeeStock para ese par Deparament/CoffeType')

class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)