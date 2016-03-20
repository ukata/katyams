from django.test import TestCase
from django.test import Client
# Create your tests here.



class MainMenuTest(TestCase):
    """Test cases for the menu links.
    """
    def setUp(self):
        self.client = Client()

    def test_contact(self):
        response = self.client.get('/contact/')
        self.assertContains(response, "contact")

class FooterTest(TestCase):
    """Test cases for the footer.
    """
    
    def setUp(self):
        self.client = Client()
        
    def test_footer(self):
        response = self.client.get('/contact/')
        self.assertContains(response, "Katia Zawadzka 2016")
    