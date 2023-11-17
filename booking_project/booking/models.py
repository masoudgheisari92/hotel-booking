from django.db import models

from listing_owner.models import Room


class TimeStampedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Booking(TimeStampedModel):
    username = models.CharField(max_length=32)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()
