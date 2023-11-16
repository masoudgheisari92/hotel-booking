from datetime import datetime

from rest_framework.exceptions import ValidationError


def validate_checkin_checkout(checkin: str, checkout: str) -> bool:
    try:
        checkin = datetime.strptime(checkin, "%Y-%m-%d").date()
        checkout = datetime.strptime(checkout, "%Y-%m-%d").date()
    except ValueError:
        raise ValidationError("checkin or checkout does not match format '%Y-%m-%d'")

    if checkout <= checkin:
        raise ValidationError("checkout date should be greater than checkin date")

    return True
