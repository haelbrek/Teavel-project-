from django.test import TestCase, Client
from home.models import ApiPreferenceModel 
from django.urls import reverse
from django.db.models import QuerySet 

class ApiPreferenceModelTestCase(TestCase):
    def setUp(self):
        ApiPreferenceModel.objects.create(ville="MAD")
        
    def test_Name_ville(self):
        MAD = ApiPreferenceModel.objects.get(ville="MAD")
        self.assertIsInstance(MAD.ville,str)
        
class ApiPreferenceViewsTestCase(TestCase):
        def setUp(self):
             self.client= Client()
             self.list_url=reverse('home')
             
             
        def test_home_page_get(self):
            response = self.client.get(self.list_url)
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'home/home_page.html')
            
            
        def test_home_page_post(self):
            response = self.client.post(
                self.list_url,
                )                     
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'home/result_preference.html')
             
