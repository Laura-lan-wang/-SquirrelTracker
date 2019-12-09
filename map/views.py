from django.shortcuts import render

from sightings.models import Squirrel

def map(request,*args,**kwargs):
    squirrel = Squirrel.objects.all()
    context={
        'Squirrel':squirrel
    }
    return render(request,'map/map.html',context)