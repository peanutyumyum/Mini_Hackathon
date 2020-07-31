from django.utils import timezone
from django.db import models
from django.conf import settings

# Create your models here.

class Blog(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=2000)
    author = models.CharField(max_length=100)
    time = models.DateTimeField(default=timezone.now)
    hit = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title

    @property
    def update_counter(self):
        self.hit = self.hit +1
        self.save()

class Comment(models.Model):
    objects = models.Manager()
    post=models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_date=models.DateTimeField(default=timezone.now)
    comment_contents=models.CharField(max_length=200)
    comment_writer=models.CharField(max_length=100)

class Trait(models.Model):
    objects = models.Manager()
    traits = models.CharField(max_length=50, primary_key=True) # manager can categorize traits of abstract mood
    def __str__(self):
        return self.traits

class Bookstore(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20, default="d", null=True) # name of bookstore
    city_address_of_bookstore = models.CharField(max_length=20) # location of bookstore in city scale
    specific_address = models.TextField() # location of bookstore in specific scale
    trait = models.ForeignKey(Trait, on_delete=models.CASCADE)# trait of bookstore
    bookstore_information = models.TextField() # summary about bookstore
    bookstore_image = models.ImageField(upload_to="image", blank=True)
    def __str__(self):
        return self.name
    
class Evaluation_about_bookstore(models.Model):
    objects = models.Manager()
    evaluation = models.IntegerField(default=0) # about evaluations, mark with number 1 to 5
    comment_about_bookstore_with_text = models.TextField() # utility of comments, user can evaluate with text
    #comment_about_bookstore_with_image = models.ImageField(upload_to="image", blank=True) # utility of comments, user can upload image


class Informations(models.Model):
    objects = models.Manager()
    bookstore = models.ForeignKey(Bookstore, on_delete=models.CASCADE)
    bookstore_image = models.ImageField(upload_to="image", blank=True) # relevant image of bookstore


class Bookstore_event(models.Model):
    objects = models.Manager()
    event_name = models.CharField(max_length=20) # name of events
    event_date = models.DateField(auto_now=True) # date of events
    bookstore = models.ForeignKey(Bookstore, on_delete=models.CASCADE) # bookstore where it be

    # bookstore_resrvation = models.ForeignKey(user, on_delete = models.SET_NULL, null=True, blank=True) # utility of who resrvate bookstore // it is not work
