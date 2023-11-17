from datetime import date

from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
    OpenApiExample,
)
import pandas as pd
from rest_framework import viewsets, generics
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from . import serializers
from .models import Hotel, Room
from .utils import *
from booking.models import Booking
from booking.serializers import BookingSerializer
from booking.utils import validate_startdate_enddate, get_booked_rooms


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


@extend_schema(
    parameters=[
        OpenApiParameter(
            name="hotel",
            type=int,
            description="id of the hotel",
            required=True,
        ),
        OpenApiParameter(
            name="report_format",
            type=str,
            description="The format of the report. choice: `html`, `json`",
        ),
        OpenApiParameter(
            name="start_date",
            type=date,
            examples=[OpenApiExample("start_date", "2023-11-17")],
        ),
        OpenApiParameter(
            name="end_date",
            type=date,
            examples=[OpenApiExample("end_date", "2023-11-18")],
        ),
    ]
)
class HotelReportView(generics.ListAPIView):
    authentication_classes = ()
    permission_classes = ()
    pagination_class = None
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            hotel = int(self.request.query_params["hotel"])
        except KeyError:
            raise APIException("`hotel` parameter is required")

        try:
            start_date = self.request.query_params["start_date"]
            end_date = self.request.query_params["end_date"]
        except KeyError:
            raise APIException("`start_date` and `end_date` parameters are required")
        validate_startdate_enddate(start_date, end_date, "start_date", "end_date")

        self.queryset = get_booked_rooms(
            start_date, end_date, room__hotel_id=hotel
        ).order_by("room", "checkin")

        report_format = request.query_params.get("report_format")
        if not report_format:
            report_format = "html"

        hotel_rooms = Room.objects.filter(hotel_id=hotel)
        kwargs.update({"report_format": report_format, "hotel_rooms": hotel_rooms})
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        report = get_booked_rooms_report(
            booking_queryset=queryset,
            report_format=kwargs["report_format"],
            hotel_rooms_queryset=kwargs["hotel_rooms"],
            report_start_data=request.query_params["start_date"],
            report_end_date=request.query_params["end_date"],
        )

        return Response(report)
