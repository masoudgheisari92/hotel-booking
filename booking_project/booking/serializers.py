from datetime import datetime

from django.db.models import Q

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Booking, Room


class BookingSerializer(serializers.ModelSerializer):
    """Serialize a booking"""

    class Meta:
        model = Booking
        fields = "__all__"

    def validate_checkin(self, value):
        if value < datetime.now().date():
            raise ValidationError("checkin date can not be earlier than today")
        return value

    def validate(self, attrs):
        if attrs["checkout"] <= attrs["checkin"]:
            raise ValidationError(
                {"checkout": "checkout date should be greater than checkin date"}
            )
        return super().validate(attrs)

    def create(self, validated_data):
        room = validated_data["room"]
        checkin = validated_data["checkin"]
        checkout = validated_data["checkout"]
        if Booking.objects.filter(
            Q(
                room=room,
                checkin__lte=checkin,
                checkout__gt=checkin,
            )
            | Q(
                room=room,
                checkin__lt=checkout,
                checkout__gte=checkout,
            )
        ):
            raise ValidationError({"The room is booked at this time"})
        return super().create(validated_data)


class RoomSerializer(serializers.ModelSerializer):
    hotel = serializers.SlugRelatedField("name", read_only=True)

    class Meta:
        model = Room
        fields = ("name", "hotel")
