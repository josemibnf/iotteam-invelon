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

class CoffeTypeSaveTestCase(TestCase):
    def setUp(self):
        Department.objects.create(name='terraza') 
        Department.objects.create(name='planta_baja') 
        CoffeType.objects.create(name='cappuccino', current_price=1.5) # Aqui me tiene que crear los dos CoffeStocks.

    def test_coffe_stocks_are_created(self):
        coffe_type = CoffeType.objects.get(name='cappuccino')
        self.assertEqual(CoffeeStock.objects.filter(coffe_type=coffe_type, department=Department.objects.get(name='terraza')).count(), 1)
        self.assertEqual(CoffeeStock.objects.filter(coffe_type=coffe_type, department=Department.objects.get(name='planta_baja')).count(), 1)

class CoffeOrderAreCreatedWithStock0(TestCase):
    def setUp(self):
        CoffeType.objects.create(name='naranjada', current_price=1.2)
        Department.objects.create(name='terraza')
        #Aqui ya me ha creado un CoffeStock.
    
    def test_when_stock_is_created(self):
        coffe_stock = CoffeeStock.objects.get(department=Department.objects.get(name='terraza'))
        self.assertTrue(CoffeeOrder.objects.filter(coffee_stock=coffe_stock, unit_price=1.2, units=100, status='Pending').count()==1)