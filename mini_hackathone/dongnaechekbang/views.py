from django.shortcuts import render
from django.db.models import Q
from .models import bookstore, city, trait

def search(request):
    return render (request, 'search.html')

def result(request):
    bookstoreinfo = bookstore.objects.all()
    query = request.GET.get('query','')
    if query:
        bookstoreinfo = bookstoreinfo.filter(Q(name__icontains=query)|Q(city_address_of_bookstore__icontains=query)|Q(trait__icontains=query)|Q(bookstore_information__icontains=query)).order_by('-time')

    return render(request,'result.html',{'bookstoreinfo':bookstoreinfo,'query':query})
# Create your views here.
