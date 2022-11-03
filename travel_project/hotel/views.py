from django.shortcuts import render
from amadeus import Client, ResponseError, Location
from . import forms
from .forms import hotels
from requests import Session

# Create your views here.

api_keys='enYwMRMTNJzy8AzGgeoCefo6gPusZh7p'
api_secret='EFyhdlYaJgPQKXrM'


def hotel_page(request):
    amadeus= Client(client_id=api_keys,
    client_secret = api_secret)
    liste_des_hotels = []

    if request.method == "POST":

        form = forms.hotels(request.POST)

        if form.is_valid():
               print("le formulaire est valide")
               print( "clean data : ",form.cleaned_data)

               response_hotels = amadeus.reference_data.locations.hotels.by_city.get(
                        cityCode = form.cleaned_data ["ville"],
                        ratings = form.cleaned_data["nombre_etoiles"],
                        amenities = form.cleaned_data["services_equipements"]
               )

               response_hotels = response_hotels.result
               if len(response_hotels["data"]) >=3:
                    for i in range (3):
                        nom_hotel = response_hotels["data"][i]["name"]
                        liste_des_hotels.append(nom_hotel)
               elif len(response_hotels["data"]) == 2:
                    for i in range (2):
                        nom_hotel = response_hotels["data"][i]["name"]
                        liste_des_hotels.append(nom_hotel)
               elif len(response_hotels["data"]) == 1:
                    for i in range (1):
                        nom_hotel = response_hotels["data"][i]["name"]
                        liste_des_hotels.append(nom_hotel)
               elif len(response_hotels["data"]) == 0:
                    print("Il n'y a aucun résultat qui correspond à votre recherche")



    
        else:
            print(form.errors)

        return render (request, 'hotel/reponse_hotel.html', context ={'form':form,'liste_des_hotels':liste_des_hotels})

    elif request.method == "GET":
          form= forms.hotels()
          return render(request, 'hotel/hotel_page.html', context= {"form" :form} )


