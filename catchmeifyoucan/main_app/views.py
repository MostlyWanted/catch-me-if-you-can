from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('< h1 > hello this is our game < /h1 > ')


def games(request):
    return HttpResponse(' Hello these are all the games available to play')
