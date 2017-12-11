from django import forms
from .models import Booking
import datetime

class BookingForm(forms.Form):

    doctorText = forms.CharField()
    date = forms.DateField(initial = datetime.datetime.now())
    date.widget.attrs = {'class': 'd'}
    time = forms.TimeField()


