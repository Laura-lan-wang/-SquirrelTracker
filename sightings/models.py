from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Squirrel(models.Model):

    X = models.FloatField(
        help_text = _("Longitude")
    )

    Y = models.FloatField(
        help_text = _("Latitude")
    )

    Unique_Squirrel_ID = models.CharField(
        help_text = _("Unique_Squirrel_ID"),
        max_length = 50
    )

    AM = "AM"
    PM = "PM"

    SHIFT_CHOICES = (
        (AM,"AM"),
        (PM,"PM")
    )

    Shift = models.CharField (
        help_text = _("AM or PM Shift"),
        max_length = 2,
        choices = SHIFT_CHOICES,
    )

    Date = models.DateField(
        help_text = _("Date")
    )

    ADULT = "Adult"
    JUVENILE = "Juvenile"
    BLANK = ""
    UNKNOWN = "?"

    AGE_CHOICES = (
        (ADULT,"Adult"),
        (JUVENILE, "Juvenile"),
        (BLANK, ""),
        (UNKNOWN, "?")
    )

    Age = models.CharField(
        help_text = _("Age of Squirrel"),
        max_length = 10,
        choices = AGE_CHOICES,
        default = BLANK,
        null=True,
        blank = True,
    )

    GRAY = "Gray"
    BLACK = "Black"
    CINNAMMON = "Cinnammon"
    BLANK = ""


    PRIMARY_COLOR_CHOICES = (
        (GRAY, "Gray"),
        (BLACK,"Black"),
        (CINNAMMON, "Cinnammon"),
        (BLANK, "")
    )

    Primary_Fur_Color = models.CharField(
        help_text = _("Primary Fur Color"),
        choices = PRIMARY_COLOR_CHOICES,
        max_length = 10,
        default = True,
        null=True,
        blank = True,
    )


    
    AG = 'Above Ground'
    GP = 'Ground Plane'
    BLANK = ''
    
    LOCATION_CHOICES = (
        (AG, "Above Ground"),
        (GP, "Ground Plane"),
        (BLANK, "")
    )

    Location = models.CharField(
       help_text=_('Location'),
       choices = LOCATION_CHOICES,
       max_length = 20,
       default = BLANK,
       null = True,
   )

    Specific_Location = models.CharField(
        help_text = _('Specific Locaton'),
        max_length = 50,
        null = True,
        blank = True,
    )
    TRUE = 'TRUE'
    FALSE = 'FALSE'

    TF_CHOICES = (
        (TRUE, 'TRUE'),
        (FALSE, "FALSE")
    )

    Running = models.CharField(
        help_text=_('Running'),
        choices=TF_CHOICES,
        default=FALSE,
        max_length=5,
        null=True
    )
    Chasing = models.CharField(
        help_text=_('Chasing'),
        choices=TF_CHOICES,
        default=FALSE,
        max_length=5,
        null=True
    )
    Climbing = models.CharField(
        help_text=_('Climbing'),
        choices=TF_CHOICES,
        default=FALSE,
        max_length=5,
        null=True
    )
    Eating = models.CharField(
        help_text =_('Eating'),
        choices=TF_CHOICES,
        default=FALSE,
        max_length=5,
        null=True
    )
    Foraging = models.CharField(
        help_text=_('Foraging'),
        choices=TF_CHOICES,
        default=FALSE,
        max_length=5,
        null=True
    )
    Other_Activities = models.CharField(
        help_text=_('Other Activities'),
        max_length=100,
        null=True,
        blank=True,
    )
    Kuks = models.CharField(
        help_text=_('Kuks'),
        choices=TF_CHOICES,
        default=FALSE,
        max_length=5,
        null=True
    )
    Quaas = models.CharField(
        help_text=_('Quaas'),
        choices=TF_CHOICES,
        default=FALSE,
        max_length=5,
        null=True
    )
    Moans = models.CharField(
        help_text=_('Moans'),
        choices=TF_CHOICES,
        default=FALSE,
        max_length=5,
        null=True
    )
    Tail_Flags = models.CharField(
        help_text=_('Tail flags'),
        choices=TF_CHOICES,
        default=FALSE,
        max_length=5,
        null=True
    )
    Tail_Twitches = models.CharField(
        help_text=_('Tail twitches'),
        choices=TF_CHOICES,
        default=FALSE,
        max_length=5,
        null=True
    )
    Approaches = models.CharField(
        help_text=_('Approaches'),
        choices=TF_CHOICES,
        default=FALSE,
        max_length=5,
        null=True
    )
    Indifferent = models.CharField(
        help_text=_('Indifferent'),
        choices=TF_CHOICES,
        default=FALSE,
        max_length=5,
        null=True
    )
    Runs_From = models.CharField(
        help_text=_('Runs from'),
        choices=TF_CHOICES,
        default=FALSE,
        max_length=5,
        null=True
    )















