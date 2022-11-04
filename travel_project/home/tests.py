from django.test import TestCase, Client
from home.models import ApiPreferenceModel 
from django.urls import reverse , resolve


class ApiPreferenceModelTestCase(TestCase):
    def setUp(self):
        ApiPreferenceModel.objects.create(ville="Paris")
        ApiPreferenceModel.objects.create(pays_de_depart="France")
    
        
    def test_Name_ville(self):
        Paris = ApiPreferenceModel.objects.get(ville="Paris")
        France= ApiPreferenceModel.objects.get(pays_de_depart="France")
        self.assertIsInstance(Paris.ville,str)
        self.assertIsInstance(France.pays_de_depart,str)
        
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
             
