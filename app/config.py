# Configurations
from os import environ
host = ""
access_key = ""

class Config:
    ESTING = "" # environ["TESTING"]
    FLASK_DEBUG = "" # environ["FLASK_DEBUG"]
    SECRET_KEY = "" #  environ.get('SECRET_KEY')
    # Database
    SQLALCHEMY_DATABASE_URI = "" #  environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = "" #  environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")

