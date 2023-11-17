from abc import ABC, abstractmethod
from datetime import date, datetime, timedelta

from django.db.models import QuerySet

import pandas as pd
from rest_framework.exceptions import NotFound


class DFConvertor(ABC):
    def __init__(self, df: pd.DataFrame):
        self.df = df

    @staticmethod
    @abstractmethod
    def meets_condition(report_format: str) -> bool:
        return False

    @abstractmethod
    def convert(self) -> str:
        """convert dataframe"""


class DFtoHTMLConvertor(DFConvertor):
    @staticmethod
    def meets_condition(report_format: str) -> bool:
        return report_format == "html"

    def convert(self) -> str:
        html = "<h1> Report Table <h1>"
        html += self.df.to_html()
        html = html.replace("\n", "")
        return html


class DFtoJsonConvertor(DFConvertor):
    @staticmethod
    def meets_condition(report_format: str) -> bool:
        return report_format == "json"

    def convert(self) -> str:
        return self.df.to_json()


def get_df_convertor(report_format: str, df: pd.DataFrame) -> DFConvertor:
    for convertor in DFConvertor.__subclasses__():
        if convertor.meets_condition(report_format):
            return convertor(df)  # type: ignore
    else:
        raise NotFound("df convertor not found")


def get_booked_rooms_report(
    booking_queryset: QuerySet,
    report_format: str,
    hotel_rooms_queryset: QuerySet,
    report_start_data: date,
    report_end_date: date,
) -> str:
    room_names = hotel_rooms_queryset.values_list("name", flat=True)
    report_start_data = datetime.strptime(report_start_data, "%Y-%m-%d").date()
    report_end_date = datetime.strptime(report_end_date, "%Y-%m-%d").date()
    pandas_columns = []
    rdate = report_start_data
    while rdate < report_end_date:
        pandas_columns.append(rdate)
        rdate += timedelta(1)

    df = pd.DataFrame(columns=pandas_columns, index=room_names)

    for booking in booking_queryset:
        bdate = booking.checkin
        while bdate < min(booking.checkout, report_end_date):
            df.loc[booking.room.name, bdate] = "Booked"
            bdate += timedelta(1)

    convertor = get_df_convertor(report_format, df)

    return convertor.convert()
