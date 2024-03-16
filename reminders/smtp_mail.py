from celery import shared_task
from celery.exceptions import MaxRetriesExceededError
from django.core.mail import send_mail
from django.conf import settings
from .models import Reminder

@shared_task(max_retries=3, default_retry_delay=600)
def send_reminder_mail(id):
    """ Sends email to the recipient and updates the Reminder status """
    try:
        reminder = Reminder.objects.get(id=id)
        subject = 'Reminder: It\'s Time'
        message = str(reminder.message)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [reminder.email]
        # Send mail using SMTP
        send_mail(subject, message, email_from, recipient_list)
        # Update Reminder Status 
        reminder.status = 'Completed'
        reminder.is_completed = True
        reminder.save()
    except MaxRetriesExceededError:
        # Handle max retries exceeded
        print("Max retries exceeded for send_reminder_mail task.")
