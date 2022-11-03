from django.test import TestCase, Client
from hotel.models import Hotels
from django.urls import reverse
from django.db.models import QuerySet 

class HotelModelTestCase(TestCase):
    def setUp(self):
        self.cara_hotel=Hotels.objects.create(ville="MAD",etoile=4,services_equipements="SWIMMING_POOL")
    def test_ville(self):
        self.cara_hotel=Hotels.objects.get(ville="MAD",etoile=4,services_equipements="SWIMMING_POOL")
        self.assertIsInstance(self.cara_hotel.ville,str)
        self.assertIsInstance(self.cara_hotel.etoile,int)
        self.assertIsInstance(self.cara_hotel.services_equipements,str)
class ApiPreferenceViewsTestCase(TestCase):
        def setUp(self):
             self.client= Client()
             self.list_url=reverse('hotel')
             
             
        def test_hotel_page_get(self):
        
            response = self.client.get(self.list_url)
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'hotel/hotel_page.html')
            
            
        def test_hotel_page_post(self):
            # category.objects.create(
            #     project=self.project1,
            #     name='development'
            #     )
        
            response = self.client.post(
                self.list_url,
                )                     
            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'hotel/reponse_hotel.html')
             
