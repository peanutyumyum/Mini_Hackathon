from django.shortcuts import render
from .models import Bookstore, Evaluation_about_bookstore, Informations, City
# import model data

# Create your views here.

def location(request):
    bookstore_model = Bookstore.objects.all()
    evaluation_about_bookstore_model = Evaluation_about_bookstore.objects.all()
    informations_model = Informations.objects.all()
    city_model = City.objects.all()
    # insert model information to use in location.html

    city_name = bookstore_model.filter(city_address_of_bookstore='을지로')
    # to list city address of bookstore

    context = {
        'bookstore' : bookstore_model, 
        'evaluation_about_bookstore' : evaluation_about_bookstore_model, 
        'informations' : informations_model, 
        'city' : city_model, 
        'city_name' : city_name, 
    }
    # declare variable
    

    return render(request, 'location.html', context)

def location_city_scale(request, city_id):
    return render(request, 'location_city_scale.html')

def location_bookstore(request):
    return render(request, 'location_bookstore.html')