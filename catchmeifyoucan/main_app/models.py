from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField
from django.db.models.fields.related import OneToOneField
from django.urls import reverse
import requests
# Create your models here.


def locations(populate):
    
    outer_list = []
    
    
    response = requests.get('https://restcountries.eu/rest/v2/all?fields=name')
    locations = response.json()

    

    if populate == 'populate':
        populate_list = []


        for location in locations:
            populate_list.append(location['name'])
            

            

        for country in populate_list:
            r = requests.get(f'https://restcountries.eu/rest/v2/name/{country}?fullText=true')

            clues = r.json()
            clues = clues[0]
            
            location = Location(location_name=country, map_cord_X=0, map_cord_Y=0)

            location.save()

            location.clue_set.create(clue_name='capital', desc=clues['capital'])
            location.clue_set.create(clue_name='subregion', desc=clues['subregion'])
            location.clue_set.create(clue_name='borders', desc=clues['borders'][0])
            location.clue_set.create(clue_name='timezones', desc=clues['timezones'][0])
            location.clue_set.create(clue_name='currencies', desc=clues['currencies'][0]['code'])
            location.clue_set.create(clue_name='callingCodes', desc=clues['callingCodes'][0])
            location.clue_set.create(clue_name='population', desc=clues['population'])
            location.clue_set.create(clue_name='area', desc=clues['area'])
            

        return 0





    # Creating a tuple of two tuples from the response for the db
    for location in locations:
        inner_list = []
        inner_tuple = ()
        inner_list.append(location['name'])
        inner_list.append(location['name'])
        inner_tuple = tuple(inner_list)
        outer_list.append(inner_tuple)

    
    return tuple(outer_list)

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
    map_cord_X = models.FloatField()
    map_cord_Y = models.FloatField()

    
class Clue(models.Model):
    clue_name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    # capital = models.CharField(max_length=200)
    # subregion = models.CharField(max_length=200)
    # borders = models.CharField(max_length=200)
    # timezones = models.CharField(max_length=200)
    # currencies = models.CharField(max_length=200)
    # callingCodes = models.CharField(max_length=200)
    # population = models.CharField(max_length=200)
    # area = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


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
