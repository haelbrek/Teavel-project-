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
                        ratings = form.cleaned_data["nombre d'etoiles"],
                        amenities = form.cleaned_data["services et equipements"]
               )


