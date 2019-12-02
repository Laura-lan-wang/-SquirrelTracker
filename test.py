import csv
from .sightings.models import Squirrel
path = '../'
with open(path) as f:
    reader = csv.reader(f)
    i=0
    column0 = [row[0] for row in reader]
    column1 = [row[1] for row in reader]
    for row in reader:
        _, created = Squirrel.objects.get_or_create(
            X=column0[i],
            Y=column1[i],
            i=i+1
        )