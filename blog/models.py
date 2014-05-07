from django.db import models

# Create your models here.

class videopost(models.Model):
	title = models.CharField()
	post = models.TextField()
	videoid = models.CharField()