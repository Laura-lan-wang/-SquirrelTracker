# Squirrel Tracker Web Application

Squirrel Tracker is a Web Application based on Django framework that can view, add and update squirrel data. Key functionality is listed in the next section. 

Squirrel Census Data 2018 is available at:
 <a href='https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv'>2018 Central Park Squirrel Census Data</a>
 
 ![Image of Squirrel](https://ichef.bbci.co.uk/news/976/cpsprodpb/D6E6/production/_109241055_mediaitem109241054.jpg)

## Key Functionality

**Management Commands:**

- Import: A command that can import the data from the 2018 census file. The file path needs to be specified at the command line after the name of the management command.
        
        $ python manage.py import_squirrel_data /path/to/file.csv
        
- Export: A command that can export the all squirrel data in CSV format. The file path needs be to specified at the command line after the name of the management command. 
        
        $ python manage.py import_squirrel_data /path/to/file.csv


**Map:**

 Displays the location of the squirrel sightings on an OpenStreets map

    located at: https://neat-sunspot-255500.appspot.com/map/

**Sightings:** 

 - View all: lists all squirrel sightings with links to edit each sighting
        
    located at: https://neat-sunspot-255500.appspot.com/sightings/

 - Add: create a new squirrel sighting

    located at: https://neat-sunspot-255500.appspot.com/sightings/add/

 - Edit: update a particular sighting with its unique squirrel ID

    located at: https://neat-sunspot-255500.appspot.com/sightings/<unique_squirrel_id>/


 - Statistics of Squirrel Data: Show general statistics of the current data set

    located at: https://neat-sunspot-255500.appspot.com/sightings/stats/

## Build with
Django 2.2.7

Python3

sqlite3

HTML

OpenStreetMap: https://www.openstreetmap.org/about/

## Group Name and Section
Project Group 15

Section 2

## Contributors
Laura Wang and Jueran Ren

UNIs: [lw2884, jr3982]

## Deployment

The deployment of the application is done on Google Cloud Server.

Link:
https://neat-sunspot-255500.appspot.com



