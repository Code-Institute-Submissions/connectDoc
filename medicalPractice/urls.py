from django.conf.urls import url, include
from .views import all_doctors, do_search, practice_details
from booking.views import booking

urlpatterns = [
    url(r'^$', all_doctors, name='medicalPractice'),
    url(r'^search/', do_search, name='search'),
    url(r'^(\d+)$', practice_details, name='practice_details'),
    url(r'^(\d+)/booking$', booking, name='booking'),
]