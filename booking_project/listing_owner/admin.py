from django.contrib import admin

from .models import Hotel, Room


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "star",
        "created_at",
    )
    fields = ("id", "name", "star", "created_at", "updated_at")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "hotel",
        "name",
        "beds",
        "created_at",
    )
    list_filter = ("hotel__name", "beds")
    fields = ("id", "hotel", "name", "beds", "created_at", "updated_at")
    readonly_fields = ("id", "created_at", "updated_at")
