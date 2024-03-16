from django.urls import path, include
from . import views

urlpatterns = [  
    path('reminder/',views.reminder_operations.as_view()),
    path('test/',views.test.as_view())
    
]