from django.db import models
from django.core.urlresolvers import reverse
from django.forms import ModelForm

# Create your models here.

class Videopost(models.Model):
	title = models.CharField(unique=True, max_length=255)
	post = models.TextField()
	videoid = models.CharField(max_length=255)

	def __unicode__(self):
		return u'%s'% self.title

	def get_absolute_url(self):
		return reverse('blog.views.videopost', args=[self.title])

#class VideoForm(ModelForm):
#	class Meta:
#		model = Videopost
#		fields = ['title','post','videoid']