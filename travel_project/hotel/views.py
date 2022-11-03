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
                        ratings = form.cleaned_data["etoile"],
                        #amenities = form.cleaned_data["services_equipements"]
               )
               response_hotels = response_hotels.result
               ville_hotel = response_hotels["data"][0]["iataCode"]
               nom_hotel = response_hotels["data"][0]["name"]
               etoile_hotel = response_hotels["data"][0]["rating"]
               hotel_id = response_hotels["data"][0]["hotelId"]
               #services_equipement = response_hotels["data"][0]["amenities"]
               data=response_hotels["data"][0]
               
            #    liste_des_hotels.append(ville_hotel)
            #    liste_des_hotels.append(nom_hotel)
            #    liste_des_hotels.append(etoile_hotel)
            #    liste_des_hotels.append(hotel_id)
            #    liste_des_hotels.append(services_equipements)
    
        else:
            print(form.errors)

        return render (request, 'hotel/reponse_hotel.html', context ={'form':form,"ville_hotel":data})

    elif request.method == "GET":
          form= forms.hotels()
          return render(request, 'hotel/hotel_page.html', context= {"form" :form} )


