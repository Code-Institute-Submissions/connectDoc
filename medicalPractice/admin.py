from django.contrib import admin
from .models import Doctor, DoctorImage, Patient, MedicalPractice

# Register your models here.
admin.site.register(MedicalPractice)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(DoctorImage)