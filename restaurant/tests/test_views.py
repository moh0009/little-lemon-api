from django.test import TestCase
from django.urls import reverse
from restaurant.serializers import MenuSerializer
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of the Menu model
        Menu.objects.create(Title="IceCream", Price=80, inventory=100)

    def test_getall(self):
        # Retrieve all Menu objects
        menu_objects = Menu.objects.all()
        
        # Serialize the data
        serializer = MenuSerializer(menu_objects, many=True)
        expected_data = serializer.data
        
        # Make a request to the view
        url = reverse('menu')  
        response = self.client.get(url)
        
        # Compare serialized data with response data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)
