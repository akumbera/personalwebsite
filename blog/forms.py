from django.forms import ModelForm

from blog.models import Videopost

class VideoForm(ModelForm):
	class Meta:
		model = Videopost
		fields = ['title','post','videoid']