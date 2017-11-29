from django.db import models
from geoposition.fields import GeopositionField


class Doctor(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    practice = models.CharField(max_length=50, default="independent")
    location = models.CharField(max_length=254, default='')
    position = GeopositionField(blank=True)
    
    def __str__(self):
        return self.name
        
class DoctorImage(models.Model):
    medicalPractice = models.ForeignKey(Doctor, related_name='images')
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return str(self.image)
        
