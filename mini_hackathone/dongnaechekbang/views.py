from django.shortcuts import render
from .models import Bookstore, Evaluation_about_bookstore, Informations
from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
# import model data

# Create your views here.

def location(request):
    bookstore_model = Bookstore.objects.all()
    evaluation_about_bookstore_model = Evaluation_about_bookstore.objects.all()
    informations_model = Informations.objects.all()
    # insert model information to use in location.html

    context = {
        'bookstore' : bookstore_model, 
        'evaluation_about_bookstore' : evaluation_about_bookstore_model, 
        'informations' : informations_model, 
    }
    # declare variable
    
    return render(request, 'location.html', context)

def location_bookstore(request, bookstore_id):

    bookstore = get_object_or_404(Bookstore, pk=bookstore_id)
    bookstore_model = Bookstore.objects.all()
    # insert model information to use in location_bookstore.html

    """ city_address_of_bookstore_을지로_model = bookstore_model.filter(city_address_of_bookstore='을지로')
    city_address_of_bookstore_망원동_model = bookstore_model.filter(city_address_of_bookstore='망원동')
    # to list city address of bookstore """
    # 사용 안합니다

    context = {
        'bookstores' : bookstore, 
        'bookstore' : bookstore_model
    }
    # declare variable

    return render(request, 'location_bookstore.html', context)