from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import reminder_model_serializers
from rest_framework import status
from .models import Reminder
from django.utils import timezone

#tasks
from .smtp_mail import send_reminder_mail
from .twilio_sms import send_reminder_sms


class reminder_operations(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request, format=None):
        serializer = reminder_model_serializers(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            time_to_remind = validated_data.get('time_to_remind')
            # checking if the time is less than current time 
            if time_to_remind < timezone.now():
                return Response({"error" : "time to remind is already over"}, status=status.HTTP_400_BAD_REQUEST)
            
            reminder = serializer.save()
            print("xcxc")
            eta_time = reminder.time_to_remind
            # schedule Send reminder to email 
            if reminder.email:
                send_reminder_mail.apply_async(args = [reminder.id], eta=eta_time) # scheduling send mail task at the specific time
            # schedule Send reimnder to phone 
            if reminder.phone:
                send_reminder_sms.apply_async(args =[reminder.id] , eta=eta_time) # scheduling send sms task at the specific time
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        reminder = Reminder.objects.all().order_by('-time_created')[:5]
        serializer = reminder_model_serializers(reminder,many=True)
        return Response(serializer.data)
    
    
# a sample test response
class test(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        return Response({"details":"server is up and responding"})
    
    
#     {
#     "phone": 1234567890,
#         "email": "example@example.com",
#         "time_to_remind": "2024-03-16T15:30:00",
#         "message": "dsdsdsdsd"
# }