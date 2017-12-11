from django import forms
from .models import Booking
import datetime

class BookingForm(forms.Form):

    MONTH_CHOICES = [(i, i,) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i,) for i in range(2017, 2036)]
    DAY_CHOICES = [(i, i,) for i in range(1, 8)]
    TIME_CHOICES = [(i, i,) for i in range(1, 24)]

    date = forms.DateField(initial = datetime.date.today)
    date.widget.attrs = {'class': 'datepicker'}
    time = forms.TimeField()
    booking_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES, required=False)
    booking_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES, required=False)
    booking_day = forms.ChoiceField(label="Day", choices=DAY_CHOICES, required=False)
    booking_time = forms.ChoiceField(label="Time", choices=TIME_CHOICES, required=False)

    # credit_card_number = forms.CharField(label='Credit card number', required=False)
    # cvv = forms.CharField(label='Security code (CVV)', required=False)

    # stripe_id = forms.CharField(widget=forms.HiddenInput)

