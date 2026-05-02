# syntax=docker/dockerfile:1
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY web_app/ ./web_app
WORKDIR /app/web_app

# Sécurité : s'assurer que le dossier staticfiles existe pour WhiteNoise
RUN mkdir -p /app/web_app/staticfiles
RUN python manage.py collectstatic --noinput

CMD ["sh", "-c", "gunicorn static_site.wsgi:application --bind 0.0.0.0:${PORT:-10000}"]
