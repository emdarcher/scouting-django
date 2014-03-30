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
            #form.save(commit=True)
            #add stuff to deal with the total_points part of the model
            total = (form.cleaned_data.get('auto_points')) + (form.cleaned_data.get('teleop_points'))
            part_form = form.save(commit=False)
            part_form.total_points = total            
            part_form.save()

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

def team(request,team_number_url):

    #context = RequestContext(request)
     
        

    context_dict = {'team_number_url' : team_number_url}
    
    #stuff to sort and get the teams match data to the page
    list_by_match = TeamData.objects.order_by('-match_number')[0:]
    
    #relevant_matches = []
    relevant_matches = TeamData.objects.filter(team_number = team_number_url)
    

    #for match in list_by_match:
    #    #
    #    #find related matches
    #     if match.team_number == team_number_url:
    #        relevant_matches.append(match)
    #    
    #    ##remove unrelated matches
    #    #if match.team_number != team_number_url:
    #    #    del relevant_matches[match] 

       
    context_dict['relevant_matches'] = relevant_matches


    #try:
    #    #try to find team with given number
    #    # if we can't the .get() method raises a DoesNotExist exception.
    #    teamnum = TeamData.objects.get(team_number = team_number_url)
    # 
    #    #used to verify team exists
    #    context_dict['teamnum'] = teamnum

    #except TeamData.DoesNotExist:
    #    #if we did not find it template witll display "no team found"
    #
    #    pass

    return render(request, 'scouting/team.html', context_dict)




