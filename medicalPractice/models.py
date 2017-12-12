from django.db import models
from geoposition.fields import GeopositionField
from django.contrib.auth.models import User

class MedicalPractice(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    address = models.TextField(max_length=254, default='')
    location = models.CharField(max_length=100)
    position = GeopositionField(blank=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE, related_name="Doctor")
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    location = models.CharField(max_length=100)
    practice = models.ForeignKey(MedicalPractice, blank=False, related_name='doctors')

    def __str__(self):
        if self.name != "":
            return self.name
        else:
            return self.user.first_name + " " + self.user.last_name

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Patient")
    name = models.CharField(max_length=254, default='')
    date_of_birth = models.CharField(max_length=254, default='')

    def __str__(self):
        return self.user.last_name + ", " + self.user.first_name


class Clinic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Clinic")
    name = models.CharField(max_length=254, default='')
    address = models.CharField(max_length=254, default='')

    def __str__(self):
        return self.user.last_name + ", " + self.user.first_name



class DoctorImage(models.Model):
    medicalPractice = models.ForeignKey(Doctor, related_name='images')
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return str(self.image)




