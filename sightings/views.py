from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Squirrel
from .forms import SquirrelForm

def show_map(request):
    squirrel = Squirrel.objects.all()
    context = {
        'Squirrel': squirrel,
    }
    return render(request, 'map/map.html', context)



# def index(request):
#
#     return HttpResponse("Squirrel Tracker")

def all_squirrel(request):
    squirrel = Squirrel.objects.all()
    context = {
        'Squirrel': squirrel,
    }
    return render(request, 'sightings/all.html', context)


def edit_squirrel(request, sq_ID):
    squirrel = Squirrel.objects.get(Unique_Squirrel_ID=sq_ID)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=squirrel)
        # check data with form
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{sq_ID}')
    else:
        form = SquirrelForm(instance=squirrel)

    context = {
        'form': form,
        'sq_ID':sq_ID,

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


def show_stats(request):
    squirrel = Squirrel.objects.all()
    total_squirrel = Squirrel.objects.count()
    above_ground = Squirrel.objects.filter(Location='Above Ground').count()
    cinnamon = Squirrel.objects.filter(Primary_Fur_Color='Cinnamon').count()
    adult = Squirrel.objects.filter(Age='Adult').count()
    shift = Squirrel.objects.filter(Shift='AM').count()
    context = {
        'total_squirrel': total_squirrel,
        'above_ground': above_ground,
        'cinnamon': cinnamon,
        'adult': adult,
        'shift': shift,
        'Squirrel': squirrel,
    }

    return render(request, 'sightings/stats.html', context)
