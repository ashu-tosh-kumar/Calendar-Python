import logging

from src.constants import DAY, MONTH, PIVOT_DATE, PIVOT_DAY, Date
from src.utils import date_validator, get_actual_days_in_month, num_days_between_dates

logger = logging.getLogger(__name__)


def get_date_matrix(date: str) -> list[list]:  # Format: "YYYY-MM-DD"
    """Computes the date matrix for a given date
    Parameters:
        date: str
            Date for which calendar is required
    Returns:
        date_matrix: list[list]
            Returns a list of list representing 7*6 calendar for the month as per `date`
    """
    logger.info(f"Computing date matrix for: {date}")

    # Validation on date passed by user
    date_validator(date, PIVOT_DATE)

    date_obj = Date(date)  # Convert into application specific Date object
    date_obj.day = 1
    diff_days_from_pivot_date = num_days_between_dates(PIVOT_DATE, date_obj)
    curr_day = DAY._value2member_map_[(PIVOT_DAY.value + diff_days_from_pivot_date) % 7]

    #   S  M  T   W   T   F   S
    date_matrix = [[0] * 7 for _ in range(6)]

    # Fill the matrix
    # Fill the previous month
    idx = 0
    jdx = curr_day.value - 1
    last_month_date = get_actual_days_in_month(MONTH._value2member_map_[date_obj.month.value - 1], date_obj.year)
    while jdx >= 0:
        date_matrix[idx][jdx] = last_month_date
        last_month_date -= 1
        jdx -= 1

    # Fill the current month
    idx = 0
    jdx = curr_day.value
    this_month_date = get_actual_days_in_month(date_obj.month, date_obj.year)
    for day in range(1, this_month_date + 1):
        date_matrix[idx][jdx] = day
        jdx += 1
        if jdx >= len(date_matrix[0]):
            idx += 1
            jdx = 0

    # Fill the next month
    next_month_date = 1
    while idx < len(date_matrix):
        date_matrix[idx][jdx] = next_month_date
        next_month_date += 1
        jdx += 1
        if jdx >= len(date_matrix[0]):
            idx += 1
            jdx = 0

    logger.info(f"Date matrix for date: {date_obj} is: {date_matrix}")
    return date_matrix
