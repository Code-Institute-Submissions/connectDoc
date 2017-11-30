from django.shortcuts import render, get_object_or_404
from medicalPractice.models import Doctor
# Create your views here.

def booking(request, id):
    doctor= get_object_or_404(Doctor, pk=id)
    return render(request, 'booking.html', {'doctor': doctor})