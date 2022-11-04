from email.policy import default
from random import choice, choices
from django.db import models

# Create your models here.
class ApiPreferenceModel(models.Model):

    ville = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )   
    FRANCE= 'FR'
    ARGENTINE = 'AR'
    UNITED_KINGDOM = "GB"
    ITALIE = 'IT'
    ETATS_UNIS = 'US'
    ALLEMAGNE = 'DE'
    SPAIN = 'ES'
    PAYS_BAS = 'NL'
    MEXIQUE = 'MX'
    ARABIE_SAOUDITE = 'SA'
    PAYS_DE_DEPART = [
        (FRANCE, 'France'),
        (ARGENTINE, 'Argentine'),
        (UNITED_KINGDOM, 'Royaume-Uni'),
        (ITALIE, 'Italie'),
        (ETATS_UNIS, 'Etats-Unis'),
        (ALLEMAGNE, 'Allemagne'),
        (SPAIN, 'Espagne'),
        (PAYS_BAS, 'Pays-bas'),
        (MEXIQUE, 'Mexique'),
        (ARABIE_SAOUDITE, 'Arabie saoudite')
    ]
    pays_de_depart = models.CharField(
        max_length=3,
        blank= False,
        null= True,
        choices= PAYS_DE_DEPART,
        default = FRANCE
        
    )

    