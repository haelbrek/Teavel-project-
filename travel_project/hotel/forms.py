from django import forms
from django.forms import ModelForm
from . import models


class hotels(forms.ModelForm):
    class Meta:
        model = models.Hotels
        fields = "__all__"