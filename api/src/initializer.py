# Module to initialize things for common use across the project like logging, database
# connection etc. It also helps in avoiding circular dependencies in the code

import logging

from flask import Flask

# ----------------------------------------------------------
# Logger setup
logger = logging.getLogger(__name__)

# ----------------------------------------------------------
# Flask application setup
flask_app = Flask(__name__)
