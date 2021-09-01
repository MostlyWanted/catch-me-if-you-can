from django.forms import ModelForm, Form
from .models import Location, Game

class LocationForm(ModelForm):
  class Meta:
    model = Location
    fields = ['location_name']

class GameForm(ModelForm):
  class Meta:
    model = Game
    fields = '__all__'