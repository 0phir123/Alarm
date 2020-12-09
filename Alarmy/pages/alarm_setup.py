from database.models import Database
from pages import config
import time

def turnOnAlarm():
        

        while(config.state):
          
            print (config.state)
            print ("alarm on")
            time.sleep(5)

## dont forget to add function that check the db length and clear if neccseary
# by the command Database.object.all().delete()
# Count by Database.objects.count() 
# make count of 1000 for right possibler 
