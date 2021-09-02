from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game, Location
from .forms import LocationForm
import requests


def home(request):
    return render(request ,'maps.html')

@login_required
def play(request, game_id):
    game = Game.objects.get(id=game_id)
    locations = game.locations.all()

    response = requests.get('https://restcountries.eu/rest/v2/name/Canada?fullText=true')

    clues = response.json()
    clues = clues[0]

    usr_clues = {}

    usr_clues['capital'] = clues['capital']
    usr_clues['subregion'] = clues['subregion']
    # usr_clues['language'] = clues['language'][0]
    usr_clues['borders'] = clues['borders']
    # usr_clues['topLevelDomain'] = clues['topLevelDomain'][0]
    usr_clues['timezones'] = clues['timezones']
    usr_clues['currencies'] = clues['currencies'][0]['code']
    usr_clues['callingCodes'] = clues['callingCodes']
    usr_clues['population'] = clues['population']
    usr_clues['area'] = clues['area']
    
    return render(request, 'games/play.html', {'game': game, 'locations': locations, 'clues': usr_clues})

class GameCreate(CreateView):
    model = Game
    fields = ['name','number_of_lvls','description']
    last_record = Game.objects.all().count() + 1
    success_url = f'/games/{last_record}/'
    # success_url = '/games/'


class LocationCreate(CreateView):
    model = Location
    fields = '__all__'
    # last_record = Location.objects.all().count() + 1
    # success_url = f'/games/{last_record}/'
    # success_url =  f'/games/{last_record}/'

def assoc_location(request, game_id, ignore_id, location_id):
    Game.objects.get(id=game_id).locations.add(location_id)
    return redirect('game_details', game_id=game_id)

@login_required
def games(request):
    games = Game.objects.all()
    return render(request, 'games/home.html/', {'games': games})
    # return render('games/home.html/')


@login_required
def game_details(request, game_id):
    game = Game.objects.get(id=game_id)
    locationsOptions = Location.objects.all()
    location_form = LocationForm()
    return render(request, 'games/details.html/', {'game': game, 'location_form': location_form, 'locations': locationsOptions})


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('home')
        else:
            error_message = 'really bro!'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class GameUpdate(UpdateView):
    model = Game
    fields = '__all__'
    success_url = '/games/'


class GameDelete(DeleteView):
    model = Game
    success_url = '/games/'

class LocationUpdate(UpdateView):
    model = Location
    fields = '__all__'
    success_url = '/games/'

class LocationDelete(DeleteView):
    model = Location
    success_url = '/games/'