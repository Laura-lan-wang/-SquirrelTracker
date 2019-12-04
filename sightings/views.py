from django.shortcuts import render
from django.http import HttpResponse
from .models import Squirrel
def show_map(request):
    #squirrels = Squirrel.objects.all()
    context = {
        'Squirrel': 1,
    }
    return render(request, 'map/map.html', context)

def index(request):

    return HttpResponse("Squirrel Tracker")





# Create your views here.
