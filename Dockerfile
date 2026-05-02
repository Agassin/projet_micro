# syntax=docker/dockerfile:1
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements-dev.txt .
RUN python -m pip install --upgrade pip \
    && pip install -r requirements-dev.txt gunicorn

COPY web_app/ ./web_app
WORKDIR /app/web_app

RUN python manage.py collectstatic --noinput

EXPOSE 10000
CMD gunicorn static_site.wsgi:application --bind 0.0.0.0:$PORT
