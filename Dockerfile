FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /iwinghire
RUN pip3 install numpy==1.25.1
COPY requirements.txt .
RUN pip install --upgrade pip
RUN python -m venv .venv
RUN source .venv/bin/activate
RUN pip3 install numpy==1.25.1
RUN pip3 install -r requirements.txt
COPY . .
RUN python manage.py migrate
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000

