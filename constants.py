from enum import Enum


class DAY(Enum):
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6


class MONTH(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


class Date:
    def __init__(self, date: str) -> None:
        self._date = date
        year, month, day = map(int, date.split("-"))
        self._year = year
        self._month = MONTH._value2member_map_[month]
        self._day = day

    @property
    def year(self) -> int:
        return self._year

    @property
    def month(self) -> MONTH:
        return self._month

    @property
    def day(self) -> int:
        return self._day

    @day.setter
    def day(self, day) -> int:
        self._day = day

    def __str__(self):
        return self._date


# The Britain and the British Empire including the American colonies adopted the Gregorina Calendar on 13-Sept-1752
# We are following the Gregorian Calendar and hence minimum supported date is 01-Oct-1752
PIVOT_DATE = Date("1752-10-01")
PIVOT_DAY = DAY.SUNDAY

MONTHS_WITH_31_DAYS = {
    MONTH.JANUARY,
    MONTH.MARCH,
    MONTH.MAY,
    MONTH.JULY,
    MONTH.AUGUST,
    MONTH.OCTOBER,
    MONTH.DECEMBER
}
