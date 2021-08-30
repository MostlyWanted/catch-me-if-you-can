from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.games, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('games/<int:game_id>/', views.game_details, name='game_details'),
    path('games/create', views.GameCreate.as_view(), name='games_create'),
]
