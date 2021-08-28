from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.games, name='index'),
    path('accounts/signup/', views.signup, name='signup')]
