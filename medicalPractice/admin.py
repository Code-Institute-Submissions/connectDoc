from django.contrib import admin
from .models import Doctor, DoctorImage

# Register your models here.
admin.site.register(Doctor)
admin.site.register(DoctorImage)