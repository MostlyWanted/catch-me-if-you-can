from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.games, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('games/<int:game_id>/', views.game_details, name='game_details'),
    path('games/create', views.GameCreate.as_view(), name='games_create'),
    path('games/<int:pk>/update', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete', views.GameDelete.as_view(), name='games_delete'),
    # path('location/<int:game_id>/', views.location_details, name='locations_details'),
    path('location/create', views.LocationCreate.as_view(), name='locations_create'),
    path('location/<int:pk>/update', views.LocationUpdate.as_view(), name='locations_update'),
    path('location/<int:pk>/delete', views.LocationDelete.as_view(), name='locations_delete'),
    path ('games/<int:game_id>/assoc_location/<int:location_id>/', views. assoc_location, name='assoc_location')
]
