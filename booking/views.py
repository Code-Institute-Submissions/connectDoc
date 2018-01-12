from django.shortcuts import render, get_object_or_404
from medicalPractice.models import Doctor
from .forms import BookingForm

# Create your views here.


    # doctor = get_object_or_404(Doctor, pk=id)
    # return render(request, 'booking.html', {'doctor': doctor})

def booking(request, id):
    doctor = get_object_or_404(Doctor, pk=id)
    if request.method=="POST":
        booking_form = BookingForm(request.POST)

    else:
        booking_form = BookingForm()

    # booking = booking_form.save()




    return render(request, "booking.html", {'doctor': doctor, 'booking_form': booking_form})