from datetime import datetime

from django.db.models import Q

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Booking
from .utils import get_booked_rooms


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
        if get_booked_rooms(checkin, checkout, room=room):
            raise ValidationError({"The room is booked at this time"})
        return super().create(validated_data)
