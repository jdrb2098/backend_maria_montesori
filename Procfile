web: gunicorn backend_maria_montessori.wsgi --log-file -
web: python manage.py migrate && gunicorn backend_maria_montessori.wsgi