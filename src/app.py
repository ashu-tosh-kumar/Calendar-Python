import json

from src import exceptions, model
from src.initializer import app, logger


@app.route("/", methods=["GET"])
def home():
    return "Welcome to Calendar App. Please visit url: 'hostname:port/date' to try it."


@app.route("/health", methods=["GET"])
def health():
    return "Calendar App alive."


@app.route("/<date>", methods=["GET"])
def date(date: str) -> tuple[str, int]:  # Format: "YYYY-MM-DD"
    """Home route of the flask application
    Parameters:
        date: str
            Date for which calendar is required
    Returns:
        date_matrix: tuple(json, int)
            Returns the tuple of json response and status code
    """
    logger.info(f"GET call received to get date for: {date}")
    try:
        date_matrix = model.get_date_matrix(date)
        return json.dumps(date_matrix), 200
    except exceptions.InvalidDateFormat as e:
        logger.info("Date validation failed", exc_info=True)
        return str(e), 400
    except Exception:
        logger.exception("Server side error. Please reach out to support team for help")
        return "Server side issue", 500
