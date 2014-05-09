import re

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from blog.models import *
from blog.forms import *


def homepage(request):

	getvideo = Videopost.objects.all()

	context = {'getvideo' : getvideo}
	return render(request, 'homepage.html', context)

def aboutpage(request):
	return render(request, 'about.html')

def resumepage(request):
	return render(request, 'resume.html')

def videopost(request, title):
	
	getvideo = get_object_or_404(Videopost, title=title)

	context = {'getvideo' : getvideo}
	return render(request, 'vidpost.html', context)

def addvideo(request):

	if request.method == "POST":
		form = VideoForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			post = form.cleaned_data['post']
			videoid = form.cleaned_data['videoid']
			form.save()
			return redirect('success/')

	else:
		form = VideoForm()
	return render(request, 'videoform.html', {'form' : form,})

def successpage(request):
	return render(request, 'successpage.html')