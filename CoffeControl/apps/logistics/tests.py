from django.test import TestCase
from apps.logistics.models import *
from apps.business.models import Department

# Create your tests here.
class CoffeStockAssertionErrorTestCase(TestCase):
    def setUp(self):
        Department.objects.create(name='planta_baja')
        CoffeType.objects.create(name='naranjada', current_price='0.15')
        # Ya se ha creado un CoffeStock de ambos.
    
    def test_coffe_stock_assertion_error(self):
        department = Department.objects.get(name='planta_baja')
        coffe_type = CoffeType.objects.get(name='naranjada')
        with self.assertRaises(AssertionError) as e:
            CoffeeStock.objects.create(department=department, coffe_type=coffe_type)
        self.assertTrue('Ya existe un CoffeeStock para ese par Deparament/CoffeType' in str(e.exception))