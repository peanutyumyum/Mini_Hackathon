from django.shortcuts import render

def location(request):
    return render(request, 'location.html')
