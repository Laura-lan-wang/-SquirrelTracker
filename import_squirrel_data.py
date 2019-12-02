import csv
import os
from django.db import models
from sightings.models import Squirrel

with open(path) as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = Squirrel.objects.get_or_create(
            first_name=row[0],
            last_name=row[1],
            middle_name=row[2],
        )






