from django.db import models

# Create your models here.

class TeamData(models.Model):
    
    scouter_name = models.CharField(default="unidentified scouter", max_length=32) #name must be less than 32 characters

    match_number = models.PositiveIntegerField(default=0) #should be made sure to be filled!

    team_number = models.PositiveIntegerField(default=10000001) #stores team's number, MUST BE FILLED IN! if not, it will default to 10000001 (probably won't exist for a while)
    
    #general points and count stuff
    catches = models.PositiveIntegerField(default=0)
    truss = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    auto_points = models.PositiveIntegerField(default=0)
    teleop_points = models.PositiveIntegerField(default=0)

    #ideally total points will be calculated by the program by
    #adding together the values of auto_points & teleop_points
    #will figure that out later O.o
    total_points = models.PositiveIntegerField(default=0)
    
    
    #comments and stuff
    comments = models.TextField(default="No Comments in Entry")

    
    
     
