"""
Date    21th July 2024
@author Shreyali Ganvir

modules initialization script
"""

from flask import Flask, render_template
from flask_restful import Api
from .models import db, File, FileChunk
from .config import Config
from .routes import FileResource
from .database import initialize_db


def create_app() -> Flask:
    """
    function to create flask instance, add resource to API and initialize database
    :return:
    """

    flask_app = Flask(__name__)
    flask_app.config.from_object(Config)

    db.init_app(flask_app)
    initialize_db()
    try:
        with flask_app.app_context():
            db.create_all()
    except Exception as e:
        raise e
    api = Api(flask_app)
    # Add resources
    api.add_resource(FileResource, Config.ENDPOINT)

    return flask_app
