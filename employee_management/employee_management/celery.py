import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_management.settings')

app = Celery('employee_management')
app.conf.broker_connection_retry_on_startup = True
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()