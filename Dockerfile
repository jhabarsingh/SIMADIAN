# https://testdriven.io/blog/deploying-django-to-heroku-with-docker/
# pull official base image
FROM python:3.8-alpine

RUN mkdir /code
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

# install pillow
RUN apk --update add \
    build-base \
    jpeg-dev \
    zlib-dev

COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code

# collect static files
#RUN python simadian/manage.py collectstatic --noinput

# add and run as non-root user
RUN adduser -D myuser
USER myuser

# run gunicorn
#CMD gunicorn hello_django.wsgi:application --bind 0.0.0.0:$PORT
