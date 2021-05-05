from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField

# Create your models here.

class Session(models.Model):
	session_id = models.IntegerField()
	count_message = models.IntegerField(default=0,)
	starting_user = models.CharField(max_length=25)
	ending_user = models.CharField(max_length=25)
	saltbae = models.CharField(max_length=5)
	messages = JSONField()