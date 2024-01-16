from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from theatre.models import TheatreHall, Genre, Actor
from theatre.serializers import (
    TheatreHallSerializers,
    GenreSerializer,
    ActorSerializer,
)


class GenreViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class TheatreHallViewSet(viewsets.ModelViewSet):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializers

