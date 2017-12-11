from django import forms
from .models import Booking
import datetime

class BookingForm(forms.Form):

    date = forms.F
    date = forms.DateField(initial = datetime.date.today)
    date.widget.attrs = {'class': 'd'}
    time = forms.TimeField()


