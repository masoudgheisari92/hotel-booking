from typing import Any

from django.contrib import admin
from django.http.request import HttpRequest

from .models import Hotel, Room, Booking


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "created_at",
    )
    fields = ("id", "name", "created_at", "updated_at")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "hotel",
        "name",
        "created_at",
    )
    list_filter = ("hotel__name",)
    fields = ("id", "hotel", "name", "created_at", "updated_at")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "room",
        "checkin",
        "checkout",
        "created_at",
    )
    list_filter = ("room__hotel__name",)
    fields = (
        "id",
        "username",
        "room",
        "checkin",
        "checkout",
        "created_at",
        "updated_at",
    )
    readonly_fields = ("id", "created_at", "updated_at")
