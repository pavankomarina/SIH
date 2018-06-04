from django.contrib.auth.models import Permission, User
from django.db import models
import datetime


class Userdetails(models.Model):
    user = models.ForeignKey(User, default=1,on_delete=models.CASCADE)
    audio_file=models.FileField()
