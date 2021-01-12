from django import forms

from .models import registration,Events



class RegForm(forms.ModelForm):

    class Meta:
        model = registration
        fields = ('name','gender','year','branch','division','team_name','Events')
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'year':forms.Select(attrs={'class':'form-control'}),
            'branch':forms.Select(attrs={'class':'form-control'}),
            'divisiom':forms.Select(attrs={'class':'form-control'}),
            'team_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your team name'}),
            # 'Events':forms.ModelMultipleChoiceField(queryset=Events.objects.all()),
        }