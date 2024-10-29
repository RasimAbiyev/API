# employee_management/celery.py

import os
from celery import Celery

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_management.settings')

# Create the Celery application instance
app = Celery('employee_management')
app.conf.broker_connection_retry_on_startup = True

# Load configuration from Django settings, using a namespace
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover tasks in Django applications
app.autodiscover_tasks()