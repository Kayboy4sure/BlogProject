from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    detail = models.CharField(max_length=100000)
    time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    username = models.CharField(max_length=100)
    msg_content = models.TextField()
    msg_time = models.DateTimeField(default=datetime.now, blank=True)
    room = models.PositiveIntegerField()

    def __str__(self):
        return self.msg_content
