from django.contrib import admin
from .models import bookstore, trait, evaluation_about_bookstore, informations, bookstore_event, city

# Register your models here.

admin.site.register(city)
admin.site.register(bookstore),
admin.site.register(trait),
admin.site.register(informations),
admin.site.register(evaluation_about_bookstore),
admin.site.register(bookstore_event),
