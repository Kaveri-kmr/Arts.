from django.shortcuts import render
from django.http import HttpResponse
from .models import Events

# Create your views here.


def registration(request):
    Event = Events.objects.all()
    context = {}
    context['Event'] = Event
    return render(request, 'registration.html', context)
