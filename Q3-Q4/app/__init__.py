"""
Date    21th July 2024
@author Shreyali Ganvir

modules initialization script
"""

from flask import Flask
import os
from flask_restful import Api
from .models import db
from .config import Config
from .routes import FileResource
from flask import current_app
from flask.cli import with_appcontext
from flask_migrate import Migrate


def create_app() -> Flask:
    """
    function to create flask instance, add resource to API and initialize database
    :return:
    """

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    @app.cli.command('resetdb')
    def resetdb_command():
        """
        function: Destroys and creates the database + tables when resetdb command is provided in flask
        :return None
        """
        sqlalchemy_db_uri = os.getenv("URI")
        #sqlalchemy_db_uri = current_app.config["SQLALCHEMY_DATABASE_URI"]
        print("DB_URL : " + str(sqlalchemy_db_uri))

        from sqlalchemy_utils import database_exists, create_database
        if database_exists(sqlalchemy_db_uri):
            print('Deleting database.')
        if not database_exists(sqlalchemy_db_uri):
            print('Creating database.')
            create_database(sqlalchemy_db_uri)

        db.drop_all()
        print('Creating tables.')

        return

    Migrate(app, db)
    try:
        with app.app_context():
            db.create_all()
    except Exception as e:
        raise e
    api = Api(app)
    # Add resources
    api.add_resource(FileResource, Config.ENDPOINT)

    return app
