# Squirrel Tracker Web Application

Squirrel Tracker is a Web Application based on Django framework that can view, add and update squirrel data.

Squirrel Census Data 2018 is available at:
 <a href='https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv'>2018 Central Park Squirrel Census Data</a>

## Key Functionality

**Management Commands:

- Import: A command that can import the data from the 2018 census file. The file path needs to be specified at the command line after the name of the management command.
        
        $ python manage.py import_squirrel_data /path/to/file.csv
        
- Export: A command that can export the all squirrel data in CSV format. The file path needs be to specified at the command line after the name of the management command. 
        
        $ python manage.py import_squirrel_data /path/to/file.csv


**Map: 

Show all squirrel location on a map

    located at: map/

**Sightings: 

   - View: view all squirrel data. Each entry has its unique squirrel id, which can be redirected to edit the entry.
        
    located at: sightings/

   - Add: add squirrel entry

    located at: sightings/add/

   - Edit: edit a current squirrel data

    located at: sightings/<unique_squirrel_id>/


   - Statistics of Squirrel Data: Show general statistics of current data set

    located at: sightings/stats/

## Build with
Django 2.2.7

Python3

sqlite3

HTML

OpenStreetMap: https://www.openstreetmap.org/about/

## Group name and section
Project Group 15

Section 2

## Contributors
Laura Wang and Jueran Ren

UNIs: [lw2884, jr3982]

## Deployment

Link
https://neat-sunspot-255500.appspot.com



