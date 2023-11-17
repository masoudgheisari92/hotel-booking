from django.contrib import admin

from .models import Booking


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
