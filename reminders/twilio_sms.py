from twilio.rest import Client
from celery.exceptions import MaxRetriesExceededError
from celery import shared_task
from .models import Reminder
from django.conf import settings

# Retrieve Twilio credentials from environment variables
account_sid = settings.TWILIO_ACCOUNT_SID
auth_token = settings.TWILIO_AUTH_TOKEN
messaging_service_sid = settings.TWILIO_SERVICE_SID

if not all([account_sid, auth_token, messaging_service_sid]):
    raise ValueError("Twilio environment variables are not set correctly.")

@shared_task(max_retries=3, default_retry_delay=600)
def send_reminder_sms(id):
    """ sends sms to the phone number
    
    Args:
        id (int): id of the Reminder modal object
    """
    try:
        reminder = Reminder.objects.get(id = id)
        # Initialize Twilio client
        client = Client(account_sid, auth_token)
        # Send message using Twilio client
        message = client.messages.create(
            body='Reminder : Its Time ' + str(reminder.message),
            messaging_service_sid=messaging_service_sid,
            to='+91' + str(reminder.phone)
        )
        # update Reminder Status 
        reminder.status = 'Completed'
        reminder.is_completed = True
        reminder.save()
        print("Message SID:", message.sid)
    except MaxRetriesExceededError:
        # Handle max retries exceeded
        print("Max retries exceeded for send_reminder_sms task.")
