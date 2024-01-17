from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from theatre.models import TheatreHall, Genre, Actor, Play
from theatre.serializers import (
    TheatreHallSerializers,
    GenreSerializer,
    ActorSerializer, PlaySerializer, PlayListSerializer, PlayDetailSerializer,
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


class TheatreHallViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializers


class PlayViewSet(
    viewsets.ModelViewSet
):
    queryset = Play.objects.all().prefetch_related("actors", "genres")
    serializer_class = PlaySerializer

    def get_serializer_class(self):
        if self.action == "list":
            return PlayListSerializer
        if self.action == "retrieve":
            return PlayDetailSerializer
        return PlaySerializer
