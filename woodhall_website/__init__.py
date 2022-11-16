# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from woodhall_website.celery import app as woodhall_website_celery

__all__ = ('woodhall_website_celery',)