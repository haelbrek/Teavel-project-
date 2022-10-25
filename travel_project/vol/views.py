
from django.shortcuts import render
from amadeus import Client, ResponseError, Location
from . import forms
from .forms import vols
from requests import Session

# Create your views here
api_keys = "JwBcoLzEegwwTjRDAypurrSvQYQBtEhk"
api_secret="GWuM8LybWntkcEnu"




def vol_page(request):
     amadeus = Client(client_id=api_keys,
     client_secret = api_secret)
     liste_des_billets = []
     
     if request.method == "POST":
          
          form = forms.vols(request.POST)

          if form.is_valid():
               print("le formulaire est valid")
               print( "clean data : ",form.cleaned_data)

               response = amadeus.shopping.flight_offers_search.get(
                         originLocationCode=form.cleaned_data["depart"],
                         destinationLocationCode=form.cleaned_data["destination"],
                         departureDate=form.cleaned_data["date_depart"],
                         returnDate= form.cleaned_data["date_arrive"],
                         adults = form.cleaned_data["classe_vol"],
                         children =form.cleaned_data["nombre_enfant"],
                         infants = form.cleaned_data["infant"]
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

               nom_de_la_compagnie = ""

               billets_aller = [info_depart_aller, info_arrivee_aller]
               billets_retour = [info_depart_retour, info_arrivee_retour]


               for key, value in dico_compagnies.items():
                    if compagnies_vols == key:
                         nom_de_la_compagnie = value

               


               liste_des_billets.append(billets_aller)
               liste_des_billets.append(billets_retour)
               liste_des_billets.append(heures_de_vol)
               liste_des_billets.append(prix_billets)
               #    liste_des_billets.append(compagnies_vols)
               liste_des_billets.append(nom_de_la_compagnie)


          else:
               print("un truc")
               print(form.errors)

                    
          return render (request, 'vol/reponse_vol.html', context ={'form':form, 'liste_des_billetins' : liste_des_billets})
       
     elif request.method == "GET":
          form= forms.vols()
          return render(request, 'vol/vol_page.html', context= {"form" :form} )


