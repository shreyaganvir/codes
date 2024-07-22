import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}/{}'.format(os.getenv("DB_USER"),
                                                                   os.getenv("DB_PASSWORD"),
                                                                   os.getenv("DB_PORT"),
                                                                   os.getenv("DB_NAME"))
    # SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(os.getenv("DB_USER"),
    #                                                                os.getenv("DB_PASSWORD"),
    #                                                                os.getenv("HOST"),
    #                                                                os.getenv("DB_PORT"),
    #                                                                os.getenv("DB_NAME"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Read .env variables
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    HOST = os.getenv("HOST")
    DB_PORT = int(os.getenv("DB_PORT"))
    PORT = int(os.getenv("PORT"))
    ENDPOINT = os.getenv("ENDPOINT")
    OUT_DIR = os.getenv("OUT_DIR")

