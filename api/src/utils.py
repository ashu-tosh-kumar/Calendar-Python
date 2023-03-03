from enum import Enum

from api.src import constants, exceptions
from api.src.initializer import logger


def is_leap_year(year: int) -> bool:
    """Checks whether a year is leap year or not

    Args:
        year (int): Year that needs to be checked

    Returns:
        bool: Boolean flag as `True` if given `year` is a leap year else `False`
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


def count_leap_years(date: constants.Date) -> int:
    """Count number of leap years passed until given `date`

    - It takes current year into consideration if `date` is beyond month of February

    Args:
        date (constants.Date): Date until which we need to calculate no. of leap years

    Returns:
        int: No. of leap years passed until the `date`
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

    Args:
        month (Enum): month for which actual days is required

    Returns:
        int: No. of days in given month `month`
    """
    logger.debug(f"Getting default days for month: {month}")

    if month in constants.MONTHS_WITH_31_DAYS:
        return 31
    elif month is constants.MONTH.FEBRUARY:
        return 28
    else:
        return 30


def get_actual_days_in_month(month: Enum, year: int) -> int:
    """Returns no. of actual days in a month with considering a leap year

    - Makes use of `getDefaultDaysInMonth`

    Args:
        month (Enum): month for which actual days is required
        year (int): Year in which no. of days is required for `month`

    Returns:
        int: No. of days in given month `month`
    """
    logger.debug(f"Getting actual days for month: {month} for year: {year}")

    if month is constants.MONTH.FEBRUARY:
        if is_leap_year(year):
            return 29
        else:
            return get_default_days_in_month(month)
    else:
        return get_default_days_in_month(month)


def num_days_between_dates(base_date: constants.Date, actual_date: constants.Date) -> int:
    """Returns difference of days between two dates

    - Makes use of `getDefaultDaysInMonth`, `countLeapYears`

    Args:
        base_date (constants.Date): Base date from which difference needs to be calculated
        actual_date (constants.Date): Actual date upto which difference needs to be calculated

    Returns:
        int: Difference of days between `total_days_actual_date` `total_days_base_date`
    """
    logger.debug(f"Counting diff of days between: {base_date} and {actual_date}")

    def calculate_absolute_days(date: constants.Date) -> int:
        """Returns no. of absolute days since beginning until `date`

        - Makes use of `getDefaultDaysInMonth`, `countLeapYears`

        Args:
            date (constants.Date): Date for which absolute no. of days needs to be calculated

        Returns:
            int: No. of days since beginning until `date`
        """
        logger.debug(f"Calculating absolute number of days from beginning for date: {date}")

        total_days = date.year * 365 + date.day
        for i in range(1, date.month.value):
            total_days += get_default_days_in_month(constants.MONTH._value2member_map_[i])

        total_days += count_leap_years(date)
        logger.debug(f"Absolute number of days from beginning for date: {date} calculated = {total_days}")

        return total_days

    total_days_base_date = calculate_absolute_days(base_date)
    total_days_actual_date = calculate_absolute_days(actual_date)
    logger.debug(
        f"Diff of days between: {base_date} and {actual_date} = {total_days_actual_date} - {total_days_base_date} = {total_days_actual_date - total_days_base_date}"
    )

    return total_days_actual_date - total_days_base_date


def date_validator(date: str, pivot_date: constants.Date) -> None:
    """Validates a string date to be accepted by the application

    Args:
        date (str): Date that needs to be validated
        pivot_date (constants.Date): Minimum possible date supported by the application

    Raises:
        exceptions.InvalidDateFormat: If the passed `date` fails the validations test(s)
    """
    logger.info(f"Validating date: {date}")
    try:
        year, month, day = date.split("-")
    except Exception:
        logger.info(f"Failed to fetch year, month and/or day information from string: {date}")
        raise exceptions.InvalidDateFormat(f"String {date} doesn't contain enough separators to specify year, month and day")

    try:
        year, month, day = int(year), int(month), int(day)
    except Exception:
        logger.info(f"Year and/or month and/or day of date: {date} is/are not Integers")
        raise exceptions.InvalidDateFormat(f"Year: {year} or month: {month} or day: {day} is/are not integer(s)")

    if month <= 0 or month > 12:
        logger.info(f"Month of date: {date} is not in range [1, 12]")
        raise exceptions.InvalidDateFormat(f"Given month {month} isn't between [1, 12]")

    if day < 0 or day > 31:
        logger.info(f"Day of date: {date} is not in range [1, 31]")
        raise exceptions.InvalidDateFormat(f"Given day: {day} isn't between [1, 31]")

    if month == 2:
        if is_leap_year(year):
            if day > 29:
                logger.info(f"Month of date: {date} is not in range [1, 29] for a leap year")
                raise exceptions.InvalidDateFormat(f"Given day: {day} isn't between [1,29] for a leap year")
        else:
            if day > 28:
                logger.info(f"Month of date: {date} is not in range [1, 28] for a non-leap year")
                raise exceptions.InvalidDateFormat(f"Given day: {day} isn't between [1,28] for a non-leap year")
    elif constants.MONTH._value2member_map_[month] not in constants.MONTHS_WITH_31_DAYS:
        if day == 31:
            logger.info(f"Month of date: {date} is not in range [1,30]")
            raise exceptions.InvalidDateFormat(f"Given day: {day} isn't between [1, 30] for given month: {constants.MONTH._value2member_map_[month].name}")

    if num_days_between_dates(pivot_date, constants.Date(date)) < 0:
        logger.info(f"Give: {date} is less than the pivot date: {pivot_date} and hence not supported")
        raise exceptions.InvalidDateFormat(f"Given date: {date} should be greater or equal to {pivot_date}")
