import re

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from blog.models import *


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