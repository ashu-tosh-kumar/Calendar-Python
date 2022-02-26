from email.mime import base

from constants import DAY, MONTH, PIVOT_DATE, PIVOT_DAY, numDaysBetweenDates
from exceptions import InvalidDateFormat
from utils import Date, getDaysInMonth


def getDateMatrix(date: str) -> list[list]:  # Format: "YYYY-MM-DD"
    """ Computes the date matrix for a given date
    Parameters:
        date: str
            Date for which calendar is required
    Returns:
        dateMatrix: tuple(json, int)
            Returns the tuple of json response and status code
    """
    pass
