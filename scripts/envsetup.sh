#!/bin/bash

sudo apt install nginx -y

sudo apt install -y python3-venv

python3 -m venv env

source /home/ubuntu/env/bin/activate

pip install django gunicorn

pip install gunicorn

cd iwinghire

pip install -r requirements.txt

sudo service nginx stop

sudo service nginx start

sudo service nginx status