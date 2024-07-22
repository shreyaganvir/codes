import subprocess
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from .config import Config
import logging


def check_postgres_installed():
    try:
        subprocess.run(['psql', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return
    except (subprocess.CalledProcessError, FileNotFoundError):
        logging.error("Postgresql not installed. Please read requirements.txt for pre-requisites")
        return


def create_database():
    try:
        conn = psycopg2.connect(
            dbname='postgres',
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            host=Config.HOST,
            port=Config.DB_PORT
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    except Exception as e:
        raise e
    cursor = conn.cursor()
    cursor.execute(f"SELECT 1 FROM pg_database WHERE datname='{Config.DB_NAME}';")
    if not cursor.fetchone():
        cursor.execute(f'CREATE DATABASE {Config.DB_NAME};')
    else:
        logging.info(f"Database {Config.DB_NAME} already exists.")
    return


def initialize_db():
    if check_postgres_installed():
        create_database()

    return
