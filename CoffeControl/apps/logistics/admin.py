from django.contrib import admin
from .models import CoffeType, CoffeeStock, CoffeeOrder

# Register your models here.
admin.site.register(CoffeType)
admin.site.register(CoffeeStock)
admin.site.register(CoffeeOrder)