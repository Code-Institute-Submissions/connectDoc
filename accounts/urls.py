from django.conf.urls import url, include
from .views import logout, login, registerDoctor, registerPatient, profile
# import urls_reset
from . import urls_reset




urlpatterns = [
    url(r'^logout', logout, name="logout"),
    url(r'^login', login, name="login"),
    url(r'^register/doctor', registerDoctor, name="register_doctor"),
    url(r'^register/patient', registerPatient, name="register_patient"),
    url(r'^profile', profile, name="profile"),
    url(r'^password-reset/', include(urls_reset)),



    
    ]