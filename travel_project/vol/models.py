from django.db import models


# Create your models here.
class Vols(models.Model):

    depart = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )   
    destination = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )  
    date_depart = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )  
    date_arrive = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )  
    
    classe_vol = models.CharField(
        max_length=3,
        blank= False
    )

    