import re

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from blog.models import *


def homepage(request):
	videoid = 'vAX902tSXkg'
	return render(request, 'homepage.html', {'videoid': videoid})

def aboutpage(request):
	return render(request, 'about.html')

def resumepage(request):
	return render(request, 'resume.html')