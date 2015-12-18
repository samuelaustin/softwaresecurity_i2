from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Message(models.Model):
    uid = models.ForeignKey(User)
    text = models.CharField(max_length=200)
    date = models.DateTimeField()