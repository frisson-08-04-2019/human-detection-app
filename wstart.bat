@echo off
set FLASK_APP=app.py
set FLASK_ENV=production
set FLASK_RUN_PORT=80
flask run --host=0.0.0.0 2> flask.log