"""Default configuration

Use env var to override
"""
import os

ENV = os.getenv("FLASK_ENV")
DEBUG = ENV == "development"
SECRET_KEY = os.getenv("SECRET_KEY")

MONGODB_SETTINGS = [{
        "db": os.getenv("DATABASE_NAME"),
        "host": f"{os.getenv('DATABASE_URL')}"
}]

UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
