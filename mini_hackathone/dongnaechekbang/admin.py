from django.contrib import admin
from .models import bookstore, trait, evaluation_about_bookstore, informations, bookstore_event

# Register your models here.

admin.site.register(bookstore),
admin.site.register(trait),
# admin.site.register(evaluation_about_bookstore), 오류코드
admin.site.register(informations),
admin.site.register(bookstore_event),