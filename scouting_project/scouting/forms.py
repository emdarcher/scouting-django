#forms for this app, very useful

from django import forms
from scouting.models import TeamData

class TeamDataForm(forms.ModelForm):
    scouter_name = forms.CharField(max_length=32, help_text="Please enter your name")
    match_number = forms.IntegerField(help_text="enter Match Number",required=True)
    team_number = forms.IntegerField(help_text="enter team number",required=True)
    catches = forms.IntegerField(help_text="enter amount of catches",required=True)
    truss = forms.IntegerField(help_text="enter number of truss shots", required = True) 
    assists = forms.IntegerField(help_text="enter number of assists", required=True)
    
    auto_points = forms.IntegerField(help_text="enter total autonomous points", required=True)
    teleop_points = forms.IntegerField(help_text="enter total tele-op points", required=True)
    
    #make it hidden
    total_points = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    #total_points = forms.IntegerField(help_text = "enter total points scored by robot, auto points plus tele-op points", required=True)

    comments = forms.CharField(widget=forms.Textarea,help_text="Enter comments or stategy notes below:", required=False)


    class Meta:
        model = TeamData
        fields = '__all__'
        #exclude the total_points field, this means we must set it in the view
        #exclude = ['total_points']
