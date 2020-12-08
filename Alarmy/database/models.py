from django.db import models
from datetime import datetime

# Create your models here.

class Database(models.Model):
   

    trigger = models.BooleanField(default=False)
    time = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return str(self.time)
    def get_trigger(self):
        return (self.trigger)