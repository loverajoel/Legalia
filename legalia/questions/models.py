from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
	question = models.TextField()
	description = models.TextField(blank=True)
	author = models.ForeignKey(User, related_name='questions')	
	pub_date = models.DateTimeField()

	def __unicode__(self):
		return self.question

class Answer(models.Model):
	question = models.ForeignKey(Question, related_name='answers')	
	body = models.TextField()
	author = models.ForeignKey(User, related_name='answers')	
	pub_date = models.DateTimeField()

	def __unicode__(self):
		return self.body
