from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    OpenApiExample,
)
from rest_framework import viewsets
from rest_framework.exceptions import APIException

from . import serializers
from .models import Hotel, Room


class HotelViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = serializers.HotelDetailSerializer
    queryset = Hotel.objects.all()
    pagination_class = None


class RoomViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = serializers.RoomSerializer
    queryset = Room.objects.all()
    pagination_class = None
