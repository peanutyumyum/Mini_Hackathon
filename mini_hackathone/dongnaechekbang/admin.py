from django.contrib import admin
from .models import Bookstore, Trait, Evaluation_about_bookstore, Informations, Bookstore_event, Blog, Comment
# Register your models here.

admin.site.register(Blog),
admin.site.register(Comment),
admin.site.register(Trait),
admin.site.register(Bookstore),
admin.site.register(Informations),
admin.site.register(Evaluation_about_bookstore),
admin.site.register(Bookstore_event),