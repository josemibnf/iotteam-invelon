from django.contrib import admin
from .models import CoffeType, CoffeStock, CoffeOrder

# Register your models here.
admin.site.register(CoffeType)
admin.site.register(CoffeStock)
admin.site.register(CoffeOrder)