"""Default configuration

Use env var to override
"""
import os

ENV = os.getenv("FLASK_ENV")
DEBUG = ENV == "development"
SECRET_KEY = os.getenv("SECRET_KEY")

MONGODB_SETTINGS = [{
        "db": "citizen_feedback",
        "host": os.getenv("DATABASE_HOST"),
        "port": os.getenv("DATABASE_PORT"),
        "username": os.getenv("DATABASE_USERNAME"),
        "password": os.getenv("DATABASE_PASSWORD"),
        "alias": os.getenv("DATABASE_ALIAS", "default"),
}]

UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
