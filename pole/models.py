import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
	user_name = models.CharField(max_length=200)
	creation_date = models.DateTimeField('date created')
	ranking = models.IntegerField()

	def __str__(self):
		return self.user_name