from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from . import forms
def contact_page(request):
    return render(request, "divers/contact_page.html")

def about_page(request):
    return render(request, "divers/about.html")

class SignupPage(CreateView):

    form_class= forms.UserCreationFormCustom
    success_url= reverse_lazy('login')
    template_name= 'registration/signup.html'
    