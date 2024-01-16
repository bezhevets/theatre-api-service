from django.contrib import admin

from theatre.models import TheatreHall, Genre

# Register your models here.
admin.site.register(TheatreHall)
admin.site.register(Genre)
