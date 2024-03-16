from rest_framework import serializers
from .models import Reminder
from datetime import datetime, timedelta
from django.utils.timezone import make_aware

class reminder_model_serializers(serializers.ModelSerializer):
    remaining_time = serializers.SerializerMethodField()
    
    class Meta:
        """
        Information about the Model and fields.
        """
        model = Reminder
        fields = '__all__'
        
    def get_remaining_time(self, obj):
        """
        Calculate and return the remaining time for the reminder.
        """
        
        current_time = datetime.now()
        time_to_remind = obj.time_to_remind
        current_time_aware = make_aware(current_time, timezone=obj.time_to_remind.tzinfo)
        if time_to_remind >= current_time_aware:
            # Assuming time_to_remind is in the future
            remaining_time = time_to_remind - current_time_aware
        else:
            # if the time_to_remind is over
            remaining_time = 0
        return remaining_time
