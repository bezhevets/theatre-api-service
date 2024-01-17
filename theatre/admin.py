from django.contrib import admin

from theatre.models import (
    TheatreHall,
    Genre,
    Actor,
    Play,
    Performance,
    Ticket,
    Reservation
)

# Register your models here.
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Play)
admin.site.register(Performance)
admin.site.register(Ticket)


class TicketInline(admin.TabularInline):
    model = Ticket
    extra = 1


@admin.register(Reservation)
class OrderAdmin(admin.ModelAdmin):
    inlines = (TicketInline,)


@admin.register(TheatreHall)
class TheatreHallAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "rows",
        "seats_in_row",
        "capacity",
    ]
