from datetime import date

from django.db.models import Q

from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    OpenApiExample,
)
from rest_framework import viewsets
from rest_framework.exceptions import APIException

from . import serializers
from .models import Room, Booking
from .utils import *


class BookingViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = serializers.BookingSerializer
    queryset = Booking.objects.all()
    pagination_class = None


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="checkin",
            type=date,
            examples=[OpenApiExample("checkin", "2023-11-16")],
        ),
        OpenApiParameter(
            name="checkout",
            type=date,
            examples=[OpenApiExample("checkout", "2023-11-17")],
        ),
    ]
)
class RoomAvailabilityViewset(viewsets.ReadOnlyModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = serializers.RoomSerializer
    queryset = Room.objects.all()
    pagination_class = None

    def get_queryset(self):
        try:
            checkin = self.request.query_params["checkin"]
            checkout = self.request.query_params["checkout"]
        except KeyError:
            raise APIException("checkin and checkout parameters are required")

        validate_checkin_checkout(checkin, checkout)

        booked_rooms = Booking.objects.filter(
            Q(
                checkin__lte=checkin,
                checkout__gt=checkin,
            )
            | Q(
                checkin__lt=checkout,
                checkout__gte=checkout,
            )
        ).values("room")
        return Room.objects.all().exclude(id__in=booked_rooms)
