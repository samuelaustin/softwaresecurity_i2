from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    uid = models.ForeignKey(User)
    text = models.CharField(max_length=200)
    date = models.DateTimeField()