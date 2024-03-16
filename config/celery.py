import os
from celery import Celery
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()
from django.conf import settings

# import tasks for celery
from reminders.smtp_mail import send_reminder_mail
from reminders.twilio_sms import send_reminder_sms

app = Celery("config")

broker_connection_retry_on_startup = True

app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings,namespace='CELERY')

# app.conf.update(
#     task_soft_time_limit=600,
#     task_time_limit=1200,
# )

app.autodiscover_tasks()