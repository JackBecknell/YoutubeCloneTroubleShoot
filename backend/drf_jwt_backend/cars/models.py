from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<
jack = "string"
tessa = 1
cash = True
jj = ["list item at index 0", "list item at index 1"]

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=100)
    year = models.IntegerField()

class Github(models.Model):
    change = models.CharField(max_length=100)
    this = models.CharField(max_length=100)
    buddy = models.IntegerField()
