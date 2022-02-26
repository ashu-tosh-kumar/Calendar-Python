from flask import Flask, jsonify

from exceptions import InvalidDateFormat
from model import getDateMatrix

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home(date: str) -> jsonify:  # Format: "YYYY-MM-DD"
    """ Home route of the flask application
    Parameters:
        date: str
            Date for which calendar is required
    Returns:
        dateMatrix: tuple(json, int)
            Returns the tuple of json response and status code
    """
    try:
        dateMatrix = getDateMatrix(date)
        return jsonify(dateMatrix), 200
    except InvalidDateFormat:
        return jsonify("Invalid date format passed. Accepted format: YYYY-MM-DD"), 400
    except:
        return jsonify("Server side issue"), 500


if __name__ == "__main__":
    port = 8080
    app.run(port=port)
