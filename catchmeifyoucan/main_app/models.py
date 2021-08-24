from django.db import models

# Create your models here.


class Location(models.Model):
    # INCLDES THE CLUES China id1 , Canada, USA, 4,5 ,56   ..... 10 boom theres frank
    location_name = models.CharField(max_length=200)
    clues = models.CharField(max_length=500)
    map_Cord_X = models.FloatField()
    map_Cord_Y = models.FloatField()


class User(models.Model):
    name = models.CharField(max_length=200)
    win_or_not = models.BooleanField()


class Game(models.Model):
    name = models.CharField(max_length=200)
    number_of_lvls = models.IntegerField(max_length=200)

#  ice box BUT SHOULD REALLY DOOOOOOO1!!!
# class Hints(models.Model):
#     hint1 = models.CharField(max_length=200)
#     hint2 = models.CharField(max_length=200)
#     hint3 = models.CharField(max_length=200)
