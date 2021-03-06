from django.core.management.base import BaseCommand
from sightings.models import Squirrel
import csv

class Command(BaseCommand):
    help = 'exports all fields'

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file'], mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter = ',')
            all_fields = [f.name for f in Squirrel._meta.get_fields()]
            fieldnames = [Squirrel._meta.get_field(i).help_text for i in all_fields[1:]]
            writer.writerow(fieldnames)
            for j in range(len(Squirrel.objects.all())):
                rowval=list()
                for i in all_fields:
                    if i == 'id': continue
                    rowval.append(getattr(Squirrel.objects.all()[j],i))
                writer.writerow(rowval)
        csvfile.close