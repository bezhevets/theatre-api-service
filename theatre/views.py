from rest_framework import viewsets

from theatre.models import TheatreHall
from theatre.serializers import TheatreHallSerializers


class TheatreHallViewSet(viewsets.ModelViewSet):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializers

