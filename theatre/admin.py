from django.contrib import admin

from theatre.models import TheatreHall, Genre, Actor

# Register your models here.
admin.site.register(Genre)
admin.site.register(Actor)


@admin.register(TheatreHall)
class TheatreHallAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "rows",
        "seats_in_row",
        "capacity",
    ]
