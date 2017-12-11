from django import forms
from .models import Booking
from djan

class BookingForm(forms.Form):

    doctorText = forms.CharField()
    date = forms.DateField(initial = datetime.date.today)
    date.widget.attrs = {'class': 'd'}
    time = forms.TimeField()


