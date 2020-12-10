from database.models import Database
from detect.models import Detect
from pages import config
import time

def turnOnAlarm():
#Two vars of count for make the db clear after 1000 times of setups and 20 threat
        count_of_setups = 0
        count_of_detect = 0
        while(config.state):
          
            print ("alarm on")
         
            detect = Detect()
            detect.save()
            
            #Update the counters
            count_of_detect = Detect.objects.count()
            count_of_setups = Database.objects.count()
            clean_counters(count_of_detect,count_of_setups)

            time.sleep(5)



#Clean the Database of detects and setups
def clean_counters(detectsC,setupsC):
    if detectsC>10:
        Detect.objects.all().delete()
    else:
        pass
    if setupsC>100:
        Database.objects.all().delete()
    else:
        pass            

## dont forget to add function that check the db length and clear if neccseary
# by the command Database.object.all().delete()
# Count by Database.objects.count() 
# make count of 1000 for right possibler 
