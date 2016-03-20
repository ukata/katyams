from django.test import TestCase
from django.test import Client
# Create your tests here.



class MainMenuTest(TestCase):
    """Test cases for the menu links.
    """
    def setUp(self):
        """Prepare environment for the tests.
        """
        self.client = Client()

    def test_contact(self):
        """Test the contact page link.
        """
        response = self.client.get('/contact/')
        self.assertContains(response, "contact")

class FooterTest(TestCase):
    """Test cases for the footer.
    """
    
    def setUp(self):
        """Prepare environment for the tests.
        """
        self.client = Client()
        
    def test_footer(self):
        """Test the footer.
        """
        response = self.client.get('/contact/')
        self.assertContains(response, "Katia Zawadzka 2016")

class ContactPageTest(TestCase):
    """Test cases for the menu links.
    """
    def setUp(self):
        """Prepare environment for the tests.
        """
        self.client = Client()

    def test_contact(self):
        """Test the contact page link.
        """
        response = self.client.get('/contact/')
        self.assertContains(response, "Katia Zawadzka")
        
    def test_piwik(self):
        """Test the contact page wpik link.
        """
        response = self.client.get('/contact/')
        self.assertContains(response, "piwik")    