from django.db import models
import datetime
# Create your models here.



class Events(models.Model):
    # event_id=models.PrimaryKey(default='000000',editable=False)
    event_name=models.CharField(max_length=200,blank=False)
    event_venue=models.CharField(max_length=200,blank=False)
    
    

    def __str__(self):
        return self.event_name+':'+self.event_venue



class registration(models.Model):
    name=models.CharField(max_length=100,blank=False)
    gender=models.CharField(max_length=20,choices=(
        ('Female','Female'),
        ('Male','Male'),
    ))
    year = models.CharField(max_length=35,choices=(
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd'),
        ('4th','4th'),
    ))
    branch=models.CharField(max_length=100,choices=(
        ('CS', 'CS'),
        ('EC','EC'),
        ('EEE','EEE'),
        ('EBE','EBE'),
    ))
    division=models.CharField(max_length=10,choices=(
        ('A','A'),
        ('B','B')
    ))
    team_name = models.CharField(max_length=100, blank=False)
    Events = models.ForeignKey(Events, default=1,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
# class participants(models.Model):
#     name=models.CharField(max_length=30, blank=False)
#     gender=models.CharField(max_length=10, blank=False)
#     year=models.IntegerField()
#     team_name=models.CharField(max_length=100,blank=False)

#     def __str__(self):
#         return self.name
