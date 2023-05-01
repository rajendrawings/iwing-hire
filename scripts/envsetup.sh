#!/bin/bash

sudo apt install nginx -y

sudo apt install -y python3-venv

python3 -m venv env

source /home/ubuntu/env/bin/activate

pip install django gunicorn

pip install gunicorn

cd iwinghire

sudo mkdir ./static

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations

sudo apt-get install python3-dev default-libmysqlclient-dev build-essential

pip install mysqlclient

sudo service nginx stop

sudo service nginx start

sudo service nginx status