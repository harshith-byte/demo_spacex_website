FROM python:3.8-slim-buster

WORKDIR /app

#ADD . /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

RUN python3 manage.py makemigrations

RUN python3 manage.py migrate
