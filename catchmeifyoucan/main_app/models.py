from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField
from django.db.models.fields.related import OneToOneField
from django.urls import reverse

# Create your models here.
LOCATION = (
    # ('NULL','NULL')
    ('CANADA','CANADA'),
    ('USA','USA'),
    ('ARCTIC','ARCTIC'),

    )



class Location(models.Model):
    # INCLDES THE CLUES China id1 , Canada, USA, 4,5 ,56   ..... 10 boom theres frank
    location_name = models.CharField(
        choices = LOCATION,  
        max_length=200
    )
    clues = models.CharField(max_length=500)
    map_Cord_X = models.FloatField()
    map_Cord_Y = models.FloatField()

class Game(models.Model):
    name = models.CharField(max_length=200)
    number_of_lvls = models.IntegerField(default=0)
    description = models.TextField(max_length=200)
    locations = models.ManyToManyField(Location, null = True)

class User(models.Model):
    name = models.CharField(max_length=200)
    win_or_not = models.BooleanField()



    def get_absolut_url(self):
        return reverse('detail', kwargs={'game_id': self.id})

#  ice box BUT SHOULD REALLY DOOOOOOO1!!!
# class Hints(models.Model):
#     hint1 = models.CharField(max_length=200)
#     hint2 = models.CharField(max_length=200)
#     hint3 = models.CharField(max_length=200)


class Gamer(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    account = models.IntegerField()
