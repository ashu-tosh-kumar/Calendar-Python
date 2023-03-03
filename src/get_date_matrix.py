from src import constants, utils
from src.initializer import logger


def get_date_matrix(date: str) -> list[list]:
    """Computes the date matrix for a given date

    NOTE: We can use `dateutil` library to parse the date efficiently but the objective
    here is to use minimal libraries and showcase the project

    Args:
        date (str): Date (Format: "YYYY-MM-DD") for which calendar is required

    Returns:
        list[list]: Returns a list of list representing 7*6 calendar for the month as per `date`
    """
    logger.info(f"Computing date matrix for: {date}")

    # Validation on date passed by user
    utils.date_validator(date, constants.PIVOT_DATE)

    date_obj = constants.Date(date)  # Convert into application specific Date object
    date_obj.day = 1
    diff_days_from_pivot_date = utils.num_days_between_dates(constants.PIVOT_DATE, date_obj)
    curr_day = constants.DAY._value2member_map_[(constants.PIVOT_DAY.value + diff_days_from_pivot_date) % 7]

    #   S  M  T   W   T   F   S
    date_matrix = [[0] * 7 for _ in range(6)]

    # Fill the matrix
    # Fill the previous month
    idx = 0
    jdx = curr_day.value - 1
    last_month_date = utils.get_actual_days_in_month(constants.MONTH._value2member_map_[date_obj.month.value - 1], date_obj.year)
    while jdx >= 0:
        date_matrix[idx][jdx] = last_month_date
        last_month_date -= 1
        jdx -= 1

    # Fill the current month
    idx = 0
    jdx = curr_day.value
    this_month_date = utils.get_actual_days_in_month(date_obj.month, date_obj.year)
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
