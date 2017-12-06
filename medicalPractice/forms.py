from django import forms
from .models import Doctor, Patient

class DoctorRegistrationForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=['description', 'price', 'image', 'practice', ]

        
class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=['date_of_birth']
