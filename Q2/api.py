"""
Date    21st July 2024
@author Shreyali Ganvir

n3 hub Challenge Devops / Python Developer
Q2- Python script to create miniRestAPI application
"""

from app import create_app
from app.config import Config


if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(host=Config.HOST, port=Config.PORT)
