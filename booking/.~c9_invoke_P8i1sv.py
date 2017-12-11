from django import forms
from .models import Booking
import datetime

class BookingForm(forms.Form):

    doctorText = forms.CharField()
    doctorText = forms.Cha    
    date.widget.attrs = {'class': 'd'}
    time = forms.TimeField()


