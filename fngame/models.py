from django.db import models
from django.contrib.auth.models import User,auth

# Create your models here.
class ghostscore(models.Model):
    username = models.CharField(max_length=30)
    score = models.IntegerField()

class breakscore(models.Model):
    username = models.CharField(max_length=30)
    score = models.IntegerField()
