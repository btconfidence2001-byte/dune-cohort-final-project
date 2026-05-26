from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse

class HomePageTests(TestCase):
    def test_home_page_loads(self):
        # 1. Simulate a user visiting the homepage URL
        response = self.client.get(reverse('marketplace:home'))

        # 2. Check that the website didn't crash (Status 200 means "OK")
        self.assertEqual(response.status_code, 200)
        
        # Check for text we actually know is in view function!
        self.assertContains(response, 'Trusted seller spaces')