from django.test import TestCase
from apps.business.models import Department
from apps.logistics.models import CoffeType, CoffeeStock

# Create your tests here.
class DepartmentSaveTestCase(TestCase):
    def setUp(self):
        CoffeType.objects.create(name='frappuccino', current_price=4.0)
        CoffeType.objects.create(name='cappuccino', current_price=1.5)
        Department.objects.create(name='planta_baja')
    
    def test_coffe_stocks_are_created(self):
        department = Department.objects.get(name='planta_baja')
        self.assertEqual(CoffeeStock.objects.filter(coffe_type=CoffeType.objects.get(name='cappuccino'), department=department).count(), 1)
        self.assertEqual(CoffeeStock.objects.filter(coffe_type=CoffeType.objects.get(name='frappuccino'), department=department).count(), 1)