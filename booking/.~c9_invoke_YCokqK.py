from django import forms
from .models import Booking
import datetime

class BookingForm(forms.Form):

    date
    date = forms.DateField(initial = datetime.date.today)
    date.widget.attrs = {'class': 'd'}
    time = forms.TimeField()


