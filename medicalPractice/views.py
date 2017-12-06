from django.shortcuts import render, get_object_or_404
from .models import Doctor, MedicalPractice
from django.db.models import Q

# Create your views here.
# def do_search(request):
#     query=request.GET['search_box']
#     doctors = Doctor.objects.filter(Q(name__icontains=query) | Q(practice__icontains=query) | Q(location__icontains=query))
#     return render(request, "medical_practice.html", {"doctors": doctors})


def all_doctors(request):
    medicalPractice = Doctor.objects.all()
    return render(request, "medical_practice.html", {"medicalPractice": medicalPractice})
    
    
def practice_details(request, id):
    this_doctor = get_object_or_404(Doctor, pk=id)
    practices = get_object_or_404(MedicalPractice, pk=id)
    return render(request, "practice_detail.html", {"doctor" : this_doctor, "practices": practices})
    
