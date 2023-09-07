#!/bin/bash

rm db.sqlite3
rm -rf ./wilderwatch_api/migrations
python3 manage.py migrate
python3 manage.py makemigrations wilderwatch_api
python3 manage.py migrate wilderwatch_api
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata wilder_users
python3 manage.py loaddata regions
python3 manage.py loaddata studytypes
python3 manage.py loaddata studies
python3 manage.py loaddata observations