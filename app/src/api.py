import json

from app.src import exceptions, get_date_matrix
from app.src.initializer import flask_app, logger


@flask_app.route("/", methods=["GET"])
def home() -> tuple[str, int]:
    """Home end point

    Returns:
        tuple[str, int]: Returns string message and status code
    """
    logger.debug("Home GET end point called")

    return "Welcome to Calendar App. Please visit url: 'hostname:port/date' to try it.", 200


@flask_app.route("/health", methods=["GET"])
def health() -> tuple[str, int]:
    """Health end point

    Returns:
        tuple[str, int]: Returns string message and status code
    """
    logger.debug("Health GET end point called")

    return "Calendar App alive.", 200


@flask_app.route("/date/<date>", methods=["GET"])
def date(date: str) -> tuple[str, int]:
    """Home route of the flask application

    Args:
        date (str): Date for which calendar is required

    Returns:
        tuple[str, int]: Returns the tuple of json response and status code
    """
    logger.info(f"GET call received to get date for: {date}")

    try:
        date_matrix = get_date_matrix.get_date_matrix(date)
        return json.dumps(date_matrix), 200
    except exceptions.InvalidDateFormat as e:
        logger.info("Date validation failed", exc_info=True)
        return str(e), 400
    except Exception:
        logger.exception("Server side error. Please reach out to support team for help")
        return "Server side issue", 500
