#!/usr/bin/env bash

virtualenv /home/ubuntu/env
source /home/ubuntu/env/bin/activate
pip install -r /home/ubuntu/iwinghire/requirements.txt

cd /home/ubuntu/iwinghire
sudo mkdir ./static
python manage.py makemigrations 
python manage.py migrate 
python manage.py makemigrations     
python manage.py collectstatic

cd 