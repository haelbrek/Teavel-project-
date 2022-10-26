from django import forms
from django.forms import ModelForm
from . import models


class vols(forms.ModelForm):
    class Meta:
        model = models.Vols
        fields = "__all__"
      