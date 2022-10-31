
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from amadeus import Client, ResponseError, Location
from . import forms
from .forms import vols
from requests import Session

from dotenv import load_dotenv 
load_dotenv()
import os 

api_keys = os.getenv("api_keys")
api_secret=os.getenv("api_secret")



@login_required
def vol_page(request):
     amadeus = Client(client_id=api_keys,
     client_secret = api_secret)
     liste_des_billets=[]
     
     if request.method == "POST":
          
          form = forms.vols(request.POST)

          if form.is_valid():
               print("le formulaire est valid")
               print( "clean data : ",form.cleaned_data)

               response = amadeus.shopping.flight_offers_search.get(
                         originLocationCode=form.cleaned_data["depart"],
                         destinationLocationCode=form.cleaned_data["destination"],
                         departureDate=form.cleaned_data["date_depart"],
                         returnDate=form.cleaned_data["date_arrive"],
                         adults=form.cleaned_data["nombre_adult"],
                         children=form.cleaned_data["nombre_enfant"],
                         infants=form.cleaned_data['infant'],
                         )


               response = response.result

              
               

               info_depart_aller = response["data"][0]["itineraries"][0]["segments"][0]["departure"]
               
               info_arrivee_aller = response["data"][0]["itineraries"][0]["segments"][0]["arrival"]

               info_depart_retour = response["data"][0]["itineraries"][1]["segments"][0]["departure"]

               info_arrivee_retour = response["data"][0]["itineraries"][1]["segments"][0]["arrival"]

               prix_billets = response["data"][0]["price"]["total"]

               compagnies_vols = response["data"][0]["itineraries"][0]["segments"][0]["carrierCode"]
               
               dico_compagnies = response["dictionaries"]["carriers"]

               heures_de_vol = response["data"][0]["itineraries"][0]["segments"][0]["duration"]

               liste_des_billets=[info_depart_aller,info_arrivee_aller,info_depart_retour,info_arrivee_retour,prix_billets,compagnies_vols,heures_de_vol]
               print(liste_des_billets)
          else:
               print("un truc")
               print(form.errors)
               print("error")
                    
          return render (request, 'vol/reponse_vol.html', context ={
                                                                    'form':form, 
                                                                    'liste_des_billets' : liste_des_billets
                                                                    }
                         
                                                           )
       
     elif request.method == "GET":
          form= forms.vols()
          return render(request, 'vol/vol_page.html', context= {"form" :form} )


