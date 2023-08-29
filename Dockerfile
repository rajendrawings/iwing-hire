FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /iwinghire

# Install necessary system packages for building numpy
RUN apt-get update && apt-get install -y libblas-dev liblapack-dev gfortran

# Install Python packages
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Rest of your Dockerfile...

COPY . .
RUN python manage.py migrate
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000
