from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Squirrel
from .forms import SquirrelForm

def show_map(request):
    #squirrels = Squirrel.objects.all()
    context = {
        'Squirrel': 1,
    }
    return render(request, 'map/map.html', context)

# def index(request):
#
#     return HttpResponse("Squirrel Tracker")

def all_squirrel(request):
    Squirrel = Squirrel.objects.all()
    context = {
        'Squirrel': Squirrel,
    }
    return render(request, 'sightings/all.html', context)


def edit_squirrel(request, Unique_Squirrel_ID):
    Squirrel = Squirrel.objects.get(id=Unique_Squirrel_ID)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=Squirrel)
        # check data with form
        if form.is_valid():
            form.save()
            return redirect(f'/adopt/{Unique_Squirrel_ID}')
    else:
        form = SquirrelForm(instance=Squirrel)

    context = {
        'form': form,
    }

    return render(request, 'sightings/edit.html', context)

def add_squirrel(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        # check data with form
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')
    else:
        form = SquirrelForm()

    context = {
        'form': form,
    }

    return render(request, 'sightings/edit.html', context)

