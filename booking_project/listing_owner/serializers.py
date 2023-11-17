from rest_framework import serializers

from .models import Hotel, Room


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ["id", "name", "star"]


class HotelDetailSerializer(HotelSerializer):
    class Meta(HotelSerializer.Meta):
        fields = HotelSerializer.Meta.fields + ["owner"]


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id", "name", "hotel", "beds"]


class Room2Serializer(RoomSerializer):
    hotel = HotelSerializer(read_only=True)
