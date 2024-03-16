from django.db import models
from datetime import datetime, timedelta


class Reminder(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    )

    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    time_to_remind = models.DateTimeField()
    message = models.CharField(blank=True , null= True ,max_length = 1000)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    time_created = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'Reminder - {self.time_created}'



