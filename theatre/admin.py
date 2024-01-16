from django.contrib import admin

from theatre.models import TheatreHall, Genre, Actor

# Register your models here.
admin.site.register(TheatreHall)
admin.site.register(Genre)
admin.site.register(Actor)
