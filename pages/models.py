from django.db import models

# Create your models here.
class Flight(models.Model):
    name = models.CharField(max_length=100)
    flightType = models.CharField(max_length=100)
    price = models.IntegerField()