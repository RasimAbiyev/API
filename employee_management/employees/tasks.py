from celery import shared_task
from django.core.mail import send_mail
from .models import Employee
from datetime import timedelta
from django.utils import timezone

@shared_task
def send_notifications():
    cutoff_date = timezone.now() - timedelta(days=2)
    employees = Employee.objects.filter(created_at__lte=cutoff_date)
    for employee in employees:
        send_mail(
            'Notification',
            'You have not registered for more than 2 days.',
            'from@example.com',
            [employee.email],
            fail_silently=False,
        )