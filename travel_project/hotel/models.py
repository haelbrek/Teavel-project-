from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Hotels(models.Model):

    ville = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    etoile=models.PositiveIntegerField(
        null=True, 
        blank=True
    )
    
    # List_service = ["SWIMMING_POOL", "SPA", "FITNESS_CENTER", "AIR_CONDITIONING", "RESTAURANT", "PARKING", "PETS_ALLOWED", "AIRPORT_SHUTTLE", "BUSINESS_CENTER", "DISABLED_FACILITIES", "WIFI", "MEETING_ROOMS", "NO_KID_ALLOWED", "TENNIS", "GOLF", "KITCHEN", "ANIMAL_WATCHING", "BABY-SITTING", "BEACH", "CASINO", "JACUZZI", "SAUNA", "SOLARIUM", "MASSAGE", "VALET_PARKING", "BAR", "LOUNGE", "KIDS_WELCOME", "NO_PORN_FILMS", "MINIBAR", "TELEVISION","WI-FI_IN_ROOM", "ROOM_SERVICE", "GUARDED_PARKG", "SERV_SPEC_MENU"
    # ]
    services_equipements = models.CharField(
        max_length=100,
        blank= False,
        # choices= List_service,
        # default = "SWIMMING_POOL"
    )