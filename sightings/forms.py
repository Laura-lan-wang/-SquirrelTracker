from django.forms import ModelForm
from .models import Squirrel


class SquirrelForm(ModelForm):
    class Meta:
        model = Squirrel
        all_fields = [f.name for f in Squirrel._meta.get_fields()]
        fields = []
        fields.extend(all_fields)