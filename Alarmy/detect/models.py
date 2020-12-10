from django.db import models
from datetime import datetime

# Create your models here.

class Detect(models.Model):
   

    time = models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return str(self.time)
   