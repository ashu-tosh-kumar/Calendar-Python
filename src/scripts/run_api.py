import os

from src.config import config

if config.ENV in [
    "production",
]:
    print("Starting the application server")
    os.system("gunicorn --workers=4 --bind=0.0.0.0:8000 src.app:app")
else:
    print("Starting the application server")
    os.system("gunicorn --workers=4 --bind=0.0.0.0:8000 src.app:app --reload")
