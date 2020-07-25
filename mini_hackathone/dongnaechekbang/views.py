from django.shortcuts import render
from .models import bookstore, evaluation_about_bookstore, informations
# import model data

# Create your views here.

def location(request):
    bookstore_model = bookstore.objects.all()
    evaluation_about_bookstore_model = evaluation_about_bookstore.objects.all()
    informations_model = informations.objects.all()
    # insert model information to use in location.html

    context = { 'bookstore' : bookstore_model, 'evaluation_about_bookstore' : evaluation_about_bookstore_model, 'informations' : informations_model }
    # declare variable

    
    bookstore_model.city_address_of_bookstore

    return render(request, 'location.html', context)

def location_city_scale(request):
    return render(request, 'location_city_scale.html')

def location_bookstore(request):
    return render(request, 'location_bookstore.html')