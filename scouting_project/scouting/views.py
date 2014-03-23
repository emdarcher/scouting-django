from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader

#got to import models 


# Create your views here.

def index(request):
    
    test_string = "Hello, I am a test string."
    
    context = {'test_string_context': test_string}

    return render(request, 'scouting/index.html', context) 
