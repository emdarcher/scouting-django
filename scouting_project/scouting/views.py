from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

#got to import models 
from scouting.models import TeamData

#got to import the forms
from scouting.forms import TeamDataForm

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

def teamdata_table(request):

    #crates list with TeamData
    list_by_match = TeamData.objects.order_by('-match_number')[0:]

    #creates context
    context = {'list_by_match_context':list_by_match}

    return render(request, "scouting/teamdata_table.html", context)

def input(request):

    #context = RequestContext(request)

    if request.method == 'POST':
        form = TeamDataForm(request.POST)
        if form.is_valid():
            #put form processing stuff here
            scouter = form.cleaned_data.get('scouter_name')
            form.save(commit=True)
            
            return thanks(request, scouter)
        else:
            print form.errors

    else:
        form = TeamDataForm()

    return render(request, 'scouting/input.html',{ 'form' : form })
          

def thanks(request,name):
    #says thanks and asks if they want to enter again

    #context = RequestContext(request)

    return render(request, 'scouting/thanks.html', {'name': name})
