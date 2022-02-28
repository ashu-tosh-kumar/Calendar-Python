from enum import Enum


# Represents day of a week
class DAY(Enum):
    SUNDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6


# represents a month in a year
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


# Standardized date object used across the application
class Date:
    def __init__(self, date: str) -> None:
        """ Constructor for Date class
        Parameters:
            date: str
                Date ("YYYY-MM-DD") that needs to be represented as a `Date` object
        """
        self._date = date
        year, month, day = map(int, date.split("-"))
        self._year = year
        self._month = MONTH._value2member_map_[month]
        self._day = day

    @property
    def year(self) -> int:
        """ Returns value of year
        Returns:
            _year: int
                Integer representation of year of `Date` object
        """
        return self._year

    @property
    def month(self) -> MONTH:
        """ Returns value of month
        Returns:
            _month: MONTH
                `MONTH` representation of month of `Date` object
        """
        return self._month

    @property
    def day(self) -> int:
        """ Returns value of day
        Returns:
            _day: int
                Integer representation of day of `Date` object
        """
        return self._day

    @day.setter
    def day(self, day: int) -> None:
        """ Allows setting value of day
        Parameters:
            day: int
                Value of day that needs to be set for `Date` object
        """
        self._day = day

    def __str__(self):
        """ Returns string representation of `Date` object
        Returns:
            _date: str
                String representation of `Date` object
        """
        return self._date


# The Britain and the British Empire including the American colonies adopted the Gregorina Calendar on 13-Sept-1752
# We are following the Gregorian Calendar and hence minimum supported date is 01-Oct-1752
PIVOT_DATE = Date("1752-10-01")
PIVOT_DAY = DAY.SUNDAY

# Represents all months that have 31 days in a year
MONTHS_WITH_31_DAYS = {
    MONTH.JANUARY,
    MONTH.MARCH,
    MONTH.MAY,
    MONTH.JULY,
    MONTH.AUGUST,
    MONTH.OCTOBER,
    MONTH.DECEMBER
}
