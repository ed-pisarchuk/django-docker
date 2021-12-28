FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1
ENV KAGGLE_USERNAME elenapisarchuk
ENV KAGGLE_KEY 8aeb4349c11ce52895269c8f1ae9eb61
ENV DJANGO_SUPERUSER_PASSWORD 123456
ENV DJANGO_SUPERUSER_EMAIL admin@mail.ru
ENV DJANGO_SUPERUSER_USERNAME admin

RUN pip install --upgrade pip && \
    pip install --no-cache-dir poetry

WORKDIR /usr/src/app
COPY .  /usr/src/app/

RUN poetry install
RUN poetry run python manage.py migrate
RUN poetry run python manage.py createsuperuser --noinput \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL
CMD poetry run python manage.py runserver 0.0.0.0:8000