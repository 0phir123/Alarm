from database.models import Database
import time
def turnOnAlarm():
        state = 'True'
        print ("hele")
        while(state):
            state =  (Database.objects.all().last()).trigger
            #print (Database.objects.all().last()[0])
            print (state)
            print ("alarm on")
            time.sleep(5)

## dont forget to add function that check the db length and clear if neccseary
# by the command Database.object.all().delete()
# Count by Database.objects.count() 
# make count of 1000 for right possibler 
