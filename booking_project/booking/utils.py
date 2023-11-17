from datetime import datetime, date

from django.db.models import Q, QuerySet

from rest_framework.exceptions import ValidationError

from .models import Booking


def validate_startdate_enddate(
    date1: str, date2: str, date1_name: str = "date1", date2_name: str = "date2"
) -> bool:
    try:
        date1 = datetime.strptime(date1, "%Y-%m-%d").date()
        date2 = datetime.strptime(date2, "%Y-%m-%d").date()
    except ValueError:
        raise ValidationError(
            f"{date1_name} or {date2_name} does not match format '%Y-%m-%d'"
        )

    if date2 <= date1:
        raise ValidationError(f"{date2_name} should be greater than {date1_name}")

    if date1 < datetime.now().date():
        raise ValidationError(f"{date1_name} date can not be earlier than today")

    return True


def get_booked_rooms(start_date: date, end_date: date, **kwargs) -> QuerySet:
    return Booking.objects.filter(**kwargs).filter(
        Q(
            checkin__lte=start_date,
            checkout__gt=start_date,
        )
        | Q(
            checkin__lt=end_date,
            checkout__gte=end_date,
        )
        | Q(
            checkin__gt=start_date,
            checkout__lt=end_date,
        )
    )
