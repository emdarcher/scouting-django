from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader

#got to import models 
from scouting.models import TeamData

# Create your views here.

def index(request):
    
    test_string = "Hello, I am a test string."
    
        
    
    context = {'test_string_context': test_string}

    return render(request, 'scouting/index.html', context)

def teamdata_list(request):

    #creates a list with TeamData ordered by the match number 
    list_by_match = TeamData.objects.order_by('-match_number')[0:]

    #creates the context
    context = {'list_by_match_context':list_by_match}

    return render(request, "scouting/teamdata_list.html", context)


