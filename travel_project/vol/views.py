
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
     liste_info_depart_aller_aeroport=[]
     
     liste_info_depart_aller_date=[]
     liste_info_arrivee_aller_aeroport=[]
     liste_info_arrivee_aller_date=[]
     liste_info_depart_retour_aeroport=[]
     
     liste_info_depart_retour_date=[]
     liste_info_arrivee_retour_aeroport=[]
     liste_info_arrivee_retour_date=[]
     liste_prix_billets=[]
     liste_compagnies_vols_aller=[]
     liste_compagnies_vols_retour=[]
     liste_heures_de_vol_aller=[]
     liste_heures_de_vol_retour=[]
     liste_Escale_aller=[]
     liste_Escale_retour=[]
     liste_nom_de_la_compagnie_aller=[]
     liste_nom_de_la_compagnie_retour=[]
     
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

               print(response["data"][0])

              
               for i in range(3):

                    info_depart_aller_aeroport = response["data"][i]["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                    liste_info_depart_aller_aeroport.append(info_depart_aller_aeroport)


                    info_depart_aller_date = response["data"][i]["itineraries"][0]["segments"][0]["departure"]["at"]
                    liste_info_depart_aller_date.append(info_depart_aller_date)

                    info_arrivee_aller_aeroport = response["data"][i]["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
                    liste_info_arrivee_aller_aeroport.append(info_arrivee_aller_aeroport)

                    info_arrivee_aller_date = response["data"][i]["itineraries"][0]["segments"][0]["arrival"]["at"]
                    liste_info_arrivee_aller_date.append(info_arrivee_aller_date)


                    info_depart_retour_aeroport = response["data"][i]["itineraries"][1]["segments"][0]["departure"]["iataCode"]
                    liste_info_depart_retour_aeroport.append(info_depart_retour_aeroport)
                   

                    
                    info_depart_retour_date = response["data"][i]["itineraries"][1]["segments"][0]["departure"]["at"]
                    liste_info_depart_retour_date.append(info_depart_retour_date)

                    
                    info_arrivee_retour_aeroport = response["data"][i]["itineraries"][1]["segments"][0]["arrival"]["iataCode"]
                    liste_info_arrivee_retour_aeroport.append(info_arrivee_retour_aeroport)
                    
                    info_arrivee_retour_date = response["data"][i]["itineraries"][1]["segments"][0]["arrival"]["at"]
                    liste_info_arrivee_retour_date.append(info_arrivee_retour_date)

                    prix_billets = response["data"][i]["price"]["total"]
                    liste_prix_billets.append(prix_billets)

                    compagnies_vols_aller = response["data"][i]["itineraries"][0]["segments"][0]["carrierCode"]
                    liste_compagnies_vols_aller.append(compagnies_vols_aller)

                    compagnies_vols_retour = response["data"][i]["itineraries"][1]["segments"][0]["carrierCode"]
                    liste_compagnies_vols_retour.append(compagnies_vols_retour)

                    

                    Escale_aller = response["data"][i]["itineraries"][0]["segments"][0]["numberOfStops"]
                    liste_Escale_aller.append(Escale_aller)

                    Escale_retour = response["data"][i]["itineraries"][1]["segments"][0]["numberOfStops"]
                    liste_Escale_retour.append(Escale_retour)

                    heures_de_vol_aller = response["data"][i]["itineraries"][0]["segments"][0]["duration"]
                    liste_heures_de_vol_aller.append(heures_de_vol_aller)

                    heures_de_vol_retour = response["data"][i]["itineraries"][1]["segments"][0]["duration"]
                    liste_heures_de_vol_retour.append(heures_de_vol_retour)


                    dico_compagnies = response["dictionaries"]["carriers"]

                    nom_de_la_compagnie_aller=""
                    nom_de_la_compagnie_retour=""
                    for key, value in dico_compagnies.items():
                         if compagnies_vols_aller == key:
                               nom_de_la_compagnie_aller = value
                    liste_nom_de_la_compagnie_aller.append(nom_de_la_compagnie_aller)
                    for key, value in dico_compagnies.items():
                         if compagnies_vols_retour == key:
                               nom_de_la_compagnie_retour = value
                    liste_nom_de_la_compagnie_retour.append(nom_de_la_compagnie_retour)
               # liste_des_billets=[info_depart_aller,info_arrivee_aller,info_depart_retour,info_arrivee_retour,prix_billets,compagnies_vols,heures_de_vol]
               # print(liste_des_billets)

               liste_offre_1=[   liste_info_depart_aller_aeroport[0],
                   
                    liste_info_depart_aller_date[0],
                    liste_info_arrivee_aller_aeroport[0],
                    liste_info_arrivee_aller_date[0],
                    liste_info_depart_retour_aeroport[0],
                    liste_info_depart_retour_date[0],
                    liste_info_arrivee_retour_aeroport[0],
                    liste_info_arrivee_retour_date[0],
                    liste_prix_billets[0],
                    liste_heures_de_vol_aller[0],
                    liste_heures_de_vol_retour[0],
                    liste_Escale_aller[0],
                    liste_Escale_retour[0],
                    liste_nom_de_la_compagnie_aller[0],
                    liste_nom_de_la_compagnie_retour[0],]


               liste_offre_2=[   liste_info_depart_aller_aeroport[1],
                    
                    liste_info_depart_aller_date[1],
                    liste_info_arrivee_aller_aeroport[1],
                    liste_info_arrivee_aller_date[1],
                    liste_info_depart_retour_aeroport[1],
                    
                    liste_info_depart_retour_date[1],
                    liste_info_arrivee_retour_aeroport[1],
                    liste_info_arrivee_retour_date[1],
                    liste_prix_billets[1],
                    liste_heures_de_vol_aller[1],
                    liste_heures_de_vol_retour[1],
                    liste_Escale_aller[1],
                    liste_Escale_retour[1],
                    liste_nom_de_la_compagnie_aller[1],
                    liste_nom_de_la_compagnie_retour[1],]

               liste_offre_3=[   liste_info_depart_aller_aeroport[2],
                    
                    liste_info_depart_aller_date[2],
                    liste_info_arrivee_aller_aeroport[2],
                    liste_info_arrivee_aller_date[2],
                    liste_info_depart_retour_aeroport[2],
                    
                    liste_info_depart_retour_date[2],
                    liste_info_arrivee_retour_aeroport[2],
                    liste_info_arrivee_retour_date[2],
                    liste_prix_billets[2],
                    liste_heures_de_vol_aller[2],
                    liste_heures_de_vol_retour[2],
                    liste_Escale_aller[2],
                    liste_Escale_retour[2],
                    liste_nom_de_la_compagnie_aller[2],
                    liste_nom_de_la_compagnie_retour[2]]
               
               context = {"billet_1":liste_offre_1, "billet_2":liste_offre_2,"billet_3":liste_offre_3}    
          else:
               print("un truc")
               print(form.errors)

                    
          return render (request, 'vol/reponse_vol.html', context =context)
       
     elif request.method == "GET":
          form= forms.vols()
          return render(request, 'vol/vol_page.html', context= {"form" :form} )


