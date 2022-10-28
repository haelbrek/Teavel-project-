from django.db import models

# Create your models here.
class Hotels(models.Model):

    ville = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    UN = "1"
    DEUX = "2"
    TROIS = "3"
    QUATRE = "4"
    CINQ = "5"

    NOMBRE_ETOILES = [
        (UN,"1"),
        (DEUX,"2"),
        (TROIS,"3"),
        (QUATRE,"4"),
        (CINQ,"5")
    ]
    nombre_etoiles = models.CharField(
        max_length = 100,
        blank=True,
        null=True,
        choices = NOMBRE_ETOILES


    )

    PISCINE = "SWIMMING_POOL"
    SPA = "SPA"
    SALLE_DE_FITNESS = "FITNESS_CENTER"
    AIR_CONDITIONNE = "AIR_CONDITIONING"
    RESTAURANT = "RESTAURANT"
    PARKING = "PARKING"
    ANIMAUX_ACCEPTE = "PETS_ALLOWED"
    NAVETTE_AEROPORT = "AIRPORT_SHUTTLE"
    FACILITES_POUR_HANDICAPES = "DISABLED_FACILITIES"
    WIFI = "WIFI"
    SALLES_DE_REUNIONS = "MEETING_ROOMS"
    TENNIS = "TENNIS"
    GOLF ="GOLF"
    CUISINE = "KITCHEN"
    PLAGE = "BEACH"
    CASINO = "CASINO"
    JACUZZI = "JACUZZI"
    SAUNA = "SAUNA"
    SOLARIUM = "SOLARIUM"
    MASSAGE = "MASSAGE"
    VOITURIER = "VALET_PARKING"
    MINIBAR = "MINIBAR"
    TELEVISION = "TELEVISION"
    SERVICE_DE_CHAMBRE = "ROOM_SERVICE"
    PARKING_SURVEILLE = "GUARDED_PARKG"

    SERVICES_ET_EQUIPEMENTS = [

        (PISCINE,"Piscine"),
        (SPA,"SPA"),
        (SALLE_DE_FITNESS,"Salle de fitness"),
        (AIR_CONDITIONNE,"Air conditionné"),
        (RESTAURANT,"Restaurant"),
        (PARKING,"Parking"),
        (ANIMAUX_ACCEPTE,"Animaux accepté"),
        (NAVETTE_AEROPORT,"Navette aéroport"),
        (FACILITES_POUR_HANDICAPES,"Facilités pour handicapés"),
        (WIFI,"Wifi"),
        (SALLES_DE_REUNIONS,"Salles de réunions"),
        (TENNIS,"Tennis"),
        (GOLF,"Golf"),
        (CUISINE,"Cuisine"),
        (SOLARIUM,"Solarium"),
        (MASSAGE,"Massage"),
        (VOITURIER,"Voiturier"),
        (MINIBAR,"Mini Bar"),
        (TELEVISION,"Télévision"),
        (SERVICE_DE_CHAMBRE,"Service de chambre"),
        (PARKING_SURVEILLE,"Parking surveillé")



        
    ]


    services_et_equipements = models.CharField(
        max_length=100,
        blank=True,
        choices = SERVICES_ET_EQUIPEMENTS,

    )