from django.db import models

# Create your models here.
class ApiPreferenceModel(models.Model):

    ville = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )   
    #FRANCE= 'FR'
    #ARGENTINE = 'AR'
    #UNITED_KINGDOM = "UK"
    # ITALIE = 'IT'
    # ETATS_UNIS = 'USA'
    # PAYS_DE_DEPART = [
    #     (FRANCE, 'France'),
    #     (ARGENTINE, 'Argentine'),
    #     (UNITED_KINGDOM, 'Royaume-Uni'),
    #     (ITALIE, 'Italie'),
    #     (ETATS_UNIS, 'Etats-Unis'),
    #]
    pays_de_depart = models.CharField(
        max_length=3,
        blank= False
    )

    