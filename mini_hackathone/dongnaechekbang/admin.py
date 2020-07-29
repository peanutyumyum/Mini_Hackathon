from django.contrib import admin
from .models import bookstore, trait, city



admin.site.register(city)
admin.site.register(bookstore)
admin.site.register(trait)
