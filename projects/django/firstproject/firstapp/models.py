from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

class Reservation(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    guestCount = models.IntegerField()
    reservationTime = models.DateTimeField(auto_now=True)
    comments = models.CharField(max_length=1000)