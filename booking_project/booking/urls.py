from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


app_name = "booking"

router = DefaultRouter()
router.register(
    "available-rooms", views.RoomAvailabilityViewset, basename="available-rooms"
)
router.register("", views.BookingViewSet, basename="booking")


urlpatterns = [
    path("", include(router.urls)),
]
