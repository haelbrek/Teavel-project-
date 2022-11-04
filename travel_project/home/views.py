from django.shortcuts import render
from amadeus import Client, ResponseError, Location
from . import forms
from .forms import ApiPreferenceForm
from requests import Session

from dotenv import load_dotenv 
load_dotenv()
import os 

api_keys = os.getenv("api_keys")
api_secret=os.getenv("api_secret")


def home_page(request):
     amadeus = Client(client_id=api_keys,
     client_secret = api_secret)
     liste_des_villes = []
     liste_des_iata =[]
     session = Session()

     
     
     if request.method == "POST":
          
          form = forms.ApiPreferenceForm(request.POST)

          if form.is_valid():
               print("le formulaire est valid")
               print( "clean data : ",form.cleaned_data)


               preference = amadeus.reference_data.recommended_locations.get(cityCodes = form.cleaned_data["ville"], travelerCountryCode = form.cleaned_data["pays_de_depart"])
               print(form.cleaned_data)
               preference = preference.result
               
               for i in range(5):

                    nom_de_ville = preference["data"][i]["name"]
                    liste_des_villes.append(nom_de_ville)
                    code_iata = preference["data"][i]["iataCode"]
                    liste_des_iata.append(code_iata)
               # session["liste_des_iata"] = liste_des_iata

          else:
               #print("un truc")
               print(form.errors)

                    
          return render (request, 'home/result_preference.html', context ={'form':form, 'liste_des_villes' : liste_des_villes})
       
     elif request.method == "GET":
          form= forms.ApiPreferenceForm()
          return render(request, 'home/home_page.html', context= {"form"    :form} )


