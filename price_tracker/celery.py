import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'price_tracker.settings')

app = Celery('tracker')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
