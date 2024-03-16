This web app does one thing and one thing well. It allows users to setup a reminder with a message. The JS developers have gone ahead and created a nice UI to accept date and time, to know when to send the message, and the actual text message to send. They have also given an option to select how to remind. Right now the app support reminding through SMS and Email. Going forward the app might support other ways to send the reminder. 

Clone the repositories install requirements and start the server

#for running the server
python manage.py runserver

#for clery
celery -A config worker --beat --loglevel=info

install redis docker image for message broker and check the configuration .

How to use

naviagte to http://127.0.0.1:8000/reminder/

give a post request with enough data to schedule the reminder

#sample data

{
    "phone": 808613XXXX,
    "email": "XXXXXX@gmail.com",
    "time_to_remind": "2024-03-16T16:05:00",
    "message": "Time to create the reminder"
}


now the reminder has been scheduled

![image](https://github.com/akashpmani/remind-me-later/assets/121414718/ae58166e-7359-4323-bbcd-508a269f7305)

![image](https://github.com/akashpmani/remind-me-later/assets/121414718/b14b4b62-f204-42e3-839f-8ef0cd2bdfe6)


Thankyou <3







