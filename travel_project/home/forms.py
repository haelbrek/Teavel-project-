
from tkinter import Widget
from turtle import textinput
from django import forms
from django.forms import ModelForm, TextInput
from . import models


class ApiPreferenceForm(forms.ModelForm):
    class Meta:
        model = models.ApiPreferenceModel
        fields = "__all__"
        widgets = {
              'ville': TextInput(attrs={
                
               
                'placeholder' : 'Ville que vous aimez'
        })
        }
   