import logging

from constants import DAY, MONTH, PIVOT_DATE, PIVOT_DAY, Date
from utils import dateValidator, getActualDaysInMonth, numDaysBetweenDates

logger = logging.getLogger(__name__)


def getDateMatrix(date: str) -> list[list]:  # Format: "YYYY-MM-DD"
    """ Computes the date matrix for a given date
    Parameters:
        date: str
            Date for which calendar is required
    Returns:
        dateMatrix: list[list]
            Returns a list of list representing 7*6 calendar for the month as per `date`
    """
    logger.info(f"Computing date matrix for: {date}")

    # Validation on date passed by user
    dateValidator(date, PIVOT_DATE)

    dateObj = Date(date)  # Convert into application specific Date object
    dateObj.day = 1
    diffDaysFromPivotDate = numDaysBetweenDates(PIVOT_DATE, dateObj)
    currDay = DAY._value2member_map_[
        (PIVOT_DAY.value + diffDaysFromPivotDate) % 7]

    #   S  M  T   W   T   F   S
    dateMatrix = [[None]*7 for _ in range(6)]

    # Fill the matrix
    # Fill the previous month
    idx = 0
    jdx = currDay.value - 1
    lastMonthDate = getActualDaysInMonth(
        MONTH._value2member_map_[dateObj.month.value - 1], dateObj.year)
    while jdx >= 0:
        dateMatrix[idx][jdx] = lastMonthDate
        lastMonthDate -= 1
        jdx -= 1

    # Fill the current month
    idx = 0
    jdx = currDay.value
    for day in range(1, getActualDaysInMonth(dateObj.month, dateObj.year) + 1):
        dateMatrix[idx][jdx] = day
        jdx += 1
        if jdx >= len(dateMatrix[0]):
            idx += 1
            jdx = 0

    # Fill the next month
    nextMonthDate = 1
    while idx < len(dateMatrix):
        dateMatrix[idx][jdx] = nextMonthDate
        nextMonthDate += 1
        jdx += 1
        if jdx >= len(dateMatrix[0]):
            idx += 1
            jdx = 0

    logger.info(f"Date matrix for date: {dateObj} is: {dateMatrix}")
    return dateMatrix
