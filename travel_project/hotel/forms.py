from tkinter import Widget
from turtle import textinput
from django import forms
from django.forms import ModelForm, TextInput
from . import models


class hotels(forms.ModelForm):
    class Meta:
        model = models.Hotels
        fields = "__all__"
        widgets = {
              'ville': TextInput(attrs={
                
               
                'placeholder' : 'ex : PAR'
        })
        }