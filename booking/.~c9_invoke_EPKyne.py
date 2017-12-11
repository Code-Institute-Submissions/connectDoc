from django import forms
from .models import Booking
import datetime

class BookingForm(forms.Form):

    doctorText = forms.CharField()
    date = forms.DateField(widginitial=datetime.date.today)
    date.widget.attrs = {'class': 'd'}
    time = forms.TimeField()


