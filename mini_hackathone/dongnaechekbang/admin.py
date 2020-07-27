from django.contrib import admin
from .models import Bookstore, Trait, Evaluation_about_bookstore, Informations, Bookstore_event, City

# Register your models here.

admin.site.register(City)
admin.site.register(Bookstore),
admin.site.register(Trait),
admin.site.register(Informations),
admin.site.register(Evaluation_about_bookstore),
admin.site.register(Bookstore_event),
