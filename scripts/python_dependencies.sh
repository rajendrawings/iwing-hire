#!/usr/bin/env bash

virtualenv /home/ubuntu/env
source /home/ubuntu/env/bin/activate
pip install -r /home/ubuntu/iwinghire/requirements.txt

python /home/ubuntu/iwinghire/manage.py makemigrations
python /home/ubuntu/iwinghire/manage.py migrate
python /home/ubuntu/iwinghire/manage.py makemigrations