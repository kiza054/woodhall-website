release: python3 manage.py makemigrations
release: python3 manage.py migrate
web: gunicorn woodhall_website.wsgi
celery: celery -A woodhall_website.celery worker -l info
celerybeat: celery -A woodhall_website beat -l INFO