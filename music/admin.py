from django.contrib import admin
from . models import Song, Favourites, History, Profile

# Register your models here.

admin.site.register(Song)
admin.site.register(Favourites)
admin.site.register(History)
admin.site.register(Profile)

