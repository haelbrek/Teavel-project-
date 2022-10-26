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
    
    nombre_adult = models.PositiveIntegerField(
        null=True, 
        blank=True
    )
    nombre_enfant = models.PositiveIntegerField(
        null=True, 
        blank=True
    )
    infant = models.PositiveIntegerField(
        null=True, 
        blank=True
    )