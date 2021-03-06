from .models import User, Location, Game, Gamer
# from my_user_profile_app.models import Gamer
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin


# Register your models here.

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton


class GamerInline(admin.StackedInline):
    model = Gamer
    can_delete = False
    verbose_name_plural = 'gamer'

# Define a new User admin


class UserAdmin(BaseUserAdmin):
    inlines = (GamerInline,)

# Re-register UserAdmin


admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

# Register your models here.
admin.site.register(User)

admin.site.register(Location)

admin.site.register(Game)
