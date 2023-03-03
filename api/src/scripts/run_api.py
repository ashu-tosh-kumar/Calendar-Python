import os

from api.src.config import config

if config.ENV in [
    "production",
]:
    print("Starting the application server")
    os.system("gunicorn --workers=4 --bind=0.0.0.0:8000 api.src.api:flask_app")
else:
    print("Starting the application server")
    os.system("gunicorn --workers=4 --bind=0.0.0.0:8000 api.src.api:flask_app --reload")
