from django.db import models

# Create your models here.
class Booking(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    guestNum = models.IntegerField()
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.firstName + ' ' + self.lastName


class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name