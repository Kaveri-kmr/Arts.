from django.db import models

# Create your models here.

class Events(models.Model):
    event_name=models.CharField(max_length=200)

    event_venue=models.CharField(max_length=200)

    def __str__(self):
        return self.event_name+':'+self.event_venue

class participants(models.Model):
    name=models.CharField(max_length=30, blank=False)
    gender=models.CharField(max_length=10, blank=False)
    year=models.IntegerField()
    team_name=models.CharField(max_length=100,blank=False)
