from django.utils import timezone
from django.db import models
from django.conf import settings

class Blog(models.Model):
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
    post=models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, related_name='comments')
    comment_date=models.DateTimeField(default=timezone.now)
    comment_contents=models.CharField(max_length=200)
    comment_writer=models.CharField(max_length=100)

