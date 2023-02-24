import logging

from src.constants import MONTH, MONTHS_WITH_31_DAYS, Date
from src.exceptions import InvalidDateFormat

logger = logging.getLogger(__name__)


def isLeapYear(year: int) -> bool:
    """Checks whetehr a year is leap year or not
    Parameters:
        year: int
            Year that needs to be checked
    Returns:
        isLeapYear: bool
            Boolean flag as `True` if given `year` is a leap year else `False`
    """
    logger.debug(f"Checking year: {year} for leap year")

    isLeapYear = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                isLeapYear = False
        else:
            isLeapYear = True
    else:
        isLeapYear = False

    logger.debug(f"Leap year check: {year}: {isLeapYear}")
    return isLeapYear


def countLeapYears(date: Date) -> int:
    """Count number of leap years passed until given `date`

    if takes current year into consideration if `date` is beyond month of February else not

    Parameters:
        date: Date
            Date untl which we need to calculate no. of leap years
    Returns:
        numLeapYearsUntilDate: int
            No. of leap years passed until the `date`
    """
    logger.debug(f"Counting no. of leap years until date: {date}")
    numLeapYearsUntilDate = 0
    year = date.year

    if date.month.value <= 2:
        year -= 1

    numLeapYearsUntilDate = year // 4
    numLeapYearsUntilDate -= year // 100
    numLeapYearsUntilDate += year // 400

    logger.debug(f"No. of leap years until date: {date}: {numLeapYearsUntilDate}")
    return numLeapYearsUntilDate


def getDefaultDaysInMonth(month: MONTH) -> int:
    """Returns no. of default days in a month without considering a leap year
    Parameters:
        month: MONTH
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


def getActualDaysInMonth(month: MONTH, year: int) -> int:
    """Returns no. of actual days in a month with considering a leap year

    Makes use of `getDefaultDaysInMonth`

    Parameters:
        month: MONTH
            month for which actual days is required
        year: int
            Year in which no. of days is required for `month`
    Returns:
        numDays : int
            No. of days in given month `month`
    """
    if month is MONTH.FEBRUARY:
        if isLeapYear(year):
            return 29
        else:
            return getDefaultDaysInMonth(month)
    else:
        return getDefaultDaysInMonth(month)


def numDaysBetweenDates(baseDate: Date, actualDate: Date) -> int:
    """Returns difference of days between two dates

    Makes use of `getDefaultDaysInMonth`, `countLeapYears`

    Parameters:
        baseDate: Date
            Base date from which difference needs to be calculated

        actualDate: Date
            Actual date upto which difference needs to be calculated
    Returns:
        numDays : int
            Difference of days between `totalDaysActualDate` `totalDaysBaseDate`
    """
    logger.debug(f"Counting diff of days between: {baseDate} and {actualDate}")

    def calculateAbsoluteDays(date: Date) -> int:
        """Returns no. of absolute days since begining until `date`

        Makes use of `getDefaultDaysInMonth`, `countLeapYears`

        Parameters:
            date: Date
                Date for which absolute no. of days needs to be calculated
        Returns:
            numDays : int
                No. of days since begining until `date`
        """
        totalDays = date.year * 365 + date.day
        for i in range(1, date.month.value):
            totalDays += getDefaultDaysInMonth(MONTH._value2member_map_[i])

        totalDays += countLeapYears(date)
        return totalDays

    totalDaysBaseDate = calculateAbsoluteDays(baseDate)
    totalDaysActualDate = calculateAbsoluteDays(actualDate)

    logger.debug(f"Diff of days between: {baseDate} and {actualDate} = {totalDaysActualDate - totalDaysBaseDate}")
    return totalDaysActualDate - totalDaysBaseDate


def dateValidator(date: str, pivotDate: Date) -> None:
    """Validates a string date to be accepted by the application

    Parameters:
        date: str
            Date that needs to be validated

        pivotDate: Date
            Minimum possible date supported by the application
    Raises:
        InvalidDateFormat
            If the passed `date` fails the validations test(s)
    """
    logger.info(f"Validaing date: {date}")
    try:
        year, month, day = date.split("-")
    except Exception:
        logger.info(f"Failed to fetch year, month and/or day information from string: {date}")
        raise InvalidDateFormat(f"String {date} doesn't contain enough separators to specify year, month and day")

    try:
        year, month, day = float(year), float(month), float(day)
    except Exception:
        logger.info(f"Year and/or month and/or day of date: {date} is/are not numbers")
        raise InvalidDateFormat(f"String {date} contains non-numeric values for year and/or month and/or day")

    if int(year) != year or int(month) != month or int(day) != day:
        logger.info(f"Year and/or month and/or day of date: {date} is/are not Integers")
        raise InvalidDateFormat(f"Year: {year} or month: {month} or day: {day} is/are not integer(s)")

    if month <= 0 or month > 12:
        logger.info(f"Month of date: {date} is not in range [1, 12]")
        raise InvalidDateFormat(f"Given month {month} isn't between [1, 12]")

    if day < 0 or day > 31:
        logger.info(f"Day of date: {date} is not in range [1, 31]")
        raise InvalidDateFormat(f"Given day: {day} isn't between [1, 31]")

    if month == 2:
        if isLeapYear(year):
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

    if numDaysBetweenDates(pivotDate, Date(date)) < 0:
        logger.info(f"Give: {date} is less than the pivot date: {pivotDate} and hence not supported")
        raise InvalidDateFormat(f"Given date: {date} should be greater or equal to {pivotDate}")
