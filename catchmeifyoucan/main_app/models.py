from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField
from django.db.models.fields.related import OneToOneField
from django.urls import reverse
import requests
# Create your models here.


def locations(pop):
    
    outer_list = []
    
    
    response = requests.get('https://restcountries.eu/rest/v2/all?fields=name')
    locations = response.json()


    if pop == 'populate':
        pop_list = []




    # Creating a tuple of two tuples from the response for the db
    for location in locations:
        inner_list = []
        inner_tuple = ()
        inner_list.append(location['name'])
        inner_list.append(location['name'])
        inner_tuple = tuple(inner_list)
        outer_list.append(inner_tuple)

    
    return tuple(outer_list)

# def populate_locations():



LOCATION = locations(0)
# LOCATION = (
    
    # ('NULL','NULL')
    # ('CANADA','CANADA'),
    # ('USA','USA'),
    # ('ARCTIC','ARCTIC'),

    # )



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

    # def __str__(self):
    #     return f'{self.name}'

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
