from django.shortcuts import render
from django.db.models import Q
from .models import bookstore, city, trait

def search(request):
    return render (request, 'search.html')

def result(request):
    bookstoreinfo = bookstore.objects.all()
    query = request.GET.get('query','') 
    search_type = request.GET.get('type','')
    if query:
        if search_type == 'all':
            bookstoreinfo = bookstoreinfo.filter(Q(name__icontains=query)| Q(city_address_of_bookstore__city__icontains=query) | Q(trait__traits__icontains=query)|Q(bookstore_information__icontains=query))
        elif search_type == 'name':
            bookstoreinfo = bookstoreinfo.filter(name__icontains=query)
        elif search_type == 'city':
            bookstoreinfo = bookstoreinfo.filter(city_address_of_bookstore__city__icontains=query)
        elif search_type == 'trait':
            bookstoreinfo = bookstoreinfo.filter(trait__traits__icontains=query)
        elif search_type == 'info':
            bookstoreinfo = bookstoreinfo.filter(bookstore_information__icontains=query)
    return render(request, 'result.html',{'bookstoreinfo':bookstoreinfo , 'query':query,})
