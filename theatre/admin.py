from django.contrib import admin

from theatre.models import TheatreHall, Genre, Actor, Play, Performance

# Register your models here.
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Play)
admin.site.register(Performance)


@admin.register(TheatreHall)
class TheatreHallAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "rows",
        "seats_in_row",
        "capacity",
    ]
