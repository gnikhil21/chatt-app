from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    room = models.CharField(max_length=1000)

class Message(models.Model):
    msg = models.CharField(max_length=1000000)
    time = models.TimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)