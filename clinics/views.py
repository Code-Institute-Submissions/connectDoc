from django.shortcuts import render, get_object_or_404
from medicalPractice.models import MedicalPractice

# Create your views here.
def get_clinic(request, id):
    clinic = get_object_or_404(MedicalPractice, pk=id)
    return render(request, 'clinic.html', {'clinic': clinic})
    
    
def all_clinics(request): 
    clinics = MedicalPractice.objects.all()
    return render (request, 'all_clinics.html', {'clinics': clinics})
    
