from rest_framework import serializers

from theatre.models import TheatreHall


class TheatreHallSerializers(serializers.ModelSerializer):
    class Meta:
        model = TheatreHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")
