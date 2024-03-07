from django.test import TestCase
from restaurant import models
from django.urls import reverse
class Menu(TestCase):
    def test(self):
        item = models.Menu.objects.create(Title="IceCream", Price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")