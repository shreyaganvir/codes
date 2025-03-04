#!/usr/bin/env bash

set -e

echo "Reset DB!!"

flask resetdb

echo "Run flask app!!"
flask run --host=0.0.0.0 --port=5000
#gunicorn --bind 0.0.0.0:5000 app:create_app
