from django.db import models

# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

class Book_love(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=70)
    bithday = models.DateField()
    is_intresting = models.BooleanField(default=True)
    year_public = models.DateTimeField()
    genre = models.CharField(max_length=30)
    size = models.IntegerField()