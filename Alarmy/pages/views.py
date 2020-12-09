from django.shortcuts import render
from django.http import HttpResponse
from database.models import Database
from .alarm_setup import turnOnAlarm
from pages import config
# Create your views here.
a = 0 #a == 0 if user is autenticate


def index(request):
    if request.method == 'POST':

        trigger =  ("this is the option and it set to {}".format((request.POST['switch'])))
        time  = ("this is the password {}".format((request.POST["pass"])))
        if a == 0 and "ON" in trigger:
            database = Database(trigger=True)
            database.save()
            config.state = True
            turnOnAlarm()
            
        if a == 0 and "OFF" in trigger:
            database = Database(trigger=False)
            database.save()
            config.state = False
            

    return render(request, 'pages/index.html')
def about(request):
    return render(request, 'pages/about.html')