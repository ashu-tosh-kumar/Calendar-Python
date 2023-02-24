import json
import logging
from typing import Tuple

from flask import Flask

from src.exceptions import InvalidDateFormat
from src.model import get_date_matrix

logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Welcome to Calendar App. Please visit url: 'hostname:port/date' to try it."


@app.route("/<date>", methods=["GET"])
def date(date: str) -> Tuple[str, int]:  # Format: "YYYY-MM-DD"
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
        date_matrix = get_date_matrix(date)
        return json.dumps(date_matrix), 200
    except InvalidDateFormat as e:
        logger.info("Date validation failed", exc_info=True)
        return str(e), 400
    except Exception:
        logger.exception("Server side error. Please reach out to support team for help")
        return "Server side issue", 500


if __name__ == "__main__":
    port = 8080
    app.run(port=port)
