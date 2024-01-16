from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from theatre.models import TheatreHall, Genre
from theatre.serializers import TheatreHallSerializers, GenreSerializer


class GenreViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TheatreHallViewSet(viewsets.ModelViewSet):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializers

