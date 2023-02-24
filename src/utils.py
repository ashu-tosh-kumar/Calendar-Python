import logging
from enum import Enum

from src.constants import MONTH, MONTHS_WITH_31_DAYS, Date
from src.exceptions import InvalidDateFormat

logger = logging.getLogger(__name__)


def is_leap_year(year: int) -> bool:
    """Checks whether a year is leap year or not
    Parameters:
        year: int
            Year that needs to be checked
    Returns:
        is_leap_year: bool
            Boolean flag as `True` if given `year` is a leap year else `False`
    """
    logger.debug(f"Checking year: {year} for leap year")

    is_leap_year = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                is_leap_year = False
        else:
            is_leap_year = True
    else:
        is_leap_year = False

    logger.debug(f"Leap year check: {year}: {is_leap_year}")
    return is_leap_year


def count_leap_years(date: Date) -> int:
    """Count number of leap years passed until given `date`

    if takes current year into consideration if `date` is beyond month of February else not

    Parameters:
        date: Date
            Date until which we need to calculate no. of leap years
    Returns:
        num_leap_years_until_date: int
            No. of leap years passed until the `date`
    """
    logger.debug(f"Counting no. of leap years until date: {date}")
    num_leap_years_until_date = 0
    year = date.year

    if date.month.value <= 2:
        year -= 1

    num_leap_years_until_date = year // 4
    num_leap_years_until_date -= year // 100
    num_leap_years_until_date += year // 400

    logger.debug(f"No. of leap years until date: {date}: {num_leap_years_until_date}")
    return num_leap_years_until_date


def get_default_days_in_month(month: Enum) -> int:
    """Returns no. of default days in a month without considering a leap year
    Parameters:
        month: Enum
            month for which actual days is required
    Returns:
        numDays : int
            No. of days in given month `month`
    """
    if month in MONTHS_WITH_31_DAYS:
        return 31
    elif month is MONTH.FEBRUARY:
        return 28
    else:
        return 30


def get_actual_days_in_month(month: Enum, year: int) -> int:
    """Returns no. of actual days in a month with considering a leap year

    Makes use of `getDefaultDaysInMonth`

    Parameters:
        month: Enum
            month for which actual days is required
        year: int
            Year in which no. of days is required for `month`
    Returns:
        numDays : int
            No. of days in given month `month`
    """
    if month is MONTH.FEBRUARY:
        if is_leap_year(year):
            return 29
        else:
            return get_default_days_in_month(month)
    else:
        return get_default_days_in_month(month)


def num_days_between_dates(base_date: Date, actual_date: Date) -> int:
    """Returns difference of days between two dates

    Makes use of `getDefaultDaysInMonth`, `countLeapYears`

    Parameters:
        base_date: Date
            Base date from which difference needs to be calculated

        actual_date: Date
            Actual date upto which difference needs to be calculated
    Returns:
        numDays : int
            Difference of days between `total_days_actual_date` `total_days_base_date`
    """
    logger.debug(f"Counting diff of days between: {base_date} and {actual_date}")

    def calculate_absolute_days(date: Date) -> int:
        """Returns no. of absolute days since beginning until `date`

        Makes use of `getDefaultDaysInMonth`, `countLeapYears`

        Parameters:
            date: Date
                Date for which absolute no. of days needs to be calculated
        Returns:
            numDays : int
                No. of days since beginning until `date`
        """
        total_days = date.year * 365 + date.day
        for i in range(1, date.month.value):
            total_days += get_default_days_in_month(MONTH._value2member_map_[i])

        total_days += count_leap_years(date)
        return total_days

    total_days_base_date = calculate_absolute_days(base_date)
    total_days_actual_date = calculate_absolute_days(actual_date)

    logger.debug(f"Diff of days between: {base_date} and {actual_date} = {total_days_actual_date - total_days_base_date}")
    return total_days_actual_date - total_days_base_date


def date_validator(date: str, pivot_date: Date) -> None:
    """Validates a string date to be accepted by the application

    Parameters:
        date: str
            Date that needs to be validated

        pivot_date: Date
            Minimum possible date supported by the application
    Raises:
        InvalidDateFormat
            If the passed `date` fails the validations test(s)
    """
    logger.info(f"Validating date: {date}")
    try:
        year, month, day = date.split("-")
    except Exception:
        logger.info(f"Failed to fetch year, month and/or day information from string: {date}")
        raise InvalidDateFormat(f"String {date} doesn't contain enough separators to specify year, month and day")

    try:
        year, month, day = int(year), int(month), int(day)
    except Exception:
        logger.info(f"Year and/or month and/or day of date: {date} is/are not Integers")
        raise InvalidDateFormat(f"Year: {year} or month: {month} or day: {day} is/are not integer(s)")

    if month <= 0 or month > 12:
        logger.info(f"Month of date: {date} is not in range [1, 12]")
        raise InvalidDateFormat(f"Given month {month} isn't between [1, 12]")

    if day < 0 or day > 31:
        logger.info(f"Day of date: {date} is not in range [1, 31]")
        raise InvalidDateFormat(f"Given day: {day} isn't between [1, 31]")

    if month == 2:
        if is_leap_year(year):
            if day > 29:
                logger.info(f"Month of date: {date} is not in range [1, 29] for a leap year")
                raise InvalidDateFormat(f"Given day: {day} isn't between [1,29] for a leap year")
        else:
            if day > 28:
                logger.info(f"Month of date: {date} is not in range [1, 28] for a non-leap year")
                raise InvalidDateFormat(f"Given day: {day} isn't between [1,28] for a non-leap year")
    elif MONTH._value2member_map_[month] not in MONTHS_WITH_31_DAYS:
        if day == 31:
            logger.info(f"Month of date: {date} is not in range [1,30]")
            raise InvalidDateFormat(f"Given day: {day} isn't between [1, 30] for given month: {MONTH._value2member_map_[month].name}")

    if num_days_between_dates(pivot_date, Date(date)) < 0:
        logger.info(f"Give: {date} is less than the pivot date: {pivot_date} and hence not supported")
        raise InvalidDateFormat(f"Given date: {date} should be greater or equal to {pivot_date}")
