#!/bin/bash

export FLASK_APP=app.py
export FLASK_ENV=production
export FLASK_RUN_PORT=5000
flask run --host=0.0.0.0 &> flask.log & exit
