from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from theatre.models import TheatreHall, Genre, Actor, Play, Performance, Ticket, Reservation


class TheatreHallSerializers(serializers.ModelSerializer):
    class Meta:
        model = TheatreHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ("id", "title", "description", "actors", "genres")


class PlayListSerializer(PlaySerializer):
    actors = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="full_name"
    )
    genres = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )


class PlayDetailSerializer(PlaySerializer):
    actors = ActorSerializer(read_only=True, many=True)
    genres = GenreSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Play
        fields = (
            "id",
            "title",
            "description",
            "actors",
            "genres",
            "image"
        )


class PlayImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ("id", "image")


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = (
            "id",
            "show_time",
            "play",
            "theatre_hall",
        )


class PerformanceListSerializer(PerformanceSerializer):
    play_title = serializers.CharField(source="play.title", read_only=True)
    play_image = serializers.CharField(source="play.image", read_only=True)
    theatre_hall_name = serializers.CharField(
        source="theatre_hall.name",
        read_only=True
    )
    theatre_hall_capacity = serializers.IntegerField(
        source="theatre_hall.capacity",
        read_only=True
    )

    class Meta:
        model = Performance
        fields = (
            "id",
            "show_time",
            "play_title",
            "play_image",
            "play_image",
            "theatre_hall_name",
            "theatre_hall_capacity",
        )


class PerformanceDetailSerializer(PerformanceSerializer):
    play = PlayListSerializer(read_only=True, many=False)
    theatre_hall = TheatreHallSerializers(read_only=True, many=False)


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("id", "row", "seat", "performance")


class ReservationSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=False, allow_empty=False)

    class Meta:
        model = Reservation
        fields = ("id", "tickets", "created_at")

    def create(self, validated_data):
        with transaction.atomic():
            tickets_data = validated_data.pop("tickets")
            order = Reservation.objects.create(**validated_data)
            for ticket_data in tickets_data:
                Ticket.objects.create(order=order, **ticket_data)
            return order
