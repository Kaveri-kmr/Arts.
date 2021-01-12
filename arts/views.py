from django.shortcuts import render
from django.http import HttpResponse
from .models import Events
from .models import registration
from .forms import RegForm
# Create your views here.


def eventdetails(request):
    Event = Events.objects.all()
    context = {}
    context['Event'] = Event
    return render(request, 'eventdetails.html', context)

def list_of_participants(request):
    reg= registration.objects.all()
    context={}
    context['reg']=reg
    return render(request, 'listofstudents.html',context)
    

def registration_details(request):
    reg= registration.objects.all()
    context={}
    context['reg']=reg
    if request.POST:
        form = RegForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return HttpResponse("Registration sucessfull")
        else:
            form = RegForm()
            context['form'] = form
    else:
        form = RegForm(
            initial={
                'name': '',
                # 'description': ''
            }
        )
        context['form'] = form
    return render(request,'reg.html',context)