from enum import Enum

from utils import Date


class DAY(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


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


# The Britain and the British Empire including the American colonies adopted the Gregorina Calendar on 13-Sept-1752
# We are following the Gregorian Calendar and henceminimum supported date is 14-Sept-1752
PIVOT_DATE = Date("1752-09-14")
PIVOT_DAY = DAY.THURSDAY

MONTHS_WITH_31_DAYS = {
    MONTH.JANUARY,
    MONTH.MARCH,
    MONTH.MAY,
    MONTH.JULY,
    MONTH.AUGUST,
    MONTH.OCTOBER,
    MONTH.DECEMBER
}
