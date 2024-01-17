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
    queryset = Play.objects.prefetch_related("actors", "genres")
    serializer_class = PlaySerializer

    @staticmethod
    def _params_str_to_int(params_in_url: str) -> list:
        """Converts a list of string IDs to a list of integers"""
        return [int(param) for param in params_in_url.split(",")]

    def get_queryset(self):
        """Retrieve the movies with filters"""
        title = self.request.query_params.get("title")
        genres = self.request.query_params.get("genres")
        actors = self.request.query_params.get("actors")

        queryset = self.queryset

        if title:
            queryset = queryset.filter(title__icontains=title)

        if genres:
            genres_id = self._params_str_to_int(genres)
            queryset = queryset.filter(genres__id__in=genres_id)

        if actors:
            actors_id = self._params_str_to_int(actors)
            queryset = queryset.filter(actors__id__in=actors_id)

        return queryset.distinct()

    def get_serializer_class(self):
        if self.action == "list":
            return PlayListSerializer
        if self.action == "retrieve":
            return PlayDetailSerializer
        return PlaySerializer
