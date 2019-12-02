from django.shortcuts import render
from django.http import HttpResponse
def show_map(request):
    context = {
        'Squirrel': 1,
    }
    return render(request, 'map/map.html', context)

def index(request):

    return HttpResponse("Squirrel Tracker")





# Create your views here.
