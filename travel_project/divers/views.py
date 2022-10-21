from django.shortcuts import render

def contact_page(request):
    return render(request, "divers/contact_page.html")

def about_page(request):
    return render(request, "divers/about.html")
