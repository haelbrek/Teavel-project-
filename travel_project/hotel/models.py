from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Hotels(models.Model):

    ville = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    SWIMMING_POOL= 'SWIMMING_POOL'
    SPA = 'SPA'
    RESTAURANT = "RESTAURANT"
    PETS_ALLOWED = 'PETS_ALLOWED'
    BEACH = 'BEACH'
    FITNESS_CENTER = 'FITNESS_CENTER'
    AIRPORT_SHUTTLE = 'AIRPORT_SHUTTLE'
    MASSAGE = ' MASSAGE'
    BAR_LOUNGE = 'BAR or LOUNGE'
    ROOM_SERVICE = 'ROOM_SERVICE'
    SERVICES = [
        (SWIMMING_POOL, 'Piscine'),
        (SPA, 'SPA'),
        (RESTAURANT, 'Restaurant'),
        (PETS_ALLOWED, 'Animaux autorisés'),
        (BEACH, 'Plage'),
        (FITNESS_CENTER, 'Salle de sport'),
        (AIRPORT_SHUTTLE, 'navette aéroport'),
        (MASSAGE, 'Massage'),
        (BAR_LOUNGE, 'Bar'),
        (ROOM_SERVICE, 'Room Service')
    ]
    services_equipements = models.CharField(
        max_length=150,
        blank= False,
        null= True,
        choices= SERVICES,
        
    )

    ETOILE_1= '1'
    ETOILE_2 = '2'
    ETOILE_3 = "3"
    ETOILE_4 = '4'
    ETOILE_5 = '5'
    SERVICES = [
        (ETOILE_1, '1'),
        (ETOILE_2, '2'),
        (ETOILE_3, '3'),
        (ETOILE_4, '4'),
        (ETOILE_5, '5'),

    ]
    nombre_etoiles = models.CharField(
        max_length=150,
        blank= False,
        null= True,
        choices= SERVICES,
        
    )

    
