import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()


class Config:
    # Read .env variables
    POSTGRES_ENDPOINT = os.getenv("POSTGRES_ENDPOINT")
    POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    HOST = os.getenv("HOST")
    DB_PORT = int(os.getenv("DB_PORT"))
    PORT = int(os.getenv("PORT"))
    ENDPOINT = os.getenv("ENDPOINT")
    OUT_DIR = os.getenv("OUT_DIR")

    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}/{}'.format(POSTGRES_USER,
    #                                                                      POSTGRES_PASSWORD,
    #                                                                      POSTGRES_ENDPOINT,
    #                                                                      POSTGRES_DATABASE)
    SQLALCHEMY_DATABASE_URI = os.getenv("URI")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
