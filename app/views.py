from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
import jsonlib2 as json
import traceback

def home(request, template='base.html'):
    return render(request, template, {}) 
