from django.db import models

# Create your models here.

class trait(models.Model):
    objects = models.Manager()
    traits = models.CharField(max_length=50, primary_key=True) # manager can categorize traits of abstract mood

class city(models.Model):
    objects = models.Manager()
    city = models.CharField(max_length=20, primary_key=True) # insert city name

class bookstore(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20) # name of bookstore
    city_address_of_bookstore = models.ForeignKey(city, on_delete=models.CASCADE) # location of bookstore in city scale
    specific_address = models.TextField() # location of bookstore in specific scale
    trait = models.ForeignKey(trait, on_delete=models.CASCADE) # trait of bookstore
    bookstore_information = models.TextField() # summary about bookstore
    
class evaluation_about_bookstore(models.Manager):
    objects = models.Manager()
    evaluation = models.IntegerField(default=0) # about evaluations, mark with number 1 to 5
    comment_about_bookstore_with_text_ = models.TextField() # utility of comments, user can evaluate with text
    #comment_about_bookstore_with_image = models.ImageField(upload_to="image", blank=True) # utility of comments, user can upload image


class informations(models.Model):
    objects = models.Manager()
    bookstore = models.ForeignKey(bookstore, on_delete=models.CASCADE)
    bookstore_image = models.ImageField(upload_to="image", blank=True) # relevant image of bookstore


class bookstore_event(models.Model):
    objects = models.Manager()
    event_name = models.CharField(max_length=20) # name of events
    event_date = models.DateField(auto_now=True) # date of events
    bookstore = models.ForeignKey(bookstore, on_delete=models.CASCADE) # bookstore where it be

    # bookstore_resrvation = models.ForeignKey(user, on_delete = models.SET_NULL, null=True, blank=True) # utility of who resrvate bookstore // it is not work