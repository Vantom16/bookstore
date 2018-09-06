from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=256)
    length = models.PositiveIntegerField()
    release_year = models.PositiveIntegerField()

    def _str_(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    release_year = models.PositiveIntegerField()

    def _str_(self):
        return self.author

class Customer(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone = models.PositiveIntegerField()
    def _str_(self):
        return self.first_name + '' + self.last_name
