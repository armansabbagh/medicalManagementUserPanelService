#!/bin/bash

port=$1
url="0.0.0.0"

echo "*** makemigrations && migrate ***"
python manage.py makemigrations
python manage.py migrate
echo "*** run test ***"
python manage.py test
echo "*** run server ***"
python manage.py runserver "$url":"$port"
