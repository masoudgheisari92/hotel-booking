from django.db import models


class TimeStampedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Hotel(TimeStampedModel):
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name


class Room(TimeStampedModel):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=16)

    def __str__(self) -> str:
        return self.name


class Booking(TimeStampedModel):
    username = models.CharField(max_length=32)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()

    def __str__(self) -> str:
        return self.id
