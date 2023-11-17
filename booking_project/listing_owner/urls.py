from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


app_name = "listing_owner"

router = DefaultRouter()
router.register("hotels", views.HotelViewSet, basename="hotel")
router.register("rooms", views.RoomViewSet, basename="room")


urlpatterns = [
    path("report/hotel/", views.HotelReportView.as_view(), name="hotel-report"),
    path("", include(router.urls)),
]
