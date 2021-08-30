from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Game


def home(request):
    return HttpResponse('< h1 > hello this is our game < /h1 > ')


@login_required
def games(request):
    games = Game.objects.all()
    return render(request, 'games/home.html/', {'games': games})
    # return render('games/home.html/')


@login_required
def game_details(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'games/details.html/', {'game': game})


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
