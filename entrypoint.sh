#!/bin/sh

# Exit if any subcommand fails
set -e

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Apply database migrations"
python manage.py migrate --noinput

gunicorn mirblog.wsgi:application --bind 0.0.0.0:8000
