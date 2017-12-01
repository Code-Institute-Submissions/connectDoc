from django.db import models
from geoposition.fields import GeopositionField
from django.contrib.auth.models import User  

class MedicalPractice(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    address = models.TextField(max_length=254, default='')
    position = GeopositionField(blank=True)
    
    def __str__(self):
        return self.name

class Doctor(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    practice = models.ForeignKey(MedicalPractice, blank=False)

    def __str__(self):
        return self.name

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=254, default='')
    date_of_birth = models.CharField(max_length=254, default='')

    def __str__(self):
        return self.name


        
class DoctorImage(models.Model):
    medicalPractice = models.ForeignKey(Doctor, related_name='images')
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return str(self.image)
        
        

        
