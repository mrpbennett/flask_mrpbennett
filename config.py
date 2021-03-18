from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    SECRET_KEY = environ.get("SECRET_KEY")
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    CONTENTFUL_SPACE_ID = environ.get("CONTENTFUL_SPACE_ID")
    CONTENTFUL_ACCESS_TOKEN = environ.get("CONTENTFUL_ACCESS_TOKEN")

    # Freeze Flask
    FREEZER_RELATIVE_URLS = True
    FREEZER_IGNORE_404_NOT_FOUND = True


class ProdConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False
    DATABASE_URI = environ.get("PROD_DATABASE_URI")
    FREEZER_BASE_URL = ""


class DevConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
    DATABASE_URI = environ.get("DEV_DATABASE_URI")
    FREEZER_BASE_URL = "http://localhost"
