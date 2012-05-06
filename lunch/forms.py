from models import Lunch
from django.forms.models import ModelForm 
from django.forms import DateField, TimeField
from django.forms import extras
from widgets import SelectTimeWidget

class LunchForm(ModelForm):
    date = DateField()
    time = TimeField()
    class Meta:
        model = Lunch