from django.urls import path
from . import views 

urlpatterns = [
    path ( '', views.hotel_page, name="hotel")
]