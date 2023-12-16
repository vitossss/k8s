#!/bin/bash

# while ! make migrate  2>&1; do
#    echo "Migration is in progress status"
#    sleep 3
# done

# make run-server

echo "Waiting for postgres..."
    
    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.1
    done
    
    echo "PostgreSQL started"

python manage.py migrate --noinput

exec "$@"