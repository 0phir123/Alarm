from django.shortcuts import render, redirect
from django.http import HttpResponse
from database.models import Database
from .alarm_setup import turnOnAlarm
from pages import config
from django.contrib.auth.models import User
from django.contrib import messages, auth
# Create your views here.
a = 0 #a == 0 if user is autenticate


def setup(request):
    print ( request.user.is_authenticated)
    if request.method == 'POST':
        if  request.user.is_authenticated:
            trigger =  ("this is the option and it set to {}".format((request.POST['switch'])))
            time  = ("this is the password {}".format((request.POST["pass"])))
            if "ON" in trigger:
                database = Database(trigger=True)
                database.save()
                config.state = True
                turnOnAlarm()
                
            if "OFF" in trigger:
                database = Database(trigger=False)
                database.save()
                config.state = False
        else:
            messages.error(request, 'First Log in to the System')
            return redirect('login') 

    return render(request, 'pages/setup.html')
def index(request):
    return render(request, 'pages/index.html')