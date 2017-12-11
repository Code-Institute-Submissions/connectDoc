from django import forms
from .models import Booking
import datetime

    test = forms.CharField(lable='t')

    doctorText = forms.CharField()
    date = forms.DateField(initial = datetime.date.today)
    date.widget.attrs = {'class': 'd'}
    time = forms.TimeField()


