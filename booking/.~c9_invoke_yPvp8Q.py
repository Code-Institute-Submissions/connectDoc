from django import forms
from .models import Booking
import datetime

class BookingForm(forms.Form):

    doctorText = forms.CharField()
    date = forms.DateField(initial = datetime.date.today)
    date.widget.attrs = 
    time = forms.TimeField()


