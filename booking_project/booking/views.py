from datetime import date

from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    OpenApiExample,
)
from rest_framework import viewsets
from rest_framework.exceptions import APIException

from .serializers import BookingSerializer
from .models import Booking
from .utils import *
from listing_owner.models import Room
from listing_owner.serializers import RoomSerializer


class BookingViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    pagination_class = None


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="checkin",
            type=date,
            examples=[OpenApiExample("checkin", "2023-11-17")],
        ),
        OpenApiParameter(
            name="checkout",
            type=date,
            examples=[OpenApiExample("checkout", "2023-11-18")],
        ),
        OpenApiParameter(
            name="beds", type=int, description="number of beds (not required)"
        ),
    ]
)
class RoomAvailabilityViewset(viewsets.ReadOnlyModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    pagination_class = None

    def get_queryset(self):
        filter_kwargs = {}
        try:
            checkin = self.request.query_params["checkin"]
            checkout = self.request.query_params["checkout"]
        except KeyError:
            raise APIException("checkin and checkout parameters are required")

        beds = self.request.query_params.get("beds")
        if beds:
            filter_kwargs.update({"beds": beds})
        validate_startdate_enddate(checkin, checkout, "checkin", "checkout")
        booked_rooms = get_booked_rooms(checkin, checkout)
        return Room.objects.filter(**filter_kwargs).exclude(
            id__in=booked_rooms.values("room")
        )
