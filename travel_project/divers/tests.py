from django.test import TestCase, Client
from django.urls import reverse, resolve
from divers.views import contact_page, about_page, SignupPage
from django.db.models import QuerySet 


class diversViewsTestCase(TestCase):
        def setUp(self):
            self.client= Client()
            self.contact_url=reverse('contact')
            self.about_url=reverse('about')
            self.signup_url=reverse('signup')
             
        def test_about_page(self):
            self.assertEquals(resolve(self.about_url).func,about_page)
            
        def test_contact_page(self):
            self.assertEquals(resolve(self.contact_url).func,contact_page)

        
        
            
        
             

