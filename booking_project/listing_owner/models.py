from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class TimeStampedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Hotel(TimeStampedModel):
    name = models.CharField(max_length=32, unique=True)
    owner = models.CharField(max_length=32, null=True, blank=True)
    star = models.PositiveIntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )

    def __str__(self) -> str:
        return self.name


class Room(TimeStampedModel):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    beds = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name
