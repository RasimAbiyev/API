from celery import shared_task
from django.core.mail import send_mail
from .models import Employee
from datetime import timedelta
from django.utils import timezone
from django.conf import settings
from celery.schedules import crontab

@shared_task
def send_notifications():
    cutoff_date = timezone.now() - timedelta(days=2)
    employees = Employee.objects.filter(created_at__lte=cutoff_date)
    
    for employee in employees:
        subject = 'Important Notification'
        message = (
            'Dear Employee,\n\n'
            'This is a reminder that you have not registered for more than 2 days. '
            'Please make sure to complete your registration at your earliest convenience.\n\n'
            'Best regards,\n'
            'The Team'
        )
        
        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                ["abiyev.rasim@gmail.com"],
                fail_silently=False,
            )
        except Exception as e:
            print(f"Failed to send email to {employee.email}: {str(e)}")