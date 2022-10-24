
from django import forms
from django.forms import ModelForm
from . import models


class ApiPreferenceForm(forms.ModelForm):
    class Meta:
        model = models.ApiPreferenceModel
        fields = "__all__"
        # label = {
        #     "ville": "Entrez une ville qui vous plait",
        #     "pays_de_depart": "Choissiez votre pays de départ"
        # }