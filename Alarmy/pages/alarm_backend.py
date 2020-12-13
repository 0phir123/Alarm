import RPi.GPIO as GPIO #Use GPIO library
import time #Use time library
import vlc # for vlc alarm 
import smtplib # for send mail
import datetime # fpr time to mail send 
import os
from database.models import Database
from detect.models import Detect
from pages import config


# VARS FPOR SETUP
#GPIO.cleanup()
def initialConf():
    global ledPin, ledPin_2, pirPin, server, count_of_setups, count_of_detect
    GPIO.setwarnings(False)
    count_of_setups=0
    count_of_detect=0
    ledPin = 12
    ledPin_2 = 38
    pirPin = 11  # pin 7 is connected to output from the PIR motion sensor, 5V to pin 2, GND to pin 6
    #os.system("pulseaudio -k")
    #os.system("pulseaudio -D")
    #p = vlc.MediaPlayer("file:///path/to/track.mp3")

    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(ledPin, GPIO.OUT) #set the ledPin as output
    GPIO.output(ledPin, GPIO.LOW) # turn ininitally the led off
    GPIO.setup(ledPin_2, GPIO.OUT) #set the ledPin as output
    GPIO.output(ledPin_2, GPIO.LOW) # turn ininitally the led off
    GPIO.setup(pirPin, GPIO.IN); #set the pirPin as input
    time.sleep(5)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("ophiracyber@gmail.com", "Ophir1221")
    
   

def SentMail():
    
    
    subject = "Thief Detected"
    x = datetime.datetime.now()
    body = 'Alert is trigerd on {} please respond now.!'.format(x)

    msg = """\
    Subject: Alarm Thief Detected

    Time of the Alarm is {}.""".format(x)
    
    server.sendmail("ophiracyber@gmail.com", "ophirackerman@gmail.com", msg)
    

def playAlram():
    #opt = "--quiet"
    #vlc.Instance(opt)

    #os.system("omxplayer --no-keys -o local /home/djangoadmin/pyapps/Alarm_Project/Alarmy/pages/siren.mp3")
    #a = vlc.MediaPlayer("/home/pi/Downloads/siren.mp3")
    #a.play()
    SentMail()
    time.sleep(20)
    

#define alarm events
def soundAlarm(pirPin):
  #sound alarm (for 2 seconds )
  print("Sound Alarm")
  config.threat = True
  GPIO.output(ledPin, GPIO.HIGH)  # Turn led on
  GPIO.output(ledPin_2, GPIO.HIGH)  # Turn led_2 on
  playAlram()
  SentMail()
  detect = Detect()
  detect.save()
  time.sleep(2) # Pause for 2 seconds
  turnOffAlarm()  # Turn buzzer off
  time.sleep(30)
def turnOffAlarm():
  #turn off alarm

  GPIO.output(ledPin, GPIO.LOW)  # Turn led off
  GPIO.output(ledPin_2, GPIO.LOW) # Turn led 2 off

def clean_counters(detectC,setupsC):
    if detectC>10:
        Detect.objects.all().delete()
        config.threat = False
    else:
        pass
    if setupsC>100:
        Database.objects.all().delte()
    else:
        pass

#adding a callback function when the pir sensor output rises when motion is detected
def main():
    try:
        GPIO.cleanup()
    except:
        pass

    initialConf()
    GPIO.add_event_detect(pirPin, GPIO.RISING, callback=soundAlarm);


    #try catch block to perform GPIO cleanup
    try:
        while config.state:
            count_of_detect = Detect.objects.count()
            count_of_setups = Database.objects.count()
            clean_counters(count_of_detect, count_of_setups)
            time.sleep(5)
    except KeyboardInterrupt:
        print("You ended the program")
    finally:
        #clean up the GPIO pins
        GPIO.cleanup()

main()
