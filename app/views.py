from django.shortcuts import render
import logging

# init logging
logger = logging.getLogger(__name__)
query_logger = logging.getLogger('query_logger')

def home(request, template='base.html'):
    return render(request, template, {}) 
