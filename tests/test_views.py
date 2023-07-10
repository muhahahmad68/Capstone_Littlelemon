from django.test import TestCase
from restaurant.models import Menu 
from restaurant.serializers import MenuSerializer 

class MenuTestView(TestCase):

    @classmethod
    def setUp(cls):
        cls.item = Menu.objects.create(title='Ice cream', price=6.50, inventory=50)

    def test_getall(self):
        self.assertEqual(self.item, "Ice cream: 6.5")
        # return 