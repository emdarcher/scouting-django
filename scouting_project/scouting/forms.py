#forms for this app, very useful

from django import forms
from scouting.models import TeamData

class TeamDataForm(forms.ModelForm):
    #scouter_name = models.CharField
    

    class Meta:
        model = TeamData
        fields = '__all__'

