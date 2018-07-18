import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
	user_name = models.CharField(max_length=200)
	creation_date = models.DateTimeField('date created')
	ranking = models.IntegerField()

	def __str__(self):
		return self.user_name


class Change(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	from_rank = models.IntegerField()
	to_rank = models.IntegerField()
	creation_date = models.DateTimeField('date created')

	def __str__(self):
		return "{} of {} from {} to {}.".format(self.get_changeword('noun').capitalize(),self.user.user_name,
			self.from_rank,self.to_rank)

	def get_changeword(self,tense):
		move = self.to_rank-self.from_rank
		ind = int(((move/abs(move))+1)/2)
		tensedict = {
			'past':['promoted','demoted'],
			'future':['promote','demote'],
			'noun':['promotion','demotion'],
		}
		return tensedict[tense][ind]

