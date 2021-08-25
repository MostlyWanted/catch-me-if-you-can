from django.contrib import admin
from .models import User, Location, Game

# Register your models here.
admin.site.register(User)

admin.site.register(Location)

admin.site.register(Game)
