from django.core.management.base import BaseCommand
from sightings.models import Squirrel
import requests, csv, re, sys
from dateutil import parser
from datetime import date

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
            pattern = re.compile(r'(\d{2})(\d{2})(\d{4})')
            for item in data:
                i, j, k = pattern.match(item['Date']).groups()
                s = Squirrel(
                    X=item['X'],
                    Y=item['Y'],
                    Unique_Squirrel_ID=item['Unique Squirrel ID'],
                    #Hectare=item['Hectare'],
                    Shift=item['Shift'],
                    Date=date(int(k), int(i), int(j)),
                    #Hectare_Squirrel_Number=item['Hectare Squirrel Number'],
                    Age=item['Age'],
                    Primary_Fur_Color=item['Primary Fur Color'],
                    #Highlight_Fur_Color=item['Highlight Fur Color'],
                    #Combination_Fur=item['Combination of Primary and Highlight Color'],
                    #Color_Notes=item['Color Notes'],
                    Location=item['Location'],
                    Specific_Location=item['Specific Location'],
                    Running=item['Running'],
                    Chasing=item['Chasing'],
                    Climbing=item['Climbing'],
                    Eating=item['Eating'],
                    Foraging=item['Foraging'],
                    Other_Activities=item['Other Activities'],
                    Kuks=item['Kuks'],
                    Quaas=item['Quaas'],
                    Moans=item['Moans'],
                    Tail_Flags=item['Tail flags'],
                    Tail_Twitches=item['Tail twitches'],
                    Approaches=item['Approaches'],
                    Indifferent=item['Indifferent'],
                    Runs_From=item['Runs from'],
                    #Other_Interactions=item['Other Interactions'],
                    #Lat_Long=item['Lat/Long'],
                    #Zip_Codes=item['Zip Codes'],
                    #Community_Districts=item['Community Districts'],
                    #Borough_Boundaries=item['Borough Boundaries'],
                    #City_Council_Districts=item['City Council Districts'],
                    #Police_Precincts=item['Police Precincts'],

                )
                s.save()
