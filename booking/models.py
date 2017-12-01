from django.db import models
from medicalPractice.models import Doctor, Patient
from datetime import time 

TIME_SLOTS=(
    (time(8, 00, 00), u'8:00 AM'),
    (time(8, 15, 00), u'8:15 AM'),
    (time(8, 30, 00), u'8:30 AM'),
    (time(8, 45, 00), u'8:45 AM'),
    (time(9, 00, 00), u'9:00 AM'),
    (time(9, 15, 00), u'9:15 AM'),
    (time(9, 30, 00), u'9:30 AM'),
    (time(9, 45, 00), u'9:45 AM'),
    (time(10, 00, 00), u'10:00 AM'),
    (time(10, 15, 00), u'10:15 AM'),
    (time(10, 30, 00), u'10:30 AM'),
    (time(10, 45, 00), u'10:45 AM'),
    (time(11, 00, 00), u'11:00 AM'),
    (time(11, 15, 00), u'11:15 AM'),
    (time(11, 30, 00), u'11:30 AM'),
    (time(11, 45, 00), u'11:45 AM'),
    (time(12, 00, 00), u'12:00 AM'),
    (time(12, 15, 00), u'12:15 AM'),
    (time(12, 30, 00), u'12:30 AM'),
    (time(12, 45, 00), u'12:45 AM'),
    (time(13, 00, 00), u'1:00 PM'),
    (time(13, 15, 00), u'1:15 PM'),
    (time(13, 30, 00), u'1:30 PM'),
    (time(13, 45, 00), u'1:45 PM'),
    (time(14, 00, 00), u'2:00 PM'),
    (time(14, 15, 00), u'2:15 PM'),
    (time(14, 30, 00), u'2:30 PM'),
    (time(14, 45, 00), u'2:45 PM'),
    (time(15, 00, 00), u'3:00 PM'),
    (time(15, 15, 00), u'3:15 PM'),
    (time(15, 30, 00), u'3:30 PM'),
    (time(15, 45, 00), u'3:45 PM'),
    (time(16, 00, 00), u'4:00 PM'),
    (time(16, 15, 00), u'4:15 PM'),
    (time(16, 30, 00), u'4:30 PM'),
    (time(16, 45, 00), u'4:45 PM'),
    (time(17, 00, 00), u'5:00 PM'),
    (time(17, 15, 00), u'5:15 PM'),
    (time(17, 30, 00), u'5:30 PM'),
    (time(17, 45, 00), u'5:45 PM'),
    (time(18, 00, 00), u'6:00 PM'),
    (time(18, 15, 00), u'6:15 PM'),
    (time(18, 30, 00), u'6:30 PM'),
    (time(18, 45, 00), u'6:45 PM'),
    (time(19, 00, 00), u'7:00 PM'),
    (time(19, 15, 00), u'7:15 PM'),
    (time(19, 30, 00), u'7:30 PM'),
    (time(19, 45, 00), u'7:45 PM'),
    
    )

# Create your models here.
class Booking(models.Model):
    doctor = models.ForeignKey(Doctor)
    patient = models.ForeignKey(Patient)
    date = models.DateField()
    time = models.TimeField(choices= TIME_SLOTS)
    
    
    
# class Foo(models.Model):
#     GENDER_CHOICES = (
#     (M = "MALE"), 
#     (F = "FEMALE"), 
    
# # )
# name=models.CharField(max_length=60)gender=models.CharField(max_length=2,choices=GENDER_CHOICES)